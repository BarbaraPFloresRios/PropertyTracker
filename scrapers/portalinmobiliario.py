"""Scraper for portalinmobiliario.com (MercadoLibre's Chilean real estate site).

No browser is needed: every search page ships its whole React state as a JSON
blob inside the HTML, so we read that instead of parsing the DOM. Two levels:

  search pages  -> scrape_search()         one card per listing, cheap, paginated
  detail pages  -> fetch_listing_details() coordinates, specs, publication age

THIS IS THE MOST FRAGILE FILE IN THE PROJECT. Everything here depends on the
shape of someone else's undocumented JSON, which changes without notice. When
the pipeline suddenly returns nothing, the breakage is almost certainly in
extract_state() or iter_polycards() -- start there, and see the diagnostics
note in scrape_search().
"""
import json
import re
import time
from pathlib import Path

import pandas as pd
import requests


BASE_URL = "https://www.portalinmobiliario.com"
UF_API_URL = "https://mindicador.cl/api/uf"

# last known UF value, committed so a failed API call can fall back to it
UF_CACHE_PATH = Path("data/uf_value.json")

RESULTS_PER_PAGE = 48

# Upper bound on the pagination loop, not an expectation: the site caps results
# at ~2,016 per search (42 pages), and scrape_search() stops as soon as a page
# comes back with no usable listings. Raising this does not widen the window.
MAX_PAGES = 100

SLEEP_SECONDS = 1

# A browser-like User-Agent is required: the site answers requests without one
# differently (and the embedded state can be missing entirely).
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
    {
        "operation": "venta",
        "property_type": "departamento",
        "location": "las-condes-metropolitana",
    },
    {
        "operation": "venta",
        "property_type": "departamento",
        "location": "santiago-metropolitana",
    },
]

SEARCHES_ARRIENDO = [
    {
        "operation": "arriendo",
        "property_type": "departamento",
        "location": "providencia-metropolitana",
    },
    {
        "operation": "arriendo",
        "property_type": "departamento",
        "location": "las-condes-metropolitana",
    },
    {
        "operation": "arriendo",
        "property_type": "departamento",
        "location": "santiago-metropolitana",
    },
]


# sort by publication date (newest first) so genuinely new listings always
# land on the first pages, inside the ~2000-result window the site exposes
SORT_NEWEST = "_OrderId_BEGINS*DESC_NoIndex_True"

# a removed/expired listing still returns HTTP 200 but its detail page carries
# this exact modal text (absent on live pages)
FINISHED_MARKER = '"text":"Publicación finalizada"'

# sentinel returned by fetch_listing_details when the page says finished
LISTING_FINISHED = object()


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
    """Pull the page's embedded React state out of the HTML.

    The site assigns its whole state to a JS global, `_n.ctx.r={...}`, followed
    by more script. raw_decode() reads just the object and ignores whatever
    trails it, which is why we can't use json.loads() on the match.

    Returning None means the marker wasn't there -- either the site renamed the
    global (code change needed) or it served a page without state at all, which
    is what an IP block looks like. scrape_search() prints the response length
    so the two can be told apart.
    """
    match = re.search(r"_n\.ctx\.r=(\{.*)", html, re.DOTALL)

    if not match:
        return None

    state, _ = json.JSONDecoder().raw_decode(match.group(1))
    return state


def iter_polycards(state):
    """Yield every listing card in the state, flattening the two shapes it uses.

    Cards live under appProps.pageProps.initialState.results, where an entry is
    either a card itself ("polycard") or a group holding several in "items"
    (carousels, grouped developments). Both shapes appear on the same page, so
    both are walked -- missing the second silently drops listings.
    """
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
    """Return a card component's payload by id.

    Note the double indirection: a component declares its own `type`, and the
    payload sits under a key *named* by that type -- e.g. an id="price" entry
    carries {"type": "price", "price": {...}}. Hence .get(.get("type")).
    An unknown id gives {} so callers can chain .get() without guarding.
    """
    for component in card.get("components", []):
        if component.get("id") == component_id:
            return component.get(component.get("type"), {})

    return {}


def parse_int(text):
    match = re.search(r"(\d+)", text or "")
    return int(match.group(1)) if match else None


def parse_attributes(card):
    """Split the card's attribute strings into text and numeric columns.

    The numeric column is filled ONLY when the text holds a single value:
    developments publish ranges ("2 a 3 dormitorios", "45 - 60 m²"), and
    picking a number out of a range would invent precision the listing
    doesn't have. The raw text is always kept alongside it.
    """
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
    """Return (seller name, is official store).

    The seller string interleaves icon placeholders in braces, e.g.
    "{icon_cockade} Some Agency", so braces are stripped to get the name.
    The cockade icon is the site's badge for an official store.
    """
    text = get_component(card, "seller").get("text") or ""
    seller = re.sub(r"\{[^}]*\}", "", text).strip()

    return seller or None, "icon_cockade" in text


def parse_barrio(location_text):
    """Pull the neighborhood out of the card's location line.

    The line reads "<something>, <barrio>, <comuna>", so the barrio is the
    second-to-last part. But "<something>" is sometimes a street address, and
    then the second-to-last part is the street -- any digit in it means that,
    and we'd rather have no barrio than a street name in the barrio column.
    """
    parts = [p.strip() for p in (location_text or "").split(",") if p.strip()]

    if len(parts) < 2:
        return None

    barrio = parts[-2]

    # a digit means it's a street address, not a neighborhood
    return None if re.search(r"\d", barrio) else barrio


