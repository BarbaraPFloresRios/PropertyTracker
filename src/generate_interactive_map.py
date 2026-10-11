"""Interactive Leaflet map of recent listings, served via GitHub Pages.

Two markets on one map, switched with a toggle: sales (blue, UF/m²) and
rentals (orange, CLP/m² per month). Each keeps its own sequential ramp and its
own filter ranges instead of sharing one, because the two metrics differ by
orders of magnitude and comparing lightness across hues is unreliable -- so
only one market is drawn at a time.
"""
import json

import numpy as np
import pandas as pd

VENTA_CSV = "data/raw/portalinmobiliario_listings.csv"
ARRIENDO_CSV = "data/raw/portalinmobiliario_rentals.csv"
TEMPLATE_PATH = "src/map_template.html"
OUTPUT_HTML = "docs/map.html"

# The map's own window, deliberately wider than the pipeline's RECENT_DAYS
# (14), which governs the curated recent_listings.csv export. The map answers
# "what does the market hold right now", the export answers "what came on
# lately" -- and the rental layer already shows the whole live market, so a
# fortnight-wide sale layer made the two halves of the same map inconsistent.
# Only the view widens: nothing changes in what gets stored or exported.
MAP_DAYS = 90

# The map drops the export's size and price ceilings (150 m2 / $500M): those
# came from one buyer's criteria and the map is about the market. What it adds
# instead is a floor, because the tail that actually distorts the view is bad
# data, not luxury. An "edificio Uso Mixto" parsed as 1 m2 shows up at 240,000
# UF/m2 and stretches the price slider to $9,873M; a genuine 547 m2 flat in Las
# Condes sits at a perfectly ordinary 123 UF/m2. With the floor, the worst
# values become $2,777M and 608 UF/m2, and the colour ramp barely moves
# (p5-p95 goes 42-134 -> 42-137) because it is percentile-based anyway.
MAP_MIN_M2 = 15

RECENT_MAX_M2 = 150

# continental Chile bounding box, to drop listings with a corrupt geocode
# (e.g. a Providencia flat whose lat/lng resolve to Florida). The listing
# stays in the dataset; it just isn't plotted at the wrong place.
CHILE_LAT_MIN, CHILE_LAT_MAX = -56.0, -17.3
CHILE_LNG_MIN, CHILE_LNG_MAX = -76.0, -66.0

# Sanity bounds for the rental layer. Sale listings leak into the rental
# search -- titles like "Depto Venta 3d+3b" priced at UF 8,900, which converts
# to "$366,000,000 per month" -- and a handful of listings carry a typo'd
# surface (a 1-bedroom flat recorded as 1 m²). Both wreck the sliders and the
# ramp. A currency rule would be wrong here: 889 genuine rentals are quoted in
# UF. These cut 17 and 29 rows respectively out of ~4,100 (p99.5 of monthly
# rent is $4.2M, so the ceiling clears every plausible listing).
ARRIENDO_MAX_CLP = 6_000_000
ARRIENDO_MIN_M2 = MAP_MIN_M2

# Sequential ramps, light -> dark. Blue for sales, purple for rentals: the hue
# says which market you're looking at, the lightness says the value. Purple
# over orange because orange muddies against the grey base map, and over green
# because green and blue collide in the mid tones.
SEQ_BLUE = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
    "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
    "#0d366b",
]
SEQ_PURPLE = [
    "#e9ddf6", "#ddcbf1", "#d0b8ec", "#c2a4e6", "#b390e0", "#a37bd8",
    "#9366cf", "#8352c4", "#7342b2", "#63369c", "#542d85", "#45246e",
    "#371c58",
]

BASE_COLUMNS = [
    "title",
    "publicado_fecha_est",
    "url",
    "lat",
    "lng",
    "price_clp",
    "m2_utiles",
    "bedrooms_n",
    "parking",
    "gastos_comunes_clp",
    "barrio",
    "first_seen_date",
]
VENTA_COLUMNS = BASE_COLUMNS + ["price_uf", "uf_per_m2"]
ARRIENDO_COLUMNS = BASE_COLUMNS + ["clp_m2"]


def comuna_display(slug):
    return slug.replace("-metropolitana", "").replace("-", " ").title()


# A listing further than this from the median of its own dataset is treated as
# a geocoding error. The Chile bounding box above is too coarse to catch these:
# two sale listings sat 46 and 77 km out while the 99.9th percentile of real
# distances was 22.6 km, and fitBounds then zoomed out so far that the actual
# city became a dot. Derived from the data's own centre rather than a hardcoded
# city box, so adding a comuna somewhere else still works.
MAX_KM_FROM_CENTER = 30


