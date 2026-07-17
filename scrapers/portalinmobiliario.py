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


def build_page_url(search, page):
    url = (
        f"{BASE_URL}/{search['operation']}"
        f"/{search['property_type']}"
        f"/{search['location']}"
    )

    if page > 0:
        url += f"/_Desde_{page * RESULTS_PER_PAGE + 1}"

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
    m2_utiles = None

    for text in texts:
        if "dormitorio" in text or "ambiente" in text.lower():
            bedrooms_text = text
        elif "baño" in text:
            bathrooms_text = text
        elif "m²" in text:
            m2_text = text

            # only single values ("170 m² útiles"), not ranges ("57 - 104")
            if "-" not in text and " a " not in text:
                m2_utiles = parse_int(text)

    return bedrooms_text, bathrooms_text, m2_text, m2_utiles


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

    bedrooms, bathrooms, m2_text, m2_utiles = parse_attributes(card)

    is_project = "DEVELOPMENT" in (metadata.get("domain_id") or "")

    return {
        "title": get_component(card, "title").get("text", "").strip(),
        "price": price_value,
        "currency": currency,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "m2": m2_text,
        "m2_utiles": m2_utiles,
        "location": get_component(card, "location").get("text"),
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
