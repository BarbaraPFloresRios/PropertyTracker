import os
import time

import pandas as pd

from src.generate_interactive_map import comuna_display, generate_interactive_map
from src.generate_readme import generate_readme

from scrapers.portalinmobiliario import (
    LISTING_FINISHED,
    fetch_listing_details,
    scrape_portalinmobiliario,
)

RAW_DATA_DIR = "data/raw"

PORTALINMOBILIARIO_OUTPUT_PATH = (
    f"{RAW_DATA_DIR}/portalinmobiliario_listings.csv"
)

RECENT_DAYS = 14
RECENT_MAX_M2 = 100

# exclude high-end listings above this CLP price from the recent set / map
RECENT_MAX_PRICE_CLP = 500_000_000

# runs a listing can miss (partial scrapes) before counting as delisted
DELIST_TOLERANCE_DAYS = 2

ENRICH_MAX_PER_RUN = 300
ENRICH_SLEEP_SECONDS = 0.5

ENRICH_VALUE_COLUMNS = [
    "parking",
    "bodegas",
    "gastos_comunes_clp",
    "antiguedad_anos",
    "m2_totales",
    "m2_terraza",
    "piso_unidad",
    "pisos_edificio",
    "deptos_por_piso",
    "orientacion",
    "lat",
    "lng",
    "zona_uf_m2",
    "publicado_hace",
    "publicado_fecha_est",
]
ENRICH_COLUMNS = ENRICH_VALUE_COLUMNS + ["enriched_date"]


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


