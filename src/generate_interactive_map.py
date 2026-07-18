"""Interactive Leaflet map of recent listings, served via GitHub Pages."""
import branca.colormap
import folium
import numpy as np
import pandas as pd

RAW_CSV = "data/raw/portalinmobiliario_listings.csv"
OUTPUT_HTML = "docs/map.html"

RECENT_DAYS = 7
RECENT_MAX_M2 = 100

# sequential blue ramp, steps 100 -> 700 (light -> dark)
SEQ_BLUE = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
    "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281",
    "#0d366b",
]


def load_recent():
    df = pd.read_csv(RAW_CSV)

    cutoff = (
        pd.Timestamp.today() - pd.Timedelta(days=RECENT_DAYS)
    ).strftime("%Y-%m-%d")

    return df[
        (df["first_seen_date"] >= cutoff)
        & (df["m2_utiles"] < RECENT_MAX_M2)
        & df["lat"].notna()
        & df["uf_per_m2"].notna()
    ].copy()


def format_popup(listing):
    def number(value, suffix="", prefix="", decimals=0):
        if pd.isna(value):
            return None
        return f"{prefix}{value:,.{decimals}f}{suffix}"

    rows = [
        ("Precio", number(listing["price_uf"], suffix=" UF")),
        ("", number(listing["price_clp"], prefix="$")),
        ("Superficie", number(listing["m2_utiles"], suffix=" m²")),
        ("UF/m²", number(listing["uf_per_m2"], decimals=1)),
        ("Zona UF/m²", number(listing.get("zona_uf_m2"))),
        ("Dormitorios", number(listing["bedrooms_n"])),
        ("Estacionamientos", number(listing.get("parking"))),
        ("Gastos comunes", number(listing.get("gastos_comunes_clp"), prefix="$")),
        ("Barrio", listing.get("barrio") if pd.notna(listing.get("barrio")) else None),
        ("Publicado desde", listing["first_seen_date"]),
    ]

    lines = "".join(
        f"<div><b>{label}:</b> {value}</div>" if label else f"<div>{value}</div>"
        for label, value in rows
        if value is not None
    )

    return (
        f'<div style="font-family:system-ui,sans-serif;font-size:13px;'
        f'min-width:220px">'
        f'<a href="{listing["url"]}" target="_blank" '
        f'style="font-weight:600">{listing["title"]}</a>'
        f'<div style="margin-top:6px">{lines}</div>'
        f"</div>"
    )


def generate_interactive_map():
    recent = load_recent()

    if recent.empty:
        print("No recent listings with coordinates; skipping map.")
        return

    vmin, vmax = np.percentile(recent["uf_per_m2"], [5, 95])

    colormap = branca.colormap.LinearColormap(
        SEQ_BLUE,
        vmin=round(vmin),
        vmax=round(vmax),
        caption="UF/m² (útiles)",
    )

    fmap = folium.Map(
        location=[recent["lat"].mean(), recent["lng"].mean()],
        zoom_start=14,
        tiles="CartoDB positron",
    )

    today = pd.Timestamp.today().strftime("%Y-%m-%d")

    title = (
        '<div style="position:fixed;top:10px;left:50%;transform:translateX(-50%);'
        'z-index:1000;background:#fcfcfbee;padding:8px 16px;border-radius:8px;'
        'font-family:system-ui,sans-serif;box-shadow:0 1px 4px rgba(0,0,0,.2)">'
        '<div style="font-size:15px;font-weight:600;color:#0b0b0b">'
        "Avisos recientes en Providencia — UF/m²</div>"
        f'<div style="font-size:12px;color:#52514e">{len(recent)} departamentos '
        f"&lt;{RECENT_MAX_M2} m² vistos por primera vez en los últimos "
        f"{RECENT_DAYS} días · {today}</div></div>"
    )
    fmap.get_root().html.add_child(folium.Element(title))

    for _, listing in recent.iterrows():
        value = min(max(listing["uf_per_m2"], vmin), vmax)

        folium.CircleMarker(
            location=[listing["lat"], listing["lng"]],
            radius=6,
            color="#fcfcfb",
            weight=1,
            fill=True,
            fill_color=colormap(value),
            fill_opacity=0.9,
            tooltip=(
                f"{listing['uf_per_m2']:,.1f} UF/m² · "
                f"{listing['price_uf']:,.0f} UF"
            ),
            popup=folium.Popup(format_popup(listing), max_width=320),
        ).add_to(fmap)

    colormap.add_to(fmap)

    fmap.save(OUTPUT_HTML)
    print(f"Saved {len(recent)} listings to {OUTPUT_HTML}")


if __name__ == "__main__":
    generate_interactive_map()
