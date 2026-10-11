import re

import pandas as pd


README_PATH = "README.md"
RECENT_LISTINGS_PATH = "data/recent_listings.csv"

START_MARKER = "<!-- RECENT_LISTINGS:START -->"
END_MARKER = "<!-- RECENT_LISTINGS:END -->"

MAX_ROWS = 30


def format_number(value, prefix="", decimals=0):
    try:
        if pd.isna(value):
            return ""
        return f"{prefix}{float(value):,.{decimals}f}"
    except (TypeError, ValueError):
        return ""


def make_listings_table(max_rows=MAX_ROWS):
    df = pd.read_csv(RECENT_LISTINGS_PATH)

    if df.empty:
        return "_No recent listings found._"

    df = df.head(max_rows)

    rows = [
        "| Listing | UF | CLP | m² | UF/m² | Beds | Parking | Common exp. | Published |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]

    for _, listing in df.iterrows():
        title = str(listing.get("title", "")).replace("|", "\\|")
        url = listing.get("url", "")
        title_cell = f"[{title}]({url})" if url else title

        rows.append(
            "| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
                title_cell,
                format_number(listing.get("price_uf")),
                format_number(listing.get("price_clp"), prefix="$"),
                format_number(listing.get("m2_utiles")),
                format_number(listing.get("uf_per_m2"), decimals=2),
                format_number(listing.get("bedrooms_n")),
                format_number(listing.get("parking")),
                format_number(listing.get("gastos_comunes_clp"), prefix="$"),
                listing.get("publicado_fecha_est", ""),
            )
        )

    return "\n".join(rows)


def generate_readme():
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()

    # El texto se arma desde las constantes del pipeline a proposito: antes
    # estaba escrito a mano y quedo desfasado -- decia "first seen in the last
    # 14 days" y "published within the last 30 days" cuando el filtro ya era
    # por fecha de PUBLICACION y el tope de 30 dias se habia eliminado.
    # Import diferido: src/pipeline.py importa este modulo, asi que uno a
    # nivel de modulo seria circular.
    from src.pipeline import RECENT_DAYS, RECENT_MAX_M2, RECENT_MAX_PRICE_CLP

    criterios = (
        f"published in the last {RECENT_DAYS} days, "
        f"under {RECENT_MAX_M2} m², "
        f"under ${RECENT_MAX_PRICE_CLP / 1e6:,.0f}M CLP, "
        "still live"
    )

    section = (
        f"{START_MARKER}\n"
        f"_Top {MAX_ROWS} by UF/m² among listings {criterios}. "
        "Updated automatically from `data/recent_listings.csv`._\n\n"
        f"{make_listings_table()}\n"
        f"{END_MARKER}"
    )

    readme = re.sub(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        lambda _: section,
        readme,
        flags=re.DOTALL,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme)


if __name__ == "__main__":
    generate_readme()
    print("Updated README.md")
