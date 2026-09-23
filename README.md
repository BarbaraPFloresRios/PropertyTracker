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
| [Venta Departamento 4hab 3ba Santiago](https://www.portalinmobiliario.com/MLC-4480540246-venta-departamento-4hab-3ba-santiago-_JM) | 3,098 | $127,000,000 | 143 | 21.67 | 62 | 4 | 0 | $60,000 | 2026-09-15 |
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4502771604-departamento-estudio-en-excelente-ubicacion-_JM) | 1,220 | $50,000,000 | 55 | 22.18 | 54 | 1 | 0 | $50 | 2026-09-22 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2267397959-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,147 | $47,000,000 | 50 | 22.93 | 74 | 1 | 0 | $50,000 | 2026-09-23 |
| [Vendo Dpto. Estudio Con Bodega Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2267436743-vendo-dpto-estudio-con-bodega-excelente-ubicacion-_JM) | 1,147 | $47,000,000 | 50 | 22.93 | 74 | 1 | 0 | $50,000 | 2026-09-23 |
| [Venta Departamento De 1 Dormitorio Cercano Metro Santa Ana](https://www.portalinmobiliario.com/MLC-2267423261-venta-departamento-de-1-dormitorio-cercano-metro-santa-ana-_JM) | 1,300 | $53,289,275 | 55 | 23.64 | 53 | 2 | 0 | $70,000 | 2026-09-23 |
| [Venta Departamento 1d, Metro Santa Ana, Santiago](https://www.portalinmobiliario.com/MLC-4506396540-venta-departamento-1d-metro-santa-ana-santiago-_JM) | 1,342 | $55,000,000 | 48 | 27.95 | 73 | 1 | 0 | $62,000 | 2026-09-23 |
| [Departamento San Pablo Id: 49821](https://www.portalinmobiliario.com/MLC-4487268130-departamento-san-pablo-id-49821-_JM) | 2,857 | $117,120,000 | 100 | 28.57 | 53 | 3 | 0 | $85,000 | 2026-09-17 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-4502661944-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,293 | $53,000,000 | 45 | 28.73 | 74 | 1 | 0 | $50,000 | 2026-09-22 |
| [Venta Departamento 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-2256976743-venta-departamento-4d-centro-historico-santiago-_JM) | 3,342 | $137,000,000 | 116 | 28.81 | 62 | 4 | 0 | $150,000 | 2026-09-20 |
| [Excelente Departamento En Venta De 3 Dorm.c/ Serv. Santiago](https://www.portalinmobiliario.com/MLC-2237931549-excelente-departamento-en-venta-de-3-dormc-serv-santiago-_JM) | 4,318 | $177,000,000 | 148 | 29.17 | 64 | 3 | 0 | $0 | 2026-09-12 |
| [Departamento En Venta, Barrio Republica, Santiago](https://www.portalinmobiliario.com/MLC-4485738860-departamento-en-venta-barrio-republica-santiago-_JM) | 1,758 | $72,063,496 | 60 | 29.30 | 48 | 1 | 0 | $15,000 | 2026-09-17 |
| [Departamento A Pasos Metro](https://www.portalinmobiliario.com/MLC-4468493482-departamento-a-pasos-metro-_JM) | 2,732 | $112,000,000 | 90 | 30.36 | 55 | 4 | 1 | $75,000 | 2026-09-11 |
| [Venta Departamento 2hab 1ba Santiago](https://www.portalinmobiliario.com/MLC-4468664726-venta-departamento-2hab-1ba-santiago-_JM) | 1,830 | $75,000,000 | 60 | 30.49 | 65 | 2 | 0 | $70,000 | 2026-09-11 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (183263)](https://www.portalinmobiliario.com/MLC-2259888161-unico-3-dormitorios-bodega-metro-rondizzoni-183263-_JM) | 1,320 | $54,109,110 | 43 | 30.70 | 72 | 3 | 0 | $80,000 | 2026-09-21 |
| [Dptos. En Venta Comuna De Santiago 1d Y 1baño](https://www.portalinmobiliario.com/MLC-4484377550-dptos-en-venta-comuna-de-santiago-1d-y-1bano-_JM) | 1,464 | $60,000,000 | 47 | 31.14 | 71 | 1 | 0 | $10,000 | 2026-09-16 |
| [Amplio Y Céntrico Departamento](https://www.portalinmobiliario.com/MLC-2235126581-amplio-y-centrico-departamento-_JM) | 2,196 | $90,000,000 | 70 | 31.37 | 53 | 2 | 1 | $70,000 | 2026-09-11 |
| [Departamento En Venta De 3 Dorm. En Santiago, 2 Baños.](https://www.portalinmobiliario.com/MLC-4467066450-departamento-en-venta-de-3-dorm-en-santiago-2-banos-_JM) | 3,781 | $155,000,000 | 120 | 31.51 | 62 | 3 | 0 | $80,000 | 2026-09-10 |
| [Amplio Departamento Sector Cumming (171236)](https://www.portalinmobiliario.com/MLC-2256985533-amplio-departamento-sector-cumming-171236-_JM) | 1,960 | $80,343,830 | 62 | 31.61 | 47 | 3 | 0 | $60,000 | 2026-09-19 |
| [Departamento Versátil En Ubicación Estratégica Santiago](https://www.portalinmobiliario.com/MLC-2241157623-departamento-versatil-en-ubicacion-estrategica-santiago-_JM) | 3,800 | $155,768,650 | 120 | 31.67 | 62 | 3 | 1 | $165,000 | 2026-09-14 |
| [Gran Liquidación Dpto Adj En Remate 3 D Y 1 B, Santiago.](https://www.portalinmobiliario.com/MLC-2265338957-gran-liquidacion-dpto-adj-en-remate-3-d-y-1-b-santiago-_JM) | 1,464 | $60,011,922 | 45 | 32.53 | 66 | 3 | 0 | $50,000 | 2026-09-22 |
| [Oferta (174950)](https://www.portalinmobiliario.com/MLC-4465529118-oferta-174950-_JM) | 1,952 | $80,000,000 | 60 | 32.53 | 48 | 2 | 0 | $93,000 | 2026-09-10 |
| [Departamento Como Nuevo En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4484467946-departamento-como-nuevo-en-excelente-ubicacion-_JM) | 3,060 | $125,434,755 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-09-16 |
| [3 Dormitorios Metro Rondizzoni (164475)](https://www.portalinmobiliario.com/MLC-2248192535-3-dormitorios-metro-rondizzoni-164475-_JM) | 1,400 | $57,388,450 | 43 | 32.56 | 72 | 3 | 0 | $80,000 | 2026-09-16 |
| [Venta Depa 2 Dorm 1 Baño Cocina Americana](https://www.portalinmobiliario.com/MLC-4500847080-venta-depa-2-dorm-1-bano-cocina-americana-_JM) | 1,490 | $61,077,708 | 45 | 33.11 | 72 | 2 | 0 | $0 | 2026-09-21 |
| [Departamento En Venta En Meiggs Santiago](https://www.portalinmobiliario.com/MLC-2267423375-departamento-en-venta-en-meiggs-santiago-_JM) | 2,022 | $82,900,000 | 61 | 33.15 | 48 | 3 | 1 | $122,000 | 2026-09-23 |
| [Amplio Y Luminoso, Vendo Depto Stgo (170838)](https://www.portalinmobiliario.com/MLC-4487265186-amplio-y-luminoso-vendo-depto-stgo-170838-_JM) | 1,990 | $81,573,582 | 60 | 33.17 | 54 | 2 | 0 | $20,000 | 2026-09-17 |
| [Venta Departamento 2d Y 2b Cerca De Futura Metro Línea 7](https://www.portalinmobiliario.com/MLC-4506283356-venta-departamento-2d-y-2b-cerca-de-futura-metro-linea-7-_JM) | 1,780 | $72,965,315 | 53 | 33.58 | 47 | 2 | 0 | $90,000 | 2026-09-23 |
| [Acogedor Departamento 2d Con Vista Despejada En Santiago](https://www.portalinmobiliario.com/MLC-4485718888-acogedor-departamento-2d-con-vista-despejada-en-santiago-_JM) | 1,659 | $68,000,000 | 49 | 33.86 | 74 | 2 | 0 | $61,000 | 2026-09-16 |
| [Departamento Antiguo - Uso Oficina/habitacional](https://www.portalinmobiliario.com/MLC-2267436595-departamento-antiguo-uso-oficinahabitacional-_JM) | 1,708 | $70,000,000 | 50 | 34.15 | 73 | 1 | 0 | $60,000 | 2026-09-23 |
| [Vendo Amplio Depto  3dorm 2ba Santiago Centro](https://www.portalinmobiliario.com/MLC-2265348611-vendo-amplio-depto-3dorm-2ba-santiago-centro-_JM) | 2,391 | $98,000,000 | 70 | 34.15 | 53 | 3 | 0 | $85,000 | 2026-09-22 |
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
