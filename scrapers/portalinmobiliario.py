import json
import re
import time

import pandas as pd
import requests


BASE_URL = "https://www.portalinmobiliario.com"
UF_API_URL = "https://mindicador.cl/api/uf"

RESULTS_PER_PAGE = 48
MAX_PAGES = 100
SLEEP_SECONDS = 1

HEADERS = {
    "Accept": "text/html",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126 Safari/537.36"
    ),
}

SEARCHES = [
    {
        "operation": "venta",
        "property_type": "departamento",
        "location": "providencia-metropolitana",
    },
]


# sort by publication date (newest first) so genuinely new listings always
# land on the first pages, inside the ~2000-result window the site exposes
SORT_NEWEST = "_OrderId_BEGINS*DESC_NoIndex_True"


def build_page_url(search, page):
    url = (
        f"{BASE_URL}/{search['operation']}"
        f"/{search['property_type']}"
        f"/{search['location']}"
        "/"
    )

    if page > 0:
        url += f"_Desde_{page * RESULTS_PER_PAGE + 1}"

    url += SORT_NEWEST

    return url


def extract_state(html):
    match = re.search(r"_n\.ctx\.r=(\{.*)", html, re.DOTALL)

    if not match:
        return None

    state, _ = json.JSONDecoder().raw_decode(match.group(1))
    return state


def iter_polycards(state):
    results = (
        state
        .get("appProps", {})
        .get("pageProps", {})
        .get("initialState", {})
        .get("results", [])
    )

    for result in results:
        if not isinstance(result, dict):
            continue

        cards = []

        if "polycard" in result:
            cards.append(result["polycard"])

        for item in result.get("items", []):
            if isinstance(item, dict) and "polycard" in item:
                cards.append(item["polycard"])

        yield from cards


def get_component(card, component_id):
    for component in card.get("components", []):
        if component.get("id") == component_id:
            return component.get(component.get("type"), {})

    return {}


def parse_int(text):
    match = re.search(r"(\d+)", text or "")
    return int(match.group(1)) if match else None


def parse_attributes(card):
    texts = get_component(card, "attributes_list").get("texts", [])

    bedrooms_text = bathrooms_text = m2_text = None
    bedrooms_n = bathrooms_n = m2_utiles = None

    for text in texts:
        if "dormitorio" in text or "ambiente" in text.lower():
            bedrooms_text = text

            # only single values ("3 dormitorios"), not ranges ("2 a 3")
            if " a " not in text:
                bedrooms_n = parse_int(text)
        elif "baño" in text:
            bathrooms_text = text

            if " a " not in text:
                bathrooms_n = parse_int(text)
        elif "m²" in text:
            m2_text = text

            if "-" not in text and " a " not in text:
                m2_utiles = parse_int(text)

    return {
        "bedrooms": bedrooms_text,
        "bedrooms_n": bedrooms_n,
        "bathrooms": bathrooms_text,
        "bathrooms_n": bathrooms_n,
        "m2": m2_text,
        "m2_utiles": m2_utiles,
    }


def parse_seller(card):
    text = get_component(card, "seller").get("text") or ""
    seller = re.sub(r"\{[^}]*\}", "", text).strip()

    return seller or None, "icon_cockade" in text


def parse_barrio(location_text):
    parts = [p.strip() for p in (location_text or "").split(",") if p.strip()]

    if len(parts) < 2:
        return None

    barrio = parts[-2]

    # a digit means it's a street address, not a neighborhood
    return None if re.search(r"\d", barrio) else barrio


def parse_card(card, search):
    metadata = card.get("metadata", {})
    listing_id = metadata.get("id")

    # pads are paid placements, often from other comunas
    if not listing_id or metadata.get("is_pad") == "true":
        return None

    url = metadata.get("url", "")

    if url and not url.startswith("http"):
        url = "https://www." + url

    price = get_component(card, "price").get("current_price", {})
    price_value = price.get("value")
    currency = price.get("currency")

    attributes = parse_attributes(card)
    seller, tienda_oficial = parse_seller(card)

    location = get_component(card, "location").get("text")
    is_project = "DEVELOPMENT" in (metadata.get("domain_id") or "")

    return {
        "title": get_component(card, "title").get("text", "").strip(),
        "price": price_value,
        "currency": currency,
        **attributes,
        "seller": seller,
        "tienda_oficial": tienda_oficial,
        "location": location,
        "barrio": parse_barrio(location),
        "property_kind": "proyecto" if is_project else "usada",
        "listing_id": listing_id,
        "operation": search["operation"],
        "property_type": search["property_type"],
        "comuna": search["location"],
        "source": "portalinmobiliario",
        "url": url,
    }


def scrape_search(search):
    listings = []
    seen_ids = set()

    for page in range(MAX_PAGES):
        url = build_page_url(search, page)

        try:
            response = requests.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
        except Exception as e:
            print(f"Portalinmobiliario page {page + 1} failed: {e}")
            break

        state = extract_state(response.text)

        if state is None:
            print(f"Portalinmobiliario page {page + 1}: no embedded state")
            break

        page_listings = []

        for card in iter_polycards(state):
            listing = parse_card(card, search)

            if listing and listing["listing_id"] not in seen_ids:
                seen_ids.add(listing["listing_id"])
                page_listings.append(listing)

        if not page_listings:
            break

        print(
            f"Portalinmobiliario {search['operation']} "
            f"{search['location']} page {page + 1}: "
            f"{len(page_listings)} listings"
        )

        listings.extend(page_listings)
        time.sleep(SLEEP_SECONDS)

    return listings


def parse_clp_amount(text):
    digits = re.sub(r"\D", "", text or "")
    return int(digits) if digits else None


