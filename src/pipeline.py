import os
import time

import pandas as pd

from scrapers.portalinmobiliario import (
    fetch_listing_details,
    scrape_portalinmobiliario,
)

RAW_DATA_DIR = "data/raw"

PORTALINMOBILIARIO_OUTPUT_PATH = (
    f"{RAW_DATA_DIR}/portalinmobiliario_listings.csv"
)

RECENT_DAYS = 7
RECENT_MAX_M2 = 100

ENRICH_MAX_PER_RUN = 300
ENRICH_SLEEP_SECONDS = 0.5

ENRICH_COLUMNS = ["parking", "gastos_comunes_clp", "enriched_date"]


def normalize_key(series):
    return (
        series
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )


def print_section(title):
    width = 80
    print(f"\n{'═' * width}")
    print(f"SCRAPING {title.upper()}")
    print(f"{'═' * width}")


def print_phase(title):
    width = 80
    print(f"\n{'#' * width}")
    print(f"  {title.upper()}")
    print(f"{'#' * width}")


def report_price_changes(current_listings, old_listings, dedupe_key):
    old_prices = (
        old_listings
        .drop_duplicates(subset=[dedupe_key], keep="last")
        .set_index(dedupe_key)["price"]
    )

    merged = current_listings.copy()
    merged["old_price"] = merged[dedupe_key].map(old_prices)

    changed = merged[
        merged["old_price"].notna()
        & merged["price"].notna()
        & (merged["price"] != merged["old_price"])
    ]

    if changed.empty:
        return

    print(f"\nPrice changes ({len(changed)}):")

    for _, listing in changed.iterrows():
        direction = "↓" if listing["price"] < listing["old_price"] else "↑"

        print(
            f"\n- {listing.get('title', 'No title')} {direction} "
            f"{listing['old_price']:,.0f} → {listing['price']:,.0f} "
            f"{listing.get('currency', '')}"
        )

        if listing.get("url"):
            print(f"  {listing['url']}")


def save_listings(current_listings, output_path, source=""):

    width = 80
    print(f"\n{'═' * width}")
    print(f"RESULTS {source.upper()}")
    print(f"{'═' * width}")

    if current_listings.empty:
        print(f"{source}: no listings found; skipping.")
        return pd.DataFrame()

    dedupe_key = "listing_id"

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    current_listings = current_listings.copy()
    current_listings[dedupe_key] = normalize_key(current_listings[dedupe_key])
    current_listings["last_seen_date"] = today

    if os.path.exists(output_path):
        old_listings = pd.read_csv(output_path)
        old_listings[dedupe_key] = normalize_key(old_listings[dedupe_key])

        if "first_seen_date" not in old_listings.columns:
            old_listings["first_seen_date"] = today

        if "first_seen_price" not in old_listings.columns:
            old_listings["first_seen_price"] = old_listings.get("price")

        old_keys = old_listings[dedupe_key]

        new_listings = current_listings[
            ~current_listings[dedupe_key].isin(old_keys)
        ].copy()

        report_price_changes(current_listings, old_listings, dedupe_key)

        old_listings = old_listings.drop_duplicates(
            subset=[dedupe_key],
            keep="last",
        )

        old_indexed = old_listings.set_index(dedupe_key)

        current_listings["first_seen_date"] = (
            current_listings[dedupe_key]
            .map(old_indexed["first_seen_date"])
            .fillna(today)
        )

        current_listings["first_seen_price"] = (
            current_listings[dedupe_key]
            .map(old_indexed["first_seen_price"])
            .fillna(current_listings["price"])
        )

        # keep detail-page data already fetched for known listings
        for column in ENRICH_COLUMNS:
            if column in old_indexed.columns:
                current_listings[column] = (
                    current_listings[dedupe_key].map(old_indexed[column])
                )

        listings = pd.concat(
            [old_listings, current_listings],
            ignore_index=True,
        )

        listings = listings.drop_duplicates(
            subset=[dedupe_key],
            keep="last",
        )

    else:
        current_listings["first_seen_date"] = today
        current_listings["first_seen_price"] = current_listings["price"]
        new_listings = current_listings
        listings = current_listings

    listings = listings.sort_values(
        by=["first_seen_date", "uf_per_m2"],
        ascending=[False, True],
        na_position="last",
    )

    preferred_order = [
        "title",
        "price",
        "currency",
        "price_uf",
        "price_clp",
        "first_seen_price",
        "uf_per_m2",
        "bedrooms",
        "bathrooms",
        "m2",
        "m2_utiles",
        "location",
        "property_kind",
        "operation",
        "property_type",
        "comuna",
        "listing_id",
        "source",
        "first_seen_date",
        "last_seen_date",
        "url",
    ]

    existing_cols = [c for c in preferred_order if c in listings.columns]
    remaining_cols = [c for c in listings.columns if c not in preferred_order]

    listings = listings[existing_cols + remaining_cols]

    listings.to_csv(output_path, index=False)

    print(f"\nFound {len(current_listings)} current listings")
    print(f"Found {len(new_listings)} truly new listings")

    if len(new_listings) > 0:
        print("\nNew listings:")

        for _, listing in new_listings.iterrows():
            title = listing.get("title", "No title")
            price = listing.get("price")
            currency = listing.get("currency", "")
            url = listing.get("url", "")

            price_text = (
                f" — {price:,.0f} {currency}" if pd.notna(price) else ""
            )

            print(f"\n- {title}{price_text}")

            if url:
                print(f"  {url}")

    print(f"\nSaved {len(listings)} total listings to {output_path}")

    return new_listings


