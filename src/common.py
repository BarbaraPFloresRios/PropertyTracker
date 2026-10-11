"""Shared pipeline machinery used by both the sale and the rental pipelines.

Nothing here knows about a specific operation: it merges a fresh scrape into
the stored dataset, reports what changed and writes the CSV back out.
"""
import os

import pandas as pd


RAW_DATA_DIR = "data/raw"

# runs a listing can miss (partial scrapes) before counting as delisted
DELIST_TOLERANCE_DAYS = 2

ENRICH_SLEEP_SECONDS = 0.5

# Below this, a surface figure is treated as a data error rather than a very
# small flat. Sellers mistype it on the portal -- "1 m2" on a 3-bedroom, "3 m2"
# on a whole flat -- and the portal publishes whatever they typed.
MIN_PLAUSIBLE_M2 = 15

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


def sanitize_surfaces(listings):
    """Repair or drop implausible m2_utiles values, in place.

    A wrong surface is louder than a missing one: it divides the price, so a
    flat priced at 9.000 UF with "1 m2" lands at 9.000 UF/m2 and outranks
    every real listing in anything sorted by that metric. The README table is
    sorted by UF/m2 descending, so these used to be its first rows.

    This cannot live in the scraper. Enrichment only visits listings that are
    still pending, so a bad value written once is never looked at again -- and
    re-fetching these pages now returns m2_utiles=None, meaning the stored
    number no longer exists at the source. Running it on every save is what
    repairs the rows already on disk.

    Where m2_totales is plausible it stands in for the missing m2_utiles. It
    includes terrace and balcony, so the resulting UF/m2 runs low -- measured
    against the listings that report both, the median inflation is 7% and the
    75th percentile 15%. That was judged a better trade than discarding the
    listing. Where both figures are broken, the surface and every metric
    derived from it are cleared: no number beats a wrong one.
    """
    if "m2_utiles" not in listings.columns:
        return listings

    utiles = pd.to_numeric(listings["m2_utiles"], errors="coerce")
    broken = (utiles > 0) & (utiles < MIN_PLAUSIBLE_M2)
    if not broken.any():
        return listings

    totales = (
        pd.to_numeric(listings["m2_totales"], errors="coerce")
        if "m2_totales" in listings.columns
        else pd.Series(pd.NA, index=listings.index, dtype="float64")
    )
    rescued = broken & (totales >= MIN_PLAUSIBLE_M2)
    cleared = broken & ~rescued

    listings.loc[rescued, "m2_utiles"] = totales[rescued]
    listings.loc[cleared, "m2_utiles"] = pd.NA

    # uf_per_m2 is computed at scrape time, so the stored value still carries
    # the old surface; recompute it for every row touched here.
    if "uf_per_m2" in listings.columns and "price_uf" in listings.columns:
        touched = broken
        listings.loc[touched, "uf_per_m2"] = (
            pd.to_numeric(listings.loc[touched, "price_uf"], errors="coerce")
            / pd.to_numeric(listings.loc[touched, "m2_utiles"], errors="coerce")
        ).round(2)

    print(
        f"Surfaces under {MIN_PLAUSIBLE_M2} m2: "
        f"{int(rescued.sum())} replaced with m2_totales, "
        f"{int(cleared.sum())} cleared"
    )

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

    listings = sanitize_surfaces(listings)

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
