# PropertyTracker

[![Scrape Listings](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml/badge.svg)](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml)

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 14 days (under 150 m², published within the last 30 days). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Zona UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Venta Departamento 4hab 3ba Santiago](https://www.portalinmobiliario.com/MLC-4480540246-venta-departamento-4hab-3ba-santiago-_JM) | 3,099 | $127,000,000 | 143 | 21.67 | 62 | 4 | 0 | $60,000 | 2026-09-15 |
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4480186602-departamento-estudio-en-excelente-ubicacion-_JM) | 1,220 | $50,000,000 | 55 | 22.19 | 54 | 1 | 0 | $50 | 2026-09-15 |
| [Se Vende Metro Cumming (90527)](https://www.portalinmobiliario.com/MLC-4457859102-se-vende-metro-cumming-90527-_JM) | 2,611 | $107,000,000 | 100 | 26.11 | 50 | 3 | 0 | $20,000 | 2026-09-08 |
| [Piso Completo Con Estilo Único En Avenida Brasil](https://www.portalinmobiliario.com/MLC-4460679066-piso-completo-con-estilo-unico-en-avenida-brasil-_JM) | 4,027 | $165,000,000 | 147 | 27.39 | 62 | 5 | 0 | $0 | 2026-09-09 |
| [Departamento San Pablo Id: 49821](https://www.portalinmobiliario.com/MLC-4487268130-departamento-san-pablo-id-49821-_JM) | 2,858 | $117,120,000 | 100 | 28.58 | 53 | 3 | 0 | $85,000 | 2026-09-17 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2244992059-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,294 | $53,000,000 | 45 | 28.74 | 74 | 1 | 0 | $50,000 | 2026-09-15 |
| [Venta Departamento 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-2256976743-venta-departamento-4d-centro-historico-santiago-_JM) | 3,344 | $137,000,000 | 116 | 28.82 | 62 | 4 | 0 | $150,000 | 2026-09-20 |
| [Excelente Departamento En Venta De 3 Dorm.c/ Serv. Santiago](https://www.portalinmobiliario.com/MLC-2237931549-excelente-departamento-en-venta-de-3-dormc-serv-santiago-_JM) | 4,320 | $177,000,000 | 148 | 29.19 | 64 | 3 | 0 | $0 | 2026-09-12 |
| [Departamento En Venta, Barrio Republica, Santiago](https://www.portalinmobiliario.com/MLC-4485738860-departamento-en-venta-barrio-republica-santiago-_JM) | 1,758 | $72,034,771 | 60 | 29.30 | 48 | 1 | 0 | $15,000 | 2026-09-17 |
| [Departamento A Pasos Metro](https://www.portalinmobiliario.com/MLC-4468493482-departamento-a-pasos-metro-_JM) | 2,733 | $112,000,000 | 90 | 30.37 | 55 | 4 | 1 | $75,000 | 2026-09-11 |
| [Venta Departamento 2hab 1ba Santiago](https://www.portalinmobiliario.com/MLC-4468664726-venta-departamento-2hab-1ba-santiago-_JM) | 1,830 | $75,000,000 | 60 | 30.51 | 65 | 2 | 0 | $70,000 | 2026-09-11 |
| [Dptos. En Venta Comuna De Santiago 1d Y 1baño](https://www.portalinmobiliario.com/MLC-4484377550-dptos-en-venta-comuna-de-santiago-1d-y-1bano-_JM) | 1,464 | $60,000,000 | 47 | 31.16 | 71 | 1 | 0 | $10,000 | 2026-09-16 |
| [Amplio Y Céntrico Departamento](https://www.portalinmobiliario.com/MLC-2235126581-amplio-y-centrico-departamento-_JM) | 2,196 | $90,000,000 | 70 | 31.38 | 53 | 2 | 1 | $70,000 | 2026-09-11 |
| [Departamento En Venta De 3 Dorm. En Santiago, 2 Baños.](https://www.portalinmobiliario.com/MLC-4467066450-departamento-en-venta-de-3-dorm-en-santiago-2-banos-_JM) | 3,783 | $155,000,000 | 120 | 31.52 | 62 | 3 | 0 | $80,000 | 2026-09-10 |
| [Amplio Departamento Sector Cumming (171236)](https://www.portalinmobiliario.com/MLC-2256985533-amplio-departamento-sector-cumming-171236-_JM) | 1,960 | $80,311,804 | 62 | 31.61 | 47 | 3 | 0 | $60,000 | 2026-09-19 |
| [Departamento Versátil En Ubicación Estratégica Santiago](https://www.portalinmobiliario.com/MLC-2241157623-departamento-versatil-en-ubicacion-estrategica-santiago-_JM) | 3,800 | $155,706,558 | 120 | 31.67 | 62 | 3 | 1 | $165,000 | 2026-09-14 |
| [Departamento En Venta En Santiago Centro (182117)](https://www.portalinmobiliario.com/MLC-2231312405-departamento-en-venta-en-santiago-centro-182117-_JM) | 1,340 | $54,907,049 | 42 | 31.90 | 74 | 1 | 0 | $30,000 | 2026-09-09 |
| [Venta Departamento 2hab 2ba Santiago](https://www.portalinmobiliario.com/MLC-4456988782-venta-departamento-2hab-2ba-santiago-_JM) | 2,245 | $92,000,000 | 70 | 32.07 | 51 | 2 | 0 | $80,000 | 2026-09-08 |
| [Oferta (174950)](https://www.portalinmobiliario.com/MLC-4465529118-oferta-174950-_JM) | 1,952 | $80,000,000 | 60 | 32.54 | 48 | 2 | 0 | $93,000 | 2026-09-10 |
| [Departamento Como Nuevo En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4484467946-departamento-como-nuevo-en-excelente-ubicacion-_JM) | 3,060 | $125,384,755 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-09-16 |
| [3 Dormitorios Metro Rondizzoni (164475)](https://www.portalinmobiliario.com/MLC-2248192535-3-dormitorios-metro-rondizzoni-164475-_JM) | 1,400 | $57,365,574 | 43 | 32.56 | 72 | 3 | 0 | $80,000 | 2026-09-16 |
| [Dpto Enventa Manuel De Amat 3d 1b $78.000.000 (139829)](https://www.portalinmobiliario.com/MLC-4462120188-dpto-enventa-manuel-de-amat-3d-1b-78000000-139829-_JM) | 1,904 | $78,000,000 | 58 | 32.82 | 53 | 3 | 0 | $0 | 2026-09-09 |
| [Se Vende Depto. Recién Remodelado](https://www.portalinmobiliario.com/MLC-4454057412-se-vende-depto-recien-remodelado-_JM) | 2,300 | $94,243,443 | 70 | 32.86 | 68 | 3 | 0 | $95,000 | 2026-09-07 |
| [Cómodo Departamento 2 Dor 1 Baño Calle Zenteno](https://www.portalinmobiliario.com/MLC-4467059908-comodo-departamento-2-dor-1-bano-calle-zenteno-_JM) | 1,490 | $61,053,361 | 45 | 33.11 | 72 | 2 | 0 | $0 | 2026-09-10 |
| [Amplio Y Luminoso, Vendo Depto Stgo (170838)](https://www.portalinmobiliario.com/MLC-4487265186-amplio-y-luminoso-vendo-depto-stgo-170838-_JM) | 1,990 | $81,541,066 | 60 | 33.17 | 54 | 2 | 0 | $20,000 | 2026-09-17 |
| [{ Error : Could Not Find A Suitable Tls Ca Ce (181945)](https://www.portalinmobiliario.com/MLC-4460678322--error-could-not-find-a-suitable-tls-ca-ce-181945-_JM) | 2,001 | $82,000,000 | 60 | 33.35 | 47 | 3 | 0 | $50,000 | 2026-09-09 |
| [Remodelado, Oportunidad, A Pasos De Metro, Incluye Bodega](https://www.portalinmobiliario.com/MLC-4457860128-remodelado-oportunidad-a-pasos-de-metro-incluye-bodega-_JM) | 1,750 | $71,706,968 | 52 | 33.65 | 54 | 2 | 0 | $77,000 | 2026-09-08 |
| [Departamento Estilo Mariposa, Excelente Ubicacion!](https://www.portalinmobiliario.com/MLC-2223988779-departamento-estilo-mariposa-excelente-ubicacion-_JM) | 1,650 | $67,609,426 | 49 | 33.67 | 71 | 2 | 0 | $85,000 | 2026-09-07 |
| [Acogedor Departamento 2d Con Vista Despejada En Santiago](https://www.portalinmobiliario.com/MLC-4485718888-acogedor-departamento-2d-con-vista-despejada-en-santiago-_JM) | 1,660 | $68,000,000 | 49 | 33.87 | 74 | 2 | 0 | $61,000 | 2026-09-16 |
| [Dpto. 2 Hab-1baño-bodega-piso 22 (82631)](https://www.portalinmobiliario.com/MLC-4457310592-dpto-2-hab-1bano-bodega-piso-22-82631-_JM) | 1,700 | $69,658,197 | 50 | 34.00 | 72 | 2 | 0 | $50,000 | 2026-09-08 |
<!-- RECENT_LISTINGS:END -->

## How it works

Each run:

* Scrapes all search result pages for the configured searches (no browser needed — the site embeds structured JSON in its HTML)
* Compares against the stored dataset by listing ID
* Reports **truly new listings** and **price changes** since the last run
* Tracks `first_seen_date`, `last_seen_date` and `first_seen_price` per listing
* Stores the full history in `data/raw/portalinmobiliario_listings.csv`
* Exports listings discovered in the last 14 days (under 150 m², sorted by UF/m²) to `data/recent_listings.csv`

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
