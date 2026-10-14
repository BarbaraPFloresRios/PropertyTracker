"""Sale-listings pipeline: scrape, enrich, re-check, then publish map + README.

Kept separate from the rental pipeline on purpose -- own CSV, own schedule,
own outputs. The two only share src/common.py.
"""
import os
import time

import pandas as pd

from src.common import (
    ENRICH_COLUMNS,
    ENRICH_SLEEP_SECONDS,
    ENRICH_VALUE_COLUMNS,
    RAW_DATA_DIR,
    print_phase,
    print_section,
    save_listings,
)
from src.generate_interactive_map import comuna_display, generate_interactive_map
from src.generate_readme import generate_readme

from scrapers.portalinmobiliario import (
    LISTING_FINISHED,
    fetch_listing_details,
    scrape_portalinmobiliario,
)

PORTALINMOBILIARIO_OUTPUT_PATH = (
    f"{RAW_DATA_DIR}/portalinmobiliario_listings.csv"
)

# One definition of "recent" for everything this repo publishes: the export
# (data/recent_listings.csv), the README table and the map all read it.
RECENT_DAYS = 90

# No size or price ceiling. These used to be 150 m2 and $500M CLP, which were
# not a description of the market -- they were one buyer's purchase criteria,
# the same personal layer that came out of this repo along with the ranking.
# recent_mask still takes both, so a caller that genuinely wants a bounded
# slice can pass one without the filter logic being duplicated.
RECENT_MAX_M2 = None
RECENT_MAX_PRICE_CLP = None

# The 'finalizada' re-check keeps its OWN, narrower window, because unlike the
# others it costs one request per listing and is not capped: following
# RECENT_DAYS would take a run from ~2,030 re-checks to ~5,886.
#
# What the source actually does, measured on the 2026-10-11 run: sequential
# fetches at 1.5s draw a steady ~2% of 429s (32 in 1,753 re-checks), spread
# evenly from the ~565th request of the run to the last, with no ramp. That is
# a rate, not a daily quota -- a quota would show nothing and then a wall --
# and the run finished every re-check regardless. The real wall is
# concurrency: four parallel workers ran clean to ~1,360 fetches and then took
# 420 consecutive 403s, which lifted on its own in ~5 minutes.
#
# So tripling the re-check count would not hit a cliff, it would just triple a
# ~40-minute run that already has to finish inside one evening. Listings
# outside this window still lose their delisted_date through the not-seen
# heuristic, just a few days later.
VERIFY_DAYS = 14

# 300 stopped being enough when the map widened the window: the pending queue
# went 448 -> 536 -> 557 over three runs on 11-12 Oct 2026, so each run cleared
# 300 while more than 300 arrived, and the overflow stays without coordinates,
# invisible to both the map and the ranking. At 0.5s a fetch, doubling the cap
# costs about five minutes a run and eats the backlog in two or three nights.
ENRICH_MAX_PER_RUN = 600


def recent_mask(
    listings,
    days=RECENT_DAYS,
    max_m2=RECENT_MAX_M2,
    max_price_clp=RECENT_MAX_PRICE_CLP,
):
    """Listings that are live and recent enough to publish.

    The bounds are arguments rather than hardcoded constants because the two
    consumers want different things. The curated export (recent_listings.csv,
    README) keeps the narrow defaults. The map passes its own wider window and
    switches the size/price ceilings off: those two came from one buyer's
    criteria, and the map is meant to show the market. Pass None to drop a
    ceiling.
    """
    today = pd.Timestamp.today()
    cutoff = (today - pd.Timedelta(days=days)).strftime("%Y-%m-%d")

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
        published_recently = pub >= (today - pd.Timedelta(days=days))

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
    mask = is_recent & live

    if max_price_clp is not None:
        mask &= ~(listings["price_clp"] >= max_price_clp)

    if max_m2 is not None:
        mask &= listings["m2_utiles"] < max_m2

    return mask


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

        if all(details.get(column) is None for column in ENRICH_VALUE_COLUMNS):
            # every field empty means the detail page came back stripped
            # (seen when the source blocks the request's IP) rather than a
            # listing that genuinely has none of these fields. Leave
            # enriched_date unset so it's retried next run instead of
            # permanently stuck with no coordinates/attributes.
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
        recent_mask(listings, days=VERIFY_DAYS)
        & listings["enriched_date"].notna()
        & (listings["enriched_date"] != today)
        & listings["url"].notna()
    ]

    print(
        f"Re-checking {len(candidates)} listings published in the last "
        f"{VERIFY_DAYS} days for 'finalizada'"
    )

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

    # zona_uf_m2 is deliberately NOT exported: it's the site's own "Promedio en
    # la zona" widget, not a valuation. It skews high -- for 66% of active
    # listings it sits ABOVE the asking price of that same listing (median gap
    # +10.6%), and of 1,839 buildings with 3+ listings at identical
    # coordinates, 66% carry more than one value (up to 92 UF/m2 apart within
    # the SAME building). A figure that varies per listing doesn't describe the
    # area. Still stored in the raw CSV, just never shown in any output.
    columns = [
        "title",
        "price_uf",
        "price_clp",
        "m2_utiles",
        "uf_per_m2",
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

    # An empty scrape is not "no new listings": it's the source answering
    # HTTP 200 with no content, which is what a datacenter-IP block looks like
    # here (seen from GitHub's hosted runners since 2026-09-29). Carrying on
    # would rebuild recent_listings/map/README from a frozen dataset and, since
    # the RECENT_DAYS window keeps moving, PUBLISH A MAP THAT EMPTIES ITSELF
    # while the badge stays green. Aborting leaves the last good map published
    # and turns the run red, which is the signal we want.
    if listings.empty:
        raise RuntimeError(
            "Empty scrape (0 listings): the source answered with no content. "
            "Skipping the recent_listings/map/README rebuild so stale data "
            "isn't published. Check whether the runner's IP is blocked."
        )

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
