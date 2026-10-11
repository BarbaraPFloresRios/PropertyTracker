"""Rental-listings pipeline: scrape + enrich only.

No map, no recent set, no README -- those belong to the sale pipeline. Shares
only src/common.py with it, and writes its own CSV.
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

from scrapers.portalinmobiliario import (
    LISTING_FINISHED,
    SEARCHES_ARRIENDO,
    fetch_listing_details,
    scrape_portalinmobiliario,
)

ARRIENDO_OUTPUT_PATH = f"{RAW_DATA_DIR}/portalinmobiliario_rentals.csv"

# Medido el 2026-10-11: entran ~1.850 arriendos nuevos por semana (1.825 el
# 10-03, 1.882 el 10-10), asi que el tope anterior de 800 dejaba ~1.050 sin
# enriquecer CADA semana -- deficit estructural, no mala suerte. Se sube para
# cubrir la llegada real.
# OJO: el techo de verdad no es esta constante sino el portal, que estrangula
# (429) alrededor de las ~1.400 fichas seguidas. Un tope mas alto no corrompe
# nada -- un fetch estrangulado devuelve None, el aviso queda sin
# enriched_date y se reintenta al run siguiente -- pero tampoco garantiza que
# se enriquezcan todos en una sola pasada.
ENRICH_MAX_PER_RUN_ARRIENDO = 2000


def enrich_new_rentals():
    """Fetch parking/GC/coords for rental listings that don't have it yet.

    Unlike enrich_recent_listings, there's no map/recent-listings window to
    respect here -- just work through whatever hasn't been enriched, capped
    per run since this runs weekly (not twice daily) and can afford a bigger
    batch.
    """
    if not os.path.exists(ARRIENDO_OUTPUT_PATH):
        return

    listings = pd.read_csv(ARRIENDO_OUTPUT_PATH)

    for column in ENRICH_COLUMNS:
        if column not in listings.columns:
            listings[column] = pd.NA

    if "finished_date" not in listings.columns:
        listings["finished_date"] = pd.NA

    for column in (
        "orientacion",
        "enriched_date",
        "publicado_hace",
        "publicado_fecha_est",
        "finished_date",
    ):
        listings[column] = listings[column].astype("object")

    live = listings["delisted_date"].isna() & listings["finished_date"].isna()

    candidates = listings.index[
        live
        & listings["enriched_date"].isna()
        & listings["url"].notna()
    ]

    pending = len(candidates)
    candidates = candidates[:ENRICH_MAX_PER_RUN_ARRIENDO]

    print(f"Enriching {len(candidates)} of {pending} pending rental listings")

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    for count, index in enumerate(candidates, start=1):
        details = fetch_listing_details(listings.at[index, "url"])

        if details is None:
            continue

        if details is LISTING_FINISHED:
            listings.at[index, "finished_date"] = today
            listings.at[index, "enriched_date"] = today
            continue

        if all(details.get(column) is None for column in ENRICH_VALUE_COLUMNS):
            # stripped page (likely a blocked fetch) -- retry next run
            continue

        for column in ENRICH_VALUE_COLUMNS:
            listings.at[index, column] = details.get(column)

        listings.at[index, "enriched_date"] = today

        if count % 50 == 0:
            print(f"  {count}/{len(candidates)} enriched")

        time.sleep(ENRICH_SLEEP_SECONDS)

    listings.to_csv(ARRIENDO_OUTPUT_PATH, index=False)


def run_arriendo_pipeline():
    """Weekly rental-listings pipeline: scrape + enrich, no map/recent/README.

    Kept fully separate from run_pipeline() (venta) -- own CSV, own schedule,
    nothing here touches the venta files or the map.
    """
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    print_section("Portalinmobiliario (arriendo)")
    listings = scrape_portalinmobiliario(SEARCHES_ARRIENDO)

    # mismo criterio que en run_pipeline(): vacio = fuente bloqueada, no
    # "sin novedades". Aca no hay mapa que proteger, pero igual queremos
    # que el run falle en vez de pasar en silencio.
    if listings.empty:
        raise RuntimeError(
            "Scrape de arriendo vacio (0 listings): la fuente respondio sin "
            "contenido. Revisar si la IP del runner esta bloqueada."
        )

    print_phase("Processing results")

    save_listings(
        listings,
        ARRIENDO_OUTPUT_PATH,
        "Portalinmobiliario Arriendo",
    )

    print_phase("Enriching rental listings")

    enrich_new_rentals()

    print(f"\nArriendo pipeline done -> {ARRIENDO_OUTPUT_PATH}")