def add_delisting_columns(listings, today):
    first_seen = pd.to_datetime(listings["first_seen_date"])
    last_seen = pd.to_datetime(listings["last_seen_date"])

    listings["days_published"] = (last_seen - first_seen).dt.days + 1

    # recomputed every run, so a listing that reappears is un-delisted
    gone = (pd.Timestamp(today) - last_seen).dt.days >= DELIST_TOLERANCE_DAYS

    listings["delisted_date"] = pd.Series(
        pd.NA, index=listings.index, dtype="object"
    )
    listings.loc[gone, "delisted_date"] = (
        last_seen[gone] + pd.Timedelta(days=1)
    ).dt.strftime("%Y-%m-%d")

    return listings


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

        # finished_date is sticky: once a detail page says "Publicación
        # finalizada", the flag persists across runs (unlike delisted_date,
        # which add_delisting_columns recomputes each run)
        if "finished_date" in old_indexed.columns:
            current_listings["finished_date"] = (
                current_listings[dedupe_key].map(old_indexed["finished_date"])
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

    listings = add_delisting_columns(listings, today)

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
        "zona_uf_m2",
        "bedrooms",
        "bedrooms_n",
        "bathrooms",
        "bathrooms_n",
        "m2",
        "m2_utiles",
        "seller",
        "tienda_oficial",
        "location",
        "barrio",
        "property_kind",
        "operation",
        "property_type",
        "comuna",
        "listing_id",
        "source",
        "publicado_hace",
        "publicado_fecha_est",
        "first_seen_date",
        "last_seen_date",
        "days_published",
        "delisted_date",
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
    today = pd.Timestamp.today()
    cutoff = (today - pd.Timedelta(days=RECENT_DAYS)).strftime("%Y-%m-%d")

    # each comuna's first scrape captures a mix of old and new listings all
    # with the same first_seen_date, so that bootstrap cohort is not "new"
    bootstrap_date = listings.groupby("comuna")["first_seen_date"].transform("min")

    seen_recently = (
        (listings["first_seen_date"] >= cutoff)
        & (listings["first_seen_date"] > bootstrap_date)
    )

    # "recent" means published within the last RECENT_DAYS, by the listing's
    # real publication date. The site reports exact days under a month, so the
    # boundary is precise. first_seen_date only says when WE saw it, which
    # can lag publication by months (listings rotate into the scrape window).
    if "publicado_fecha_est" in listings.columns:
        pub = pd.to_datetime(listings["publicado_fecha_est"], errors="coerce")
        published_recently = pub >= (today - pd.Timedelta(days=RECENT_DAYS))

        # provisional: a listing we just saw but haven't enriched yet has an
        # unknown publication date. Show it now; if enrichment (same run,
        # before the map is built) reveals it is old, it drops out.
        awaiting_enrichment = pub.isna() & seen_recently

        is_recent = published_recently | awaiting_enrichment
    else:
        is_recent = seen_recently

    # exclude listings we know are gone: flagged delisted by the seen/not-seen
    # heuristic, or confirmed "Publicación finalizada" on the detail page
    live = pd.Series(True, index=listings.index)

    if "delisted_date" in listings.columns:
        live &= listings["delisted_date"].isna()

    if "finished_date" in listings.columns:
        live &= listings["finished_date"].isna()

    # drop high-end listings; >= gives False for NaN, so listings without a
    # known price_clp (e.g. a failed UF fetch) are kept rather than dropped
    not_too_expensive = ~(listings["price_clp"] >= RECENT_MAX_PRICE_CLP)

    return (
        is_recent
        & live
        & (listings["m2_utiles"] < RECENT_MAX_M2)
        & not_too_expensive
    )


def enrich_recent_listings():
    """Fetch parking and common expenses for recent listings, with cache."""
    if not os.path.exists(PORTALINMOBILIARIO_OUTPUT_PATH):
        return

    listings = pd.read_csv(PORTALINMOBILIARIO_OUTPUT_PATH)

    for column in ENRICH_COLUMNS:
        if column not in listings.columns:
            listings[column] = pd.NA

    if "finished_date" not in listings.columns:
        listings["finished_date"] = pd.NA

    # text goes into these; an all-NaN column defaults to float
    for column in (
        "orientacion",
        "enriched_date",
        "publicado_hace",
        "publicado_fecha_est",
        "finished_date",
    ):
        listings[column] = listings[column].astype("object")

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

        if details is LISTING_FINISHED:
            # detail page says "Publicación finalizada": flag it gone now
            # instead of waiting DELIST_TOLERANCE_DAYS for the not-seen heuristic
            listings.at[index, "finished_date"] = today
            listings.at[index, "enriched_date"] = today
            continue

        for column in ENRICH_VALUE_COLUMNS:
            listings.at[index, column] = details.get(column)

        listings.at[index, "enriched_date"] = today

        if count % 50 == 0:
            print(f"  {count}/{len(candidates)} enriched")

        time.sleep(ENRICH_SLEEP_SECONDS)

    listings.to_csv(PORTALINMOBILIARIO_OUTPUT_PATH, index=False)


def verify_recent_listings():
    """Re-check recent listings already enriched in a prior run.

    Enrichment only visits a listing once, so one that dies after we enriched
    it keeps showing until the seen/not-seen heuristic catches it. Here we
    re-fetch the currently-shown recent set and flag any whose detail page now
    reads "Publicación finalizada".
    """
    if not os.path.exists(PORTALINMOBILIARIO_OUTPUT_PATH):
        return

    listings = pd.read_csv(PORTALINMOBILIARIO_OUTPUT_PATH)

    if "finished_date" not in listings.columns:
        listings["finished_date"] = pd.NA
    listings["finished_date"] = listings["finished_date"].astype("object")

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    # recent_mask already excludes finished ones; skip those enriched this run
    # (enrich_recent_listings just checked them)
    candidates = listings.index[
        recent_mask(listings)
        & listings["enriched_date"].notna()
        & (listings["enriched_date"] != today)
        & listings["url"].notna()
    ]

    print(f"Re-checking {len(candidates)} recent listings for 'finalizada'")

    gone = 0

    for count, index in enumerate(candidates, start=1):
        result = fetch_listing_details(listings.at[index, "url"])

        if result is LISTING_FINISHED:
            listings.at[index, "finished_date"] = today
            gone += 1

        if count % 50 == 0:
            print(f"  {count}/{len(candidates)} re-checked")

        time.sleep(ENRICH_SLEEP_SECONDS)

    print(f"Flagged {gone} newly finished listings")

    listings.to_csv(PORTALINMOBILIARIO_OUTPUT_PATH, index=False)


def build_recent_listings():
    if not os.path.exists(PORTALINMOBILIARIO_OUTPUT_PATH):
        return pd.DataFrame()

    listings = pd.read_csv(PORTALINMOBILIARIO_OUTPUT_PATH)

    recent = listings[recent_mask(listings)].copy()

    recent["comuna"] = recent["comuna"].map(comuna_display)

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
        "zona_uf_m2",
        "bedrooms_n",
        "parking",
        "gastos_comunes_clp",
        "comuna",
        "barrio",
        "first_seen_date",
        "publicado_fecha_est",
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

    print_phase("Re-checking recent listings")

    verify_recent_listings()

    print_phase("Exporting recent listings")

    recent_listings = build_recent_listings()

    # safety net: never overwrite a healthy map with a collapsed one. A silent
    # upstream failure (e.g. the UF conversion dropping every UF-priced listing)
    # halves the recent set; abort so the previous good map/data stay published.
    recent_path = "data/recent_listings.csv"
    if os.path.exists(recent_path):
        previous_count = len(pd.read_csv(recent_path))
        if previous_count > 0 and len(recent_listings) < 0.5 * previous_count:
            raise RuntimeError(
                f"Recent set collapsed from {previous_count} to "
                f"{len(recent_listings)}; aborting to avoid publishing a "
                "broken map. Re-run once the upstream source recovers."
            )

    recent_listings.to_csv(recent_path, index=False)

    print(
        f"Saved {len(recent_listings)} recent listings "
        f"to {recent_path}"
    )

    print_phase("Updating interactive map")

    generate_interactive_map()

    print_phase("Updating README")

    generate_readme()
    print("Updated README.md")