def in_chile(df):
    return (
        df["lat"].between(CHILE_LAT_MIN, CHILE_LAT_MAX)
        & df["lng"].between(CHILE_LNG_MIN, CHILE_LNG_MAX)
    )


def drop_far_outliers(df, label):
    """Drop points absurdly far from the dataset's own centre."""
    if df.empty:
        return df

    center_lat, center_lng = df["lat"].median(), df["lng"].median()

    km = np.sqrt(
        ((df["lat"] - center_lat) * 111.32) ** 2
        + ((df["lng"] - center_lng) * 111.32
           * np.cos(np.radians(center_lat))) ** 2
    )

    keep = km <= MAX_KM_FROM_CENTER

    if (~keep).any():
        print(
            f"  {label}: dropped {(~keep).sum()} listing(s) over "
            f"{MAX_KM_FROM_CENTER} km from the centre (bad geocode)"
        )

    return df[keep].copy()


def load_recent():
    """Sale listings: the published recent set, same filter as the CSV export."""
    # deferred import: pipeline_venta imports this module at load time
    from src.pipeline_venta import recent_mask

    df = pd.read_csv(VENTA_CSV, low_memory=False)

    df = df[
        recent_mask(df, days=MAP_DAYS, max_m2=None, max_price_clp=None)
        & (df["m2_utiles"] >= MAP_MIN_M2)
        & df["lat"].notna()
        & df["uf_per_m2"].notna()
        & df["price_clp"].notna()
        & in_chile(df)
    ].copy()

    return drop_far_outliers(df, "venta")


def load_arriendos():
    """Rental listings: the whole live market, not a recency window.

    Deliberately different from the sale side. Rentals turn over fast and only
    ~68% of them expose a publication date at all, so a 14-day window would
    silently drop a third of the market for no gain -- what's useful here is
    what's currently available. The m² cap is kept so both markets cover
    comparable apartments.
    """
    df = pd.read_csv(ARRIENDO_CSV, low_memory=False)

    live = df["delisted_date"].isna() & df["finished_date"].isna()

    df = df[
        live
        & df["lat"].notna()
        & df["price_clp"].notna()
        & df["m2_utiles"].notna()
        & (df["m2_utiles"] >= ARRIENDO_MIN_M2)
        & (df["m2_utiles"] < RECENT_MAX_M2)
        & (df["price_clp"] <= ARRIENDO_MAX_CLP)
        & in_chile(df)
    ].copy()

    df["clp_m2"] = (df["price_clp"] / df["m2_utiles"]).round()

    return drop_far_outliers(df, "arriendo")


def market_payload(df, columns, metric, colors):
    """Build one market's config + rows, with the ramp scaled to its own data."""
    vmin, vmax = np.percentile(df[metric], [5, 95])

    return {
        "colors": colors,
        "vmin": round(float(vmin)),
        "vmax": round(float(vmax)),
        "metric": metric,
        # to_json turns NaN into null, which json.loads keeps as None
        "listings": json.loads(df[columns].to_json(orient="records")),
    }


def generate_interactive_map():
    venta = load_recent()

    if venta.empty:
        print("No recent listings with coordinates; skipping map.")
        return

    arriendo = load_arriendos()

    comunas = " y ".join(
        comuna_display(c) for c in sorted(venta["comuna"].dropna().unique())
    )

    config = {
        "updated": pd.Timestamp.today().strftime("%Y-%m-%d"),
        "recentDays": MAP_DAYS,
        "maxM2": RECENT_MAX_M2,
        "markets": {
            "venta": market_payload(
                venta, VENTA_COLUMNS, "uf_per_m2", SEQ_BLUE
            ),
            "arriendo": market_payload(
                arriendo, ARRIENDO_COLUMNS, "clp_m2", SEQ_PURPLE
            ) if not arriendo.empty else None,
        },
    }

    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = f.read()

    html = (
        template
        .replace("__COMUNAS__", comunas)
        .replace("__CONFIG__", json.dumps(config, ensure_ascii=False))
    )

    with open(OUTPUT_HTML, encoding="utf-8", mode="w") as f:
        f.write(html)

    print(
        f"Saved {len(venta)} sale and {len(arriendo)} rental listings "
        f"to {OUTPUT_HTML}"
    )


if __name__ == "__main__":
    generate_interactive_map()
