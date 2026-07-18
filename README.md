# PropertyTracker

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 7 days (under 100 m²). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4146269686-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,000 | $81,689,580 | 46 | 43.48 | 2 | 0 | $80,000 | 2026-07-16 |
| [Venta Lindo Depto. Metro Parque Bustamante, Providencia](https://www.portalinmobiliario.com/MLC-4054680968-venta-lindo-depto-metro-parque-bustamante-providencia-_JM) | 4,200 | $171,548,118 | 93 | 45.16 | 3 | 0 | $20,000 | 2026-07-16 |
| [Venta Depto., En Torres De Tajamar, Corazón De Providencia](https://www.portalinmobiliario.com/MLC-4188421040-venta-depto-en-torres-de-tajamar-corazon-de-providencia-_JM) | 3,900 | $159,294,681 | 82 | 47.56 | 1 | 0 | $130,000 | 2026-07-16 |
| [Vicuña Mackenna/bilbao, 3 Dorm, 2 Baños, Terraza (175770)](https://www.portalinmobiliario.com/MLC-2064049869-vicuna-mackennabilbao-3-dorm-2-banos-terraza-175770-_JM) | 4,040 | $165,000,000 | 84 | 48.09 | 3 | 0 | $30,000 | 2026-07-16 |
| [Oportunidad ! Recien Remodelado Depto 3d2b Parque Bustamante](https://www.portalinmobiliario.com/MLC-1849120345-oportunidad-recien-remodelado-depto-3d2b-parque-bustamante-_JM) | 4,149 | $169,465,034 | 86 | 48.24 | 3 | 0 | $95,000 | 2026-07-16 |
| [Depto / Metro Los Leones](https://www.portalinmobiliario.com/MLC-4198200752-depto-metro-los-leones-_JM) | 4,500 | $183,801,555 | 93 | 48.39 | 3 | 0 | $155,000 | 2026-07-18 |
| [Departamento En Venta En Barrio Italia](https://www.portalinmobiliario.com/MLC-3998830902-departamento-en-venta-en-barrio-italia-_JM) | 4,200 | $171,548,118 | 86 | 48.84 | 3 | 0 | $30,000 | 2026-07-16 |
| [Departamento En Venta O Arriendo, Manuel Montt, Providencia](https://www.portalinmobiliario.com/MLC-1932778275-departamento-en-venta-o-arriendo-manuel-montt-providencia-_JM) | 4,040 | $165,000,000 | 82 | 49.26 | 1 | 0 | $130,000 | 2026-07-16 |
| [Malaquias Concha / Parque Bustamante](https://www.portalinmobiliario.com/MLC-4155621330-malaquias-concha-parque-bustamante-_JM) | 4,200 | $171,548,118 | 85 | 49.41 | 3 | 0 | $30,000 | 2026-07-16 |
| [Metro Santa Isabel / 3 Dormitorios 2 Baños](https://www.portalinmobiliario.com/MLC-4198500546-metro-santa-isabel-3-dormitorios-2-banos-_JM) | 4,200 | $171,548,118 | 85 | 49.41 | 3 | 0 | $30,000 | 2026-07-18 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-2007590945-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 4,162 | $170,000,000 | 84 | 49.55 | 3 | 0 | $50,000 | 2026-07-16 |
| [Departamento En Venta, Manuel Montt, En Providencia](https://www.portalinmobiliario.com/MLC-1932778309-departamento-en-venta-manuel-montt-en-providencia-_JM) | 4,064 | $166,000,000 | 82 | 49.56 | 1 | 0 | $130,000 | 2026-07-16 |
| [Amplio Y Luminoso Departamento En Gran Sector De Providencia](https://www.portalinmobiliario.com/MLC-4063908486-amplio-y-luminoso-departamento-en-gran-sector-de-providencia-_JM) | 4,800 | $196,054,992 | 96 | 50.00 | 3 | 0 | $30,000 | 2026-07-16 |
| [Departamento En Venta De 1d + 2b En Providencia, 75mts.](https://www.portalinmobiliario.com/MLC-4155493916-departamento-en-venta-de-1d-2b-en-providencia-75mts-_JM) | 3,890 | $158,886,233 | 75 | 51.87 | 1 | 0 | $140,000 | 2026-07-16 |
| [Luminoso Y Amplio! 2d+1b+pieza Servicio-parque Bustamante](https://www.portalinmobiliario.com/MLC-2004388751-luminoso-y-amplio-2d1bpieza-servicio-parque-bustamante-_JM) | 4,491 | $183,433,952 | 86 | 52.22 | 2 | 0 | $0 | 2026-07-16 |
| [Luminoso Y Cómodo! 2d+1b+servicios - Parque Bustamante](https://www.portalinmobiliario.com/MLC-2004376185-luminoso-y-comodo-2d1bservicios-parque-bustamante-_JM) | 4,491 | $183,433,952 | 86 | 52.22 | 2 | 0 | $0 | 2026-07-16 |
| [Vendemos Depto  3 Dorm + 2 Baños  - Providencia](https://www.portalinmobiliario.com/MLC-2046335163-vendemos-depto-3-dorm-2-banos-providencia-_JM) | 4,680 | $191,153,617 | 87 | 53.79 | 3 | 0 | $95,000 | 2026-07-16 |
| [Departamento En Venta De 2 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-3882854416-departamento-en-venta-de-2-dorm-en-providencia-_JM) | 4,064 | $166,000,000 | 75 | 54.19 | 2 | 0 |  | 2026-07-16 |
| [Depto Dúplex 4 Dorms / 2 Baños / Metro P De Valdivia](https://www.portalinmobiliario.com/MLC-3879998620-depto-duplex-4-dorms-2-banos-metro-p-de-valdivia-_JM) | 5,200 | $212,392,908 | 95 | 54.74 | 4 | 0 | $120,000 | 2026-07-16 |
| [Depto 3 Dormitorios 2 Baños, Providencia](https://www.portalinmobiliario.com/MLC-3946820116-depto-3-dormitorios-2-banos-providencia-_JM) | 4,550 | $185,843,794 | 83 | 54.82 | 3 | 0 | $0 | 2026-07-16 |
| [En Venta Dúplex En El Corazón De Providencia](https://www.portalinmobiliario.com/MLC-4020436272-en-venta-duplex-en-el-corazon-de-providencia-_JM) | 5,000 | $204,223,950 | 91 | 54.95 | 3 | 0 |  | 2026-07-16 |
| [Departamento Oportunidad 4d2b Duplex Metro Pedro Valdivia](https://www.portalinmobiliario.com/MLC-4170191206-departamento-oportunidad-4d2b-duplex-metro-pedro-valdivia-_JM) | 5,200 | $212,392,908 | 94 | 55.32 | 4 | 0 | $90,000 | 2026-07-16 |
| [Torres Tajamar/2d/2b/ Metro Manuel Montt](https://www.portalinmobiliario.com/MLC-1957381549-torres-tajamar2d2b-metro-manuel-montt-_JM) | 4,040 | $165,000,000 | 73 | 55.34 | 2 | 0 | $140,000 | 2026-07-16 |
| [Lindo Departamento En Felix Cabrera / Pedro De Valdivia](https://www.portalinmobiliario.com/MLC-2016417437-lindo-departamento-en-felix-cabrera-pedro-de-valdivia-_JM) | 4,600 | $187,886,034 | 83 | 55.42 | 3 | 0 | $55,000 | 2026-07-16 |
| [Departamento En Venta 2 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-1720802765-departamento-en-venta-2-dorm-en-providencia-_JM) | 5,100 | $208,308,429 | 92 | 55.43 | 2 | 0 |  | 2026-07-16 |
| [Depto 4 Dormitorios, 2 Baños, 90 M2 (75040)](https://www.portalinmobiliario.com/MLC-4098189688-depto-4-dormitorios-2-banos-90-m2-75040-_JM) | 4,990 | $203,815,502 | 90 | 55.44 | 4 | 0 | $120,000 | 2026-07-16 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-3808028916-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 5,500 | $224,646,345 | 99 | 55.56 | 3 | 0 | $0 | 2026-07-16 |
| [Departamento En Venta 3d En Providencia](https://www.portalinmobiliario.com/MLC-1903158397-departamento-en-venta-3d-en-providencia-_JM) | 5,000 | $204,223,950 | 90 | 55.56 | 3 | 0 | $96,000 | 2026-07-16 |
| [2 Dormitorios En Providencia](https://www.portalinmobiliario.com/MLC-1900443457-2-dormitorios-en-providencia-_JM) | 5,400 | $220,561,866 | 97 | 55.67 | 2 | 0 | $330,000 | 2026-07-16 |
| [Metro Baquedano / 1 D / 1 B / Luminoso / Full Eléctrico](https://www.portalinmobiliario.com/MLC-2049062195-metro-baquedano-1-d-1-b-luminoso-full-electrico-_JM) | 2,800 | $114,365,412 | 50 | 56.00 | 1 | 0 | $56,000 | 2026-07-16 |
<!-- RECENT_LISTINGS:END -->

## How it works

Each run:

* Scrapes all search result pages for the configured searches (no browser needed — the site embeds structured JSON in its HTML)
* Compares against the stored dataset by listing ID
* Reports **truly new listings** and **price changes** since the last run
* Tracks `first_seen_date`, `last_seen_date` and `first_seen_price` per listing
* Stores the full history in `data/raw/portalinmobiliario_listings.csv`
* Exports listings discovered in the last 7 days (under 100 m², sorted by UF/m²) to `data/recent_listings.csv`

```bash
python3 main.py
```

The exact publication date is not public on the site, so `first_seen_date` approximates it with one-day precision when the tracker runs daily — building a timestamped dataset that doesn't exist anywhere else.

## Data captured

Per listing: title, price in both UF and CLP (converted daily via mindicador.cl), bedrooms, bathrooms, usable m², **UF per m²** (computed), location, property kind (used / new development), seller, URL, and first/last seen dates.

Recent listings are also enriched from each listing's detail page with **parking spots** and **monthly common expenses** (gastos comunes), fetched once per listing and cached.

## Roadmap: ML for investment opportunity detection

The dataset this tracker accumulates is designed to feed machine learning models:

* **Price modeling** — regression models (hedonic pricing) to estimate the expected price of a listing from its attributes (m², bedrooms, neighborhood, floor, building age), flagging listings priced significantly below their prediction as potential opportunities
* **Time-on-market signals** — using `first_seen` / `last_seen` history to estimate how fast comparable properties sell, and which price cuts precede a sale
* **Neighborhood trends** — tracking median UF/m² per neighborhood over time to detect areas appreciating faster than the comuna average
* **Anomaly detection** — unsupervised methods to surface listings that deviate from their cluster of comparables

## Configuration

Searches are defined in `scrapers/portalinmobiliario.py` (`SEARCHES`). To add rentals or other comunas:

```python
SEARCHES = [
    {"operation": "venta", "property_type": "departamento", "location": "providencia-metropolitana"},
    {"operation": "arriendo", "property_type": "departamento", "location": "providencia-metropolitana"},
]
```

The `location` slug is the one that appears in the site URL when searching for a comuna.

## Notes

* Paid placements (`is_pad`) are excluded: they often belong to other comunas and duplicate organic results
* For new developments, m² comes as a range, so `uf_per_m2` is only computed for listings with a single m² value
* One daily run with a 1-second pause between pages (~70 requests) keeps the load on the site respectful

## Status

Active personal project focused on real estate data collection, price tracking, and investment opportunity modeling.
