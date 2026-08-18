# PropertyTracker

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 7 days (under 100 m², published within the last 30 days). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Zona UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2170303589-departamento-estudio-en-excelente-ubicacion-_JM) | 1,224 | $50,000,000 | 55 | 22.25 | 54 | 1 | 0 | $50 | 2026-08-18 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2169832273-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,150 | $47,000,000 | 50 | 23.01 | 74 | 1 | 0 | $50,000 | 2026-08-18 |
| [Terraza De Lujo En Estoril](https://www.portalinmobiliario.com/MLC-4328827246-terraza-de-lujo-en-estoril-_JM) | 2,100 | $85,798,944 | 80 | 26.25 |  |  | 0 |  | 2026-08-13 |
| [Vendo Departamento A Pasos De Metro Matta](https://www.portalinmobiliario.com/MLC-2160903893-vendo-departamento-a-pasos-de-metro-matta-_JM) | 2,448 | $100,000,000 | 90 | 27.20 | 55 | 2 | 0 | $45,000 | 2026-08-15 |
| [En Venta 2 Dormitorios Contado Calle Zenteno](https://www.portalinmobiliario.com/MLC-4358312720-en-venta-2-dormitorios-contado-calle-zenteno-_JM) | 1,101 | $45,000,000 | 40 | 27.54 | 71 | 2 | 0 | $65,000 | 2026-08-17 |
| [Venta Departamento 1d, Metro Santa Ana, Santiago](https://www.portalinmobiliario.com/MLC-2160892015-venta-departamento-1d-metro-santa-ana-santiago-_JM) | 1,346 | $55,000,000 | 48 | 28.05 | 73 | 1 | 0 | $62,000 | 2026-08-15 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2170328349-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,297 | $53,000,000 | 45 | 28.83 | 74 | 1 | 0 | $50,000 | 2026-08-18 |
| [Oportunidad Unica Precio Onfire En Santiago Centro](https://www.portalinmobiliario.com/MLC-4362223316-oportunidad-unica-precio-onfire-en-santiago-centro-_JM) | 1,969 | $80,446,724 | 66 | 29.83 | 53 | 3 | 0 | $110,000 | 2026-08-18 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4351490460-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,217 | $90,579,171 | 72 | 30.79 | 53 | 2 | 0 | $45,000 | 2026-08-15 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4354301522-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,909 | $78,000,000 | 61 | 31.30 | 54 | 2 | 0 | $80,000 | 2026-08-16 |
| [Casco Histórico, Metro Santa Ana](https://www.portalinmobiliario.com/MLC-2169759145-casco-historico-metro-santa-ana-_JM) | 2,700 | $110,312,928 | 84 | 32.14 |  | 2 | 0 |  | 2026-08-18 |
| [Departamento Como Nuevo En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4352651460-departamento-como-nuevo-en-excelente-ubicacion-_JM) | 3,060 | $125,021,318 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-16 |
| [3 Dormitorios Metro Rondizzoni (164475)](https://www.portalinmobiliario.com/MLC-2164064429-3-dormitorios-metro-rondizzoni-164475-_JM) | 1,400 | $57,199,296 | 43 | 32.56 | 71 | 3 | 0 | $80,000 | 2026-08-16 |
| [Amplio Y Luminoso, Vendo Depto Stgo (170838)](https://www.portalinmobiliario.com/MLC-2167513311-amplio-y-luminoso-vendo-depto-stgo-170838-_JM) | 1,990 | $81,304,714 | 60 | 33.17 | 54 | 2 | 0 | $20,000 | 2026-08-17 |
| [Departamento General Gana Id: 148539](https://www.portalinmobiliario.com/MLC-2170328421-departamento-general-gana-id-148539-_JM) | 930 | $38,000,000 | 28 | 33.22 | 71 | 1 | 0 | $38,540 | 2026-08-18 |
| [Toesca, Bascuñan Con Terraza](https://www.portalinmobiliario.com/MLC-4354897238-toesca-bascunan-con-terraza-_JM) | 2,029 | $82,900,000 | 61 | 33.26 | 48 | 3 | 0 | $160,000 | 2026-08-16 |
| [Depto Antiguo De 58mts2 - Enrique Mac Iver](https://www.portalinmobiliario.com/MLC-4349806856-depto-antiguo-de-58mts2-enrique-mac-iver-_JM) | 1,958 | $80,000,000 | 58 | 33.76 | 53 | 1 | 0 | $75,000 | 2026-08-15 |
| [Oportunidad  En El Corazón De Santiago Venta O Arriendo](https://www.portalinmobiliario.com/MLC-2170305383-oportunidad-en-el-corazon-de-santiago-venta-o-arriendo-_JM) | 2,032 | $83,000,000 | 60 | 33.86 | 48 | 2 | 0 | $70,000 | 2026-08-18 |
| [Venta Departamento Santiago Centro, San Pablo (141336)](https://www.portalinmobiliario.com/MLC-4358675422-venta-departamento-santiago-centro-san-pablo-141336-_JM) | 2,360 | $96,421,670 | 69 | 34.20 | 51 | 3 | 1 | $70,000 | 2026-08-17 |
| [Oportunidad De Remodelar, Junto A Metro U. De Chile](https://www.portalinmobiliario.com/MLC-2169840785-oportunidad-de-remodelar-junto-a-metro-u-de-chile-_JM) | 2,300 | $93,970,272 | 67 | 34.33 | 53 | 2 | 0 | $120,000 | 2026-08-18 |
| [Metro La Moneda Antiguo](https://www.portalinmobiliario.com/MLC-4342839466-metro-la-moneda-antiguo-_JM) | 2,600 | $106,227,264 | 75 | 34.67 | 53 | 3 | 0 | $100,000 | 2026-08-14 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2154926369-metro-parque-ohiggins-_JM) | 1,690 | $69,047,722 | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-14 |
| [Nataniel Cox Depto En Venta 2 D / 1b](https://www.portalinmobiliario.com/MLC-4362191528-nataniel-cox-depto-en-venta-2-d-1b-_JM) | 1,836 | $75,000,000 | 52 | 35.30 | 54 | 2 | 0 | $61,000 | 2026-08-18 |
| [Departamento Zenteno Id: 136284](https://www.portalinmobiliario.com/MLC-4362613680-departamento-zenteno-id-136284-_JM) | 1,958 | $80,000,000 | 55 | 35.60 | 53 | 2 | 0 | $0 | 2026-08-18 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4361366490-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,836 | $75,000,000 | 50 | 36.71 | 74 | 2 | 0 | $90,000 | 2026-08-18 |
| [Inversión O Vivir En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4345189968-inversion-o-vivir-en-excelente-ubicacion-_JM) | 1,959 | $80,038,158 | 53 | 36.96 | 65 | 2 | 1 | $100,000 | 2026-08-14 |
| [Vendemos Depto 2 Dormitorios  - Frente Teatro Teletón](https://www.portalinmobiliario.com/MLC-2154940207-vendemos-depto-2-dormitorios-frente-teatro-teleton-_JM) | 1,850 | $75,584,784 | 50 | 37.00 | 73 | 2 | 0 | $90,000 | 2026-08-14 |
| [Ideal Inversión \| Depto 1d Mac Iver,santiago (179104)](https://www.portalinmobiliario.com/MLC-4342891950-ideal-inversion-depto-1d-mac-iversantiago-179104-_JM) | 1,600 | $65,370,624 | 43 | 37.21 | 73 | 1 | 0 | $60,000 | 2026-08-14 |
| [2d 1b En Venta \| Arriendo Vigente $500.000](https://www.portalinmobiliario.com/MLC-2159717235-2d-1b-en-venta-arriendo-vigente-500000-_JM) | 2,500 | $102,141,600 | 67 | 37.31 | 54 | 2 | 0 | $80,000 | 2026-08-15 |
| [Acogedor Departamento 2d Con Vista Despejada En Santiago](https://www.portalinmobiliario.com/MLC-2166203337-acogedor-departamento-2d-con-vista-despejada-en-santiago-_JM) | 1,836 | $75,000,000 | 49 | 37.46 | 74 | 2 | 0 | $61,000 | 2026-08-17 |
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
