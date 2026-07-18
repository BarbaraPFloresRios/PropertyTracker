"""Static PNG map of recent listings, colored by UF/m² (sequential blue ramp)."""
import io
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable
from PIL import Image, ImageEnhance

RAW_CSV = "data/raw/portalinmobiliario_listings.csv"
OUTPUT_PNG = "data/recent_listings_map.png"

RECENT_DAYS = 7
RECENT_MAX_M2 = 100

# sequential blue ramp, steps 100 -> 700 (light -> dark)
SEQ_BLUE = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
    "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
    "#0d366b",
]

SURFACE = "#fcfcfb"
PRIMARY_INK = "#0b0b0b"
SECONDARY_INK = "#52514e"
MUTED = "#898781"

TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
TILE_SIZE = 256
ZOOM = 15
HEADERS = {"User-Agent": "PropertyTracker/1.0 (personal project map render)"}


def lonlat_to_mercator(lon, lat):
    x = lon * 20037508.34 / 180
    y = np.log(np.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    return x, y * 20037508.34 / 180


def lonlat_to_tile(lon, lat, z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y


def tile_to_mercator(x, y, z):
    n = 2 ** z
    lon = x / n * 360 - 180
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lonlat_to_mercator(lon, lat)


def fetch_basemap(lon_min, lon_max, lat_min, lat_max):
    x0, y1 = lonlat_to_tile(lon_min, lat_min, ZOOM)
    x1, y0 = lonlat_to_tile(lon_max, lat_max, ZOOM)

    tx0, tx1 = int(x0), int(x1)
    ty0, ty1 = int(y0), int(y1)

    width = (tx1 - tx0 + 1) * TILE_SIZE
    height = (ty1 - ty0 + 1) * TILE_SIZE
    mosaic = Image.new("RGB", (width, height))

    for tx in range(tx0, tx1 + 1):
        for ty in range(ty0, ty1 + 1):
            url = TILE_URL.format(z=ZOOM, x=tx, y=ty)
            response = requests.get(url, headers=HEADERS, timeout=30)
            response.raise_for_status()
            tile = Image.open(io.BytesIO(response.content)).convert("RGB")
            mosaic.paste(tile, ((tx - tx0) * TILE_SIZE, (ty - ty0) * TILE_SIZE))

    # desaturate + lighten so the basemap recedes behind the blue ramp
    mosaic = ImageEnhance.Color(mosaic).enhance(0.0)
    mosaic = ImageEnhance.Brightness(mosaic).enhance(1.15)

    left, top = tile_to_mercator(tx0, ty0, ZOOM)
    right, bottom = tile_to_mercator(tx1 + 1, ty1 + 1, ZOOM)

    return mosaic, (left, right, bottom, top)


def load_recent():
    df = pd.read_csv(RAW_CSV)
    cutoff = (
        pd.Timestamp.today() - pd.Timedelta(days=RECENT_DAYS)
    ).strftime("%Y-%m-%d")

    recent = df[
        (df["first_seen_date"] >= cutoff)
        & (df["m2_utiles"] < RECENT_MAX_M2)
        & df["lat"].notna()
        & df["uf_per_m2"].notna()
    ].copy()

    return recent


def main():
    recent = load_recent()
    print(f"{len(recent)} recent listings with coordinates")

    pad = 0.004
    lon_min, lon_max = recent["lng"].min() - pad, recent["lng"].max() + pad
    lat_min, lat_max = recent["lat"].min() - pad, recent["lat"].max() + pad

    basemap, extent = fetch_basemap(lon_min, lon_max, lat_min, lat_max)

    x, y = lonlat_to_mercator(recent["lng"].values, recent["lat"].values)
    values = recent["uf_per_m2"].values

    vmin, vmax = np.percentile(values, [5, 95])

    cmap = LinearSegmentedColormap.from_list("seq_blue", SEQ_BLUE)
    norm = Normalize(vmin=vmin, vmax=vmax, clip=True)

    fig, ax = plt.subplots(figsize=(11, 11), dpi=150)
    fig.patch.set_facecolor(SURFACE)

    ax.imshow(basemap, extent=extent, interpolation="lanczos")

    ax.scatter(
        x, y,
        c=values,
        cmap=cmap,
        norm=norm,
        s=55,
        edgecolors=SURFACE,
        linewidths=1.2,
        zorder=3,
    )

    xmin, _ = lonlat_to_mercator(lon_min, lat_min)
    xmax, _ = lonlat_to_mercator(lon_max, lat_min)
    _, ymin = lonlat_to_mercator(lon_min, lat_min)
    _, ymax = lonlat_to_mercator(lon_min, lat_max)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.set_axis_off()
    ax.set_aspect("equal")

    today = pd.Timestamp.today().strftime("%Y-%m-%d")
    ax.set_title(
        "Avisos recientes en Providencia — UF/m²",
        color=PRIMARY_INK,
        fontsize=15,
        pad=14,
        loc="left",
    )
    ax.text(
        0, 1.005,
        f"{len(recent)} departamentos <100 m² vistos por primera vez en los "
        f"últimos {RECENT_DAYS} días · {today}",
        transform=ax.transAxes,
        color=SECONDARY_INK,
        fontsize=9.5,
    )

    cbar = fig.colorbar(
        ScalarMappable(norm=norm, cmap=cmap),
        ax=ax,
        shrink=0.55,
        pad=0.02,
        aspect=30,
    )
    cbar.set_label("UF/m²", color=SECONDARY_INK, fontsize=10)
    cbar.ax.tick_params(colors=MUTED, labelsize=9)
    cbar.outline.set_visible(False)

    ax.text(
        0.995, 0.005,
        "© OpenStreetMap contributors",
        transform=ax.transAxes,
        ha="right",
        color=MUTED,
        fontsize=7,
    )

    fig.savefig(
        OUTPUT_PNG,
        bbox_inches="tight",
        facecolor=SURFACE,
    )
    print(f"Saved {OUTPUT_PNG}")


if __name__ == "__main__":
    main()