def recent_mask(listings):
    cutoff = (
        pd.Timestamp.today() - pd.Timedelta(days=RECENT_DAYS)
    ).strftime("%Y-%m-%d")

    return (
        (listings["first_seen_date"] >= cutoff)
        & (listings["m2_utiles"] < RECENT_MAX_M2)
    )


def enrich_recent_listings():
    """Fetch parking and common expenses for recent listings, with cache."""
    if not os.path.exists(PORTALINMOBILIARIO_OUTPUT_PATH):
        return

    listings = pd.read_csv(PORTALINMOBILIARIO_OUTPUT_PATH)

    for column in ENRICH_COLUMNS:
        if column not in listings.columns:
            listings[column] = pd.NA

    candidates = listings.index[
        recent_mask(listings)
        & listings["enriched_date"].isna()
        & listings["url"].notna()
    ]

    pending = len(candidates)
    candidates = candidates[:ENRICH_MAX_PER_RUN]

    print(f"Enriching {len(candidates)} of {pending} pending listings")

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    for count, index in enumerate(candidates, start=1):
        details = fetch_listing_details(listings.at[index, "url"])

        if details is None:
            continue

        listings.at[index, "parking"] = details.get("parking")
        listings.at[index, "gastos_comunes_clp"] = (
            details.get("gastos_comunes_clp")
        )
        listings.at[index, "enriched_date"] = today

        if count % 50 == 0:
            print(f"  {count}/{len(candidates)} enriched")

        time.sleep(ENRICH_SLEEP_SECONDS)

    listings.to_csv(PORTALINMOBILIARIO_OUTPUT_PATH, index=False)


def build_recent_listings():
    if not os.path.exists(PORTALINMOBILIARIO_OUTPUT_PATH):
        return pd.DataFrame()

    listings = pd.read_csv(PORTALINMOBILIARIO_OUTPUT_PATH)

    recent = listings[recent_mask(listings)].copy()

    recent = recent.sort_values(
        by="uf_per_m2",
        ascending=True,
        na_position="last",
    )

    columns = [
        "title",
        "price_uf",
        "price_clp",
        "m2_utiles",
        "uf_per_m2",
        "bedrooms_n",
        "parking",
        "gastos_comunes_clp",
        "first_seen_date",
        "url",
    ]

    return recent[[c for c in columns if c in recent.columns]]


def run_pipeline():

    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    print_section("Portalinmobiliario")
    listings = scrape_portalinmobiliario()

    print_phase("Processing results")

    save_listings(
        listings,
        PORTALINMOBILIARIO_OUTPUT_PATH,
        "Portalinmobiliario",
    )

    print_phase("Enriching recent listings")

    enrich_recent_listings()

    print_phase("Exporting recent listings")

    recent_listings = build_recent_listings()
    recent_listings.to_csv("data/recent_listings.csv", index=False)

    print(
        f"Saved {len(recent_listings)} recent listings "
        "to data/recent_listings.csv"
    )