# fallback coordinates the site uses when a listing has no real location
DEFAULT_COORDINATES = (-35.675148, -71.54297)


def parse_coordinates(html_text):
    match = re.search(
        r'"latitude":"(-?\d+\.?\d*)","longitude":"(-?\d+\.?\d*)"',
        html_text,
    ) or re.search(
        r'"latitude":(-?\d+\.?\d*),"longitude":(-?\d+\.?\d*)',
        html_text,
    )

    if not match:
        return None, None

    lat, lng = float(match.group(1)), float(match.group(2))

    if (round(lat, 4), round(lng, 4)) == (
        round(DEFAULT_COORDINATES[0], 4),
        round(DEFAULT_COORDINATES[1], 4),
    ):
        return None, None

    return lat, lng


PUBLICADO_UNIT_DAYS = {"día": 1, "mes": 30, "año": 365}


def parse_publicado_hace(html_text):
    """Extract the header's relative "Publicado hace ..." age.

    The site only exposes this human-readable text (no exact date), so the
    day count is approximate and gets coarser with age. Project pages
    (property_kind "proyecto") don't show it at all.
    """
    match = re.search(
        r"Publicado (hoy|ayer|hace \d+ (?:días?|mes(?:es)?|años?))",
        html_text,
    )

    if not match:
        return None, None

    text = match.group(1)

    if text == "hoy":
        return text, 0

    if text == "ayer":
        return text, 1

    amount = int(re.search(r"\d+", text).group())
    unit = re.search(r"(día|mes|año)", text).group(1)

    return text, amount * PUBLICADO_UNIT_DAYS[unit]


def parse_zona_uf_m2(html_text):
    """Extract the site's "Promedio en la zona" UF/m² from the price comparison widget."""
    start = html_text.find('{"id":"price_comparison"')

    if start == -1:
        return None

    try:
        component, _ = json.JSONDecoder().raw_decode(html_text[start:])
    except ValueError:
        return None

    paragraphs = component.get("extra_info", {}).get("paragraph", [])

    for paragraph in paragraphs:
        if paragraph.get("title", {}).get("text") == "Promedio en la zona":
            return parse_int(paragraph.get("value", {}).get("text"))

    return None


def fetch_listing_details(url):
    """Fetch parking, common expenses and coordinates from a detail page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"Detail fetch failed: {url} ({e})")
        return None

    lat, lng = parse_coordinates(response.text)
    publicado_texto, publicado_dias = parse_publicado_hace(response.text)

    details = {
        "lat": lat,
        "lng": lng,
        "zona_uf_m2": parse_zona_uf_m2(response.text),
        "publicado_hace": publicado_texto,
        "publicado_fecha_est": (
            (pd.Timestamp.today() - pd.Timedelta(days=publicado_dias))
            .strftime("%Y-%m-%d")
            if publicado_dias is not None
            else None
        ),
    }

    attributes = {}
    start = response.text.find('{"id":"technical_specifications"')

    if start != -1:
        try:
            specs_component, _ = (
                json.JSONDecoder().raw_decode(response.text[start:])
            )
        except ValueError:
            specs_component = {}

        for spec in specs_component.get("specs", []):
            for attribute in spec.get("attributes", []):
                attributes[attribute.get("id")] = attribute.get("text")

    def count_of(attribute_id):
        if attribute_id in attributes:
            return parse_int(attributes[attribute_id])

        # a spec sheet without the attribute means none
        return 0 if attributes else None

    details["parking"] = count_of("Estacionamientos")
    details["bodegas"] = count_of("Bodegas")

    details["gastos_comunes_clp"] = parse_clp_amount(
        attributes.get("Gastos comunes")
    )

    antiguedad = attributes.get("Antigüedad")

    if antiguedad and "estrenar" in antiguedad.lower():
        details["antiguedad_anos"] = 0
    else:
        details["antiguedad_anos"] = parse_int(antiguedad)

    details["m2_totales"] = parse_int(attributes.get("Superficie total"))
    details["m2_terraza"] = parse_int(attributes.get("Superficie de terraza"))
    details["piso_unidad"] = parse_int(
        attributes.get("Número de piso de la unidad")
    )
    details["pisos_edificio"] = parse_int(attributes.get("Cantidad de pisos"))
    details["deptos_por_piso"] = parse_int(
        attributes.get("Departamentos por piso")
    )
    details["orientacion"] = attributes.get("Orientación")

    return details


def fetch_uf_value():
    try:
        response = requests.get(UF_API_URL, timeout=30)
        response.raise_for_status()
        value = response.json()["serie"][0]["valor"]
        print(f"UF value: {value:,.2f} CLP")
        return value
    except Exception as e:
        print(f"UF value fetch failed: {e}")
        return None


def add_price_conversions(df, uf_value):
    in_uf = df["currency"] == "CLF"
    in_clp = df["currency"] == "CLP"

    df["price_uf"] = df["price"].where(in_uf)
    df["price_clp"] = df["price"].where(in_clp)

    if uf_value:
        df.loc[in_uf, "price_clp"] = (df.loc[in_uf, "price"] * uf_value).round()
        df.loc[in_clp, "price_uf"] = (df.loc[in_clp, "price"] / uf_value).round(1)

    df["uf_per_m2"] = (df["price_uf"] / df["m2_utiles"]).round(2)

    return df


def scrape_portalinmobiliario():
    listings = []

    for search in SEARCHES:
        listings.extend(scrape_search(search))

    df = pd.DataFrame(listings)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["listing_id"], keep="first")
    df = add_price_conversions(df, fetch_uf_value())

    return df
