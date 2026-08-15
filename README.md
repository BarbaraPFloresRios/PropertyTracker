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
| [Terraza De Lujo En Estoril](https://www.portalinmobiliario.com/MLC-4328827246-terraza-de-lujo-en-estoril-_JM) | 2,100 | $85,790,649 | 80 | 26.25 |  |  | 0 |  | 2026-08-13 |
| [Vendo Departamento A Pasos De Metro Matta](https://www.portalinmobiliario.com/MLC-2160903893-vendo-departamento-a-pasos-de-metro-matta-_JM) | 2,448 | $100,000,000 | 90 | 27.20 | 55 | 2 | 0 | $45,000 | 2026-08-15 |
| [Venta Departamento 1d, Metro Santa Ana, Santiago](https://www.portalinmobiliario.com/MLC-2160892015-venta-departamento-1d-metro-santa-ana-santiago-_JM) | 1,346 | $55,000,000 | 48 | 28.05 | 73 | 1 | 0 | $62,000 | 2026-08-15 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4351490460-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,217 | $90,570,414 | 72 | 30.79 | 53 | 2 | 0 | $45,000 | 2026-08-15 |
| [Depto Antiguo De 58mts2 - Enrique Mac Iver](https://www.portalinmobiliario.com/MLC-4349806856-depto-antiguo-de-58mts2-enrique-mac-iver-_JM) | 1,958 | $80,000,000 | 58 | 33.76 | 53 | 1 | 0 | $75,000 | 2026-08-15 |
| [Metro La Moneda Antiguo](https://www.portalinmobiliario.com/MLC-4342839466-metro-la-moneda-antiguo-_JM) | 2,600 | $106,216,994 | 75 | 34.67 | 53 | 3 | 0 | $100,000 | 2026-08-14 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2154926369-metro-parque-ohiggins-_JM) | 1,690 | $69,041,046 | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-14 |
| [Inversión O Vivir En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4345189968-inversion-o-vivir-en-excelente-ubicacion-_JM) | 1,959 | $80,030,420 | 53 | 36.96 | 65 | 2 | 1 | $100,000 | 2026-08-14 |
| [Vendemos Depto 2 Dormitorios  - Frente Teatro Teletón](https://www.portalinmobiliario.com/MLC-2154940207-vendemos-depto-2-dormitorios-frente-teatro-teleton-_JM) | 1,850 | $75,577,476 | 50 | 37.00 | 73 | 2 | 0 | $90,000 | 2026-08-14 |
| [Ideal Inversión \| Depto 1d Mac Iver,santiago (179104)](https://www.portalinmobiliario.com/MLC-4342891950-ideal-inversion-depto-1d-mac-iversantiago-179104-_JM) | 1,600 | $65,364,304 | 43 | 37.21 | 73 | 1 | 0 | $60,000 | 2026-08-14 |
| [2d 1b En Venta \| Arriendo Vigente $500.000](https://www.portalinmobiliario.com/MLC-2159717235-2d-1b-en-venta-arriendo-vigente-500000-_JM) | 2,500 | $102,131,725 | 67 | 37.31 | 54 | 2 | 0 | $80,000 | 2026-08-15 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2159709115-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,958 | $80,000,000 | 52 | 37.66 | 47 | 2 | 0 | $600,000 | 2026-08-15 |
| [Renovado Studio Con Bodega Stgo Centro (152207)](https://www.portalinmobiliario.com/MLC-4345187646-renovado-studio-con-bodega-stgo-centro-152207-_JM) | 1,130 | $46,163,540 | 30 | 37.67 | 68 |  | 0 | $40,000 | 2026-08-14 |
| [Venta Departamento 2hab 1ba Santiago](https://www.portalinmobiliario.com/MLC-4342891226-venta-departamento-2hab-1ba-santiago-_JM) | 2,203 | $90,000,000 | 58 | 37.98 | 65 | 2 | 0 | $90,000 | 2026-08-14 |
| [Gran Oportunidad Venta Departamento,  Se Aceptan Ofertas](https://www.portalinmobiliario.com/MLC-4350393132-gran-oportunidad-venta-departamento-se-aceptan-ofertas-_JM) | 1,371 | $56,000,000 | 36 | 38.08 | 74 | 2 | 0 | $0 | 2026-08-15 |
| [Inversión Única: Dpto. 2d/2b En Santiago Centro](https://www.portalinmobiliario.com/MLC-2153981671-inversion-unica-dpto-2d2b-en-santiago-centro-_JM) | 1,983 | $81,010,884 | 52 | 38.13 |  | 2 | 0 |  | 2026-08-14 |
| [Dpto 2 Dormitorios,2 Baños, Metro Santa Ana (172571)](https://www.portalinmobiliario.com/MLC-2154957663-dpto-2-dormitorios2-banos-metro-santa-ana-172571-_JM) | 2,448 | $100,000,000 | 64 | 38.25 | 47 | 2 | 0 | $100,000 | 2026-08-14 |
| [Vendemos Confortable Departamento En Calle Cóndor](https://www.portalinmobiliario.com/MLC-2154940181-vendemos-confortable-departamento-en-calle-condor-_JM) | 1,990 | $81,296,853 | 52 | 38.27 | 54 | 2 | 0 | $40,000 | 2026-08-14 |
| [En Venta Depa Stgo  (106956)](https://www.portalinmobiliario.com/MLC-4351439642-en-venta-depa-stgo-106956-_JM) | 2,644 | $108,000,000 | 69 | 38.31 | 48 | 2 | 0 | $0 | 2026-08-15 |
| [Se Vende Dpto Recien Remodelado De 2d-1b En Roberto Espinoza](https://www.portalinmobiliario.com/MLC-2159712387-se-vende-dpto-recien-remodelado-de-2d-1b-en-roberto-espinoza-_JM) | 2,000 | $81,705,380 | 52 | 38.46 | 54 | 2 | 1 | $110,000 | 2026-08-15 |
| [Departamento 1d En Av. España, Cercano A Metro Republica](https://www.portalinmobiliario.com/MLC-2160854105-departamento-1d-en-av-espana-cercano-a-metro-republica-_JM) | 1,738 | $71,000,000 | 45 | 38.62 | 68 | 1 | 0 | $80,000 | 2026-08-15 |
| [Tu Nuevo Hogar Economico En Las Condes](https://www.portalinmobiliario.com/MLC-4313531944-tu-nuevo-hogar-economico-en-las-condes-_JM) | 2,595 | $106,000,000 | 67 | 38.73 | 85 | 4 | 0 | $0 | 2026-08-13 |
| [Condominio Blindados 2d/1b Metro Matta](https://www.portalinmobiliario.com/MLC-2160514035-condominio-blindados-2d1b-metro-matta-_JM) | 1,950 | $79,662,746 | 50 | 39.00 | 81 | 2 | 0 | $50,000 | 2026-08-15 |
| [Barrio Republica Dos Dormitorios Dos Baños](https://www.portalinmobiliario.com/MLC-2155655283-barrio-republica-dos-dormitorios-dos-banos-_JM) | 2,700 | $110,302,263 | 69 | 39.13 | 54 | 2 | 0 | $160,000 | 2026-08-14 |
| [Se Vende Departamento 2d+2b En Cumming 1350 Santiago](https://www.portalinmobiliario.com/MLC-4345167112-se-vende-departamento-2d2b-en-cumming-1350-santiago-_JM) | 2,400 | $98,046,456 | 61 | 39.34 | 47 | 2 | 0 | $0 | 2026-08-14 |
| [Amplio Depto. En Huérfanos Con Amunétegui](https://www.portalinmobiliario.com/MLC-4349802502-amplio-depto-en-huerfanos-con-amunetegui-_JM) | 3,182 | $130,000,000 | 80 | 39.78 | 55 | 3 | 0 | $120,000 | 2026-08-15 |
| [Bonito Depto Estilo Mariposa Con Terraza](https://www.portalinmobiliario.com/MLC-2159715865-bonito-depto-estilo-mariposa-con-terraza-_JM) | 1,990 | $81,296,853 | 50 | 39.80 | 71 | 2 | 0 | $100,000 | 2026-08-15 |
| [San Pablo Barroso Oportunidad](https://www.portalinmobiliario.com/MLC-4342838216-san-pablo-barroso-oportunidad-_JM) | 1,199 | $49,000,000 | 30 | 39.98 | 71 | 1 | 0 | $60,000 | 2026-08-14 |
| [Departamento En Venta En Santiago Centro (175599)](https://www.portalinmobiliario.com/MLC-2160910825-departamento-en-venta-en-santiago-centro-175599-_JM) | 3,690 | $150,746,426 | 92 | 40.11 | 51 | 3 | 0 | $0 | 2026-08-15 |
| [Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-2153960801-departamento-en-venta-en-santiago-_JM) | 2,421 | $98,900,000 | 60 | 40.35 | 48 | 2 | 0 | $0 | 2026-08-14 |
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