def parse_card(card, search):
    """Flatten one search-result card into a flat dict (one CSV row).

    Everything here comes from the search page, so it is cheap but partial:
    coordinates, specs and publication age need the detail page -- see
    fetch_listing_details().
    """
    metadata = card.get("metadata", {})
    listing_id = metadata.get("id")

    # Pads are paid placements. They're dropped because they often belong to a
    # different comuna than the one being searched and duplicate results that
    # already appear organically.
    if not listing_id or metadata.get("is_pad") == "true":
        return None

    url = metadata.get("url", "")

    if url and not url.startswith("http"):
        url = "https://www." + url

    # currency is a code, not a symbol: "CLF" is UF, "CLP" is pesos.
    # add_price_conversions() turns one into the other.
    price = get_component(card, "price").get("current_price", {})
    price_value = price.get("value")
    currency = price.get("currency")

    attributes = parse_attributes(card)
    seller, tienda_oficial = parse_seller(card)

    location = get_component(card, "location").get("text")

    # Developments ("proyecto") behave differently all over this file: ranges
    # instead of single values for m2/bedrooms, and no publication date on the
    # detail page.
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
    """Page through one search, newest first, until the results run out.

    DIAGNOSTICS -- the two break messages below mean different things, and
    telling them apart is the fastest way to triage a run that returned nothing:

      "no embedded state (status=200, len=N)"
          The page had no `_n.ctx.r=` marker. Either the site changed that
          global (code fix needed) or it served a contentless page, which is
          what this site does to datacenter IPs rather than returning 403.

      "0 usable listings (status=200, raw_cards=N)"
          State parsed fine. raw_cards=0 means the search itself came back
          empty -- normal at the end of pagination, suspicious on page 1.
          raw_cards>0 with 0 usable means parse_card() rejected every card,
          i.e. the card shape changed.

    Pagination stops on its own well before MAX_PAGES: the site exposes ~2,016
    results per search (42 pages) and page 43 returns 404.
    """
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
            print(
                f"Portalinmobiliario page {page + 1}: no embedded state "
                f"(status={response.status_code}, len={len(response.text)})"
            )
            break

        page_listings = []
        raw_cards = list(iter_polycards(state))

        for card in raw_cards:
            listing = parse_card(card, search)

            if listing and listing["listing_id"] not in seen_ids:
                seen_ids.add(listing["listing_id"])
                page_listings.append(listing)

        if not page_listings:
            print(
                f"Portalinmobiliario page {page + 1}: 0 usable listings "
                f"(status={response.status_code}, raw_cards={len(raw_cards)})"
            )
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
    """Extract lat/lng from the detail page, treating the site's fallback as missing.

    Two regexes because the numbers appear quoted on some pages and bare on
    others. When a listing has no real location the site fills in the centroid
    of Chile (DEFAULT_COORDINATES) -- plotting that would scatter listings in
    the middle of the country, so it's reported as absent instead.
    """
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
    """Extract the site's "Promedio en la zona" UF/m² from the price comparison widget.

    NOT SHOWN IN ANY OUTPUT, on purpose: this is the site's own marketing
    figure, not a valuation. Measured over the active set, it sits ABOVE the
    asking price of the very listing it describes in 66% of cases (median gap
    +10.6%), making almost everything look like a bargain; and of 1,839
    buildings with 3+ listings at identical coordinates, 66% carry more than
    one value for it -- up to 92 UF/m² apart within the same building. A figure
    that varies per listing is not a property of the area.

    Still collected because the detail page is fetched anyway, so it costs
    nothing and keeps the historical series auditable.
    """
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
    """Fetch coordinates, specs and publication age from one detail page.

    Three possible returns, and callers must handle all three:
      dict             -> the details
      LISTING_FINISHED -> the page says "Publicación finalizada" (removed)
      None             -> the request failed (timeout, 403, 429). Callers leave
                          enriched_date unset so the listing is retried next
                          run rather than being stored as having no data.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"Detail fetch failed: {url} ({e})")
        return None

    if FINISHED_MARKER in response.text:
        return LISTING_FINISHED

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
        """Count for a spec-sheet attribute, distinguishing zero from unknown.

        Listed    -> its number.
        Absent but the sheet parsed  -> 0, because the site omits attributes
                                        the property doesn't have.
        No sheet at all              -> None (unknown), so a page that failed
                                        to parse isn't recorded as "has none".
        """
        if attribute_id in attributes:
            return parse_int(attributes[attribute_id])

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

        UF_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        UF_CACHE_PATH.write_text(json.dumps({
            "date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "value": value,
        }))

        print(f"UF value: {value:,.2f} CLP")
        return value
    except Exception as e:
        print(f"UF value fetch failed: {e}")

        # the UF moves ~0.01%/day, so yesterday's value is fine for the map.
        # Far better than dropping every UF-priced listing (~96% of the corpus).
        if UF_CACHE_PATH.exists():
            cached = json.loads(UF_CACHE_PATH.read_text())
            print(
                f"Using cached UF from {cached['date']}: "
                f"{cached['value']:,.2f} CLP"
            )
            return cached["value"]

        # no API and no cache: die loudly rather than publish an empty map
        raise RuntimeError("No UF value available (API failed, no cache)") from e


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


def scrape_portalinmobiliario(searches=SEARCHES):
    listings = []

    for search in searches:
        listings.extend(scrape_search(search))

    df = pd.DataFrame(listings)

    if df.empty:
        return df

    df = df.drop_duplicates(subset=["listing_id"], keep="first")
    df = add_price_conversions(df, fetch_uf_value())

    return df
