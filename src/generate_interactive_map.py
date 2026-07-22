"""Interactive Leaflet map of recent listings, served via GitHub Pages."""
import json

import numpy as np
import pandas as pd

RAW_CSV = "data/raw/portalinmobiliario_listings.csv"
TEMPLATE_PATH = "src/map_template.html"
OUTPUT_HTML = "docs/map.html"

RECENT_DAYS = 7
RECENT_MAX_M2 = 100

# sequential blue ramp, steps 100 -> 700 (light -> dark)
SEQ_BLUE = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
    "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
    "#0d366b",
]

MAP_COLUMNS = [
    "title",
    "url",
    "lat",
    "lng",
    "price_uf",
    "price_clp",
    "m2_utiles",
    "uf_per_m2",
    "zona_uf_m2",
    "bedrooms_n",
    "parking",
    "gastos_comunes_clp",
    "barrio",
    "first_seen_date",
]


def comuna_display(slug):
    return slug.replace("-metropolitana", "").replace("-", " ").title()


def load_recent():
    # deferred import: pipeline imports this module at load time
    from src.pipeline import recent_mask

    df = pd.read_csv(RAW_CSV)

    return df[
        recent_mask(df)
        & df["lat"].notna()
        & df["uf_per_m2"].notna()
        & df["price_clp"].notna()
    ].copy()


def generate_interactive_map():
    recent = load_recent()

    if recent.empty:
        print("No recent listings with coordinates; skipping map.")
        return

    vmin, vmax = np.percentile(recent["uf_per_m2"], [5, 95])

    comunas = " y ".join(
        comuna_display(c) for c in sorted(recent["comuna"].dropna().unique())
    )

    config = {
        "colors": SEQ_BLUE,
        "vmin": round(vmin),
        "vmax": round(vmax),
        "recentDays": RECENT_DAYS,
        "maxM2": RECENT_MAX_M2,
        "updated": pd.Timestamp.today().strftime("%Y-%m-%d"),
    }

    # to_json turns NaN into null, which json.loads keeps as None
    listings = json.loads(recent[MAP_COLUMNS].to_json(orient="records"))

    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = f.read()

    html = (
        template
        .replace("__COMUNAS__", comunas)
        .replace("__CONFIG__", json.dumps(config))
        .replace("__LISTINGS__", json.dumps(listings, ensure_ascii=False))
    )

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Saved {len(recent)} listings to {OUTPUT_HTML}")


if __name__ == "__main__":
    generate_interactive_map()
