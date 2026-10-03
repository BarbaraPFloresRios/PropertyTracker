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
| [Se Vende Cesión De Promesa](https://www.portalinmobiliario.com/MLC-4510326138-se-vende-cesion-de-promesa-_JM) | 405 | $16,638,113 | 21 | 19.29 | 153 | 1 | 1 | $60,000 | 2026-09-24 |
| [Rosas -morande Departamento 4hab 3ba 147m2 Piso Parquet](https://www.portalinmobiliario.com/MLC-4534638388-rosas-morande-departamento-4hab-3ba-147m2-piso-parquet-_JM) | 3,091 | $127,000,099 | 143 | 21.62 | 62 | 4 | 0 | $60,000 | 2026-10-02 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2267397959-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,144 | $47,000,000 | 50 | 22.88 | 74 | 1 | 0 | $50,000 | 2026-09-23 |
| [Vendo Dpto. Estudio Con Bodega Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2267436743-vendo-dpto-estudio-con-bodega-excelente-ubicacion-_JM) | 1,144 | $47,000,000 | 50 | 22.88 | 74 | 1 | 0 | $50,000 | 2026-09-23 |
| [Venta Departamento De 1 Dormitorio Calle Mario Kreutzberger](https://www.portalinmobiliario.com/MLC-2267423261-venta-departamento-de-1-dormitorio-calle-mario-kreutzberger-_JM) | 1,300 | $53,406,288 | 55 | 23.64 | 53 | 2 | 0 | $70,000 | 2026-09-23 |
| [Departamento Grande Pedro Lagos San Diego  (184015)](https://www.portalinmobiliario.com/MLC-2275517211-departamento-grande-pedro-lagos-san-diego-184015-_JM) | 1,800 | $73,947,168 | 70 | 25.71 | 53 | 2 | 0 | $45,000 | 2026-09-26 |
| [Excelente Departamento 2 Dormitorios/barrio Yungay](https://www.portalinmobiliario.com/MLC-4534638246-excelente-departamento-2-dormitoriosbarrio-yungay-_JM) | 1,300 | $53,406,288 | 50 | 26.00 | 66 | 2 | 0 | $50,000 | 2026-10-02 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2293122333-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 1,200 | $49,298,112 | 46 | 26.09 | 72 | 3 | 0 | $70,000 | 2026-10-02 |
| [Venta Departamento Duplex Cerca Metro Rondizzonni](https://www.portalinmobiliario.com/MLC-2291497239-venta-departamento-duplex-cerca-metro-rondizzonni-_JM) | 1,582 | $65,000,000 | 60 | 26.37 | 61 | 2 | 0 | $20,000 | 2026-10-02 |
| [Departamento Santiago Av. Balmaceda Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4526099734-departamento-santiago-av-balmaceda-remate-15-octubre-2026-_JM) | 1,156 | $47,500,000 | 43 | 26.89 | 66 | 2 | 0 |  | 2026-10-01 |
| [Venta Departamento 1d, Metro Santa Ana, Santiago](https://www.portalinmobiliario.com/MLC-4506396540-venta-departamento-1d-metro-santa-ana-santiago-_JM) | 1,339 | $55,000,000 | 48 | 27.89 | 73 | 1 | 0 | $62,000 | 2026-09-23 |
| [Cesión De Promesa De Cv De Depto Nuevo Entrega En Dic-2026](https://www.portalinmobiliario.com/MLC-4536724996-cesion-de-promesa-de-cv-de-depto-nuevo-entrega-en-dic-2026-_JM) | 1,800 | $73,947,168 | 64 | 28.12 | 111 | 2 | 1 |  | 2026-10-03 |
| [Oportunidad De Inversión En El Corazón De Santiago $65 Mm](https://www.portalinmobiliario.com/MLC-2293289251-oportunidad-de-inversion-en-el-corazon-de-santiago-65-mm-_JM) | 1,582 | $65,000,000 | 56 | 28.25 | 53 | 2 | 0 |  | 2026-10-02 |
| [Inersion ,comercial O Habutacional 2d/1b Maciver (180206)](https://www.portalinmobiliario.com/MLC-4513700244-inersion-comercial-o-habutacional-2d1b-maciver-180206-_JM) | 1,826 | $75,000,000 | 61 | 29.93 | 53 | 2 | 0 | $75,000 | 2026-09-25 |
| [Oportunidad Única, San Isidro 635, 3dor 2b, Sin Comisión](https://www.portalinmobiliario.com/MLC-2282587525-oportunidad-unica-san-isidro-635-3dor-2b-sin-comision-_JM) | 1,590 | $65,319,998 | 53 | 30.00 | 65 | 3 | 0 | $170,000 | 2026-09-29 |
| [Departamento 2hab 1ba Cercano A Estación De Metro](https://www.portalinmobiliario.com/MLC-4513393944-departamento-2hab-1ba-cercano-a-estacion-de-metro-_JM) | 1,826 | $75,000,000 | 60 | 30.43 | 65 | 2 | 0 | $70,000 | 2026-09-25 |
| [Se Vende Departamento En Arturo Prat/alameda](https://www.portalinmobiliario.com/MLC-4534632972-se-vende-departamento-en-arturo-pratalameda-_JM) | 1,826 | $75,000,000 | 60 | 30.43 | 54 | 2 | 1 | $90,000 | 2026-10-02 |
| [Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-4516303766-departamento-en-venta-en-santiago-_JM) | 3,660 | $150,359,242 | 120 | 30.50 | 64 | 4 | 0 | $0 | 2026-09-26 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (183263)](https://www.portalinmobiliario.com/MLC-2259888161-unico-3-dormitorios-bodega-metro-rondizzoni-183263-_JM) | 1,320 | $54,217,112 | 43 | 30.70 | 72 | 3 | 0 | $80,000 | 2026-09-21 |
| [Venta Departamento Santiago Centro San Antonio - Monjitas](https://www.portalinmobiliario.com/MLC-2285758297-venta-departamento-santiago-centro-san-antonio-monjitas-_JM) | 2,312 | $95,000,000 | 75 | 30.83 | 53 | 3 | 0 | $0 | 2026-10-01 |
| [Departamento Stgo Miguel León Prado Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4525972044-departamento-stgo-miguel-leon-prado-remate-15-octubre-2026-_JM) | 992 | $40,767,020 | 32 | 31.01 | 83 | 1 | 0 |  | 2026-10-01 |
| [Depto. Gran Oportunidad, Precio Rebajado. Id. 41205](https://www.portalinmobiliario.com/MLC-2271027351-depto-gran-oportunidad-precio-rebajado-id-41205-_JM) | 1,710 | $70,249,810 | 55 | 31.09 | 65 | 2 | 0 |  | 2026-09-24 |
| [Departamento Lord Cochrane Id: 133796](https://www.portalinmobiliario.com/MLC-2261827245-departamento-lord-cochrane-id-133796-_JM) | 1,400 | $57,502,998 | 45 | 31.11 | 72 | 2 | 1 | $54,000 | 2026-09-21 |
| [Departamento En Venta  Calle Porvenir, Santiago  3d 1b + E](https://www.portalinmobiliario.com/MLC-2293358745-departamento-en-venta-calle-porvenir-santiago-3d-1b-e-_JM) | 2,133 | $87,627,394 | 68 | 31.37 | 54 | 3 | 1 | $68,000 | 2026-10-02 |
| [Departamento En Venta De 3 Dorm. En Santiago, 2 Baños.](https://www.portalinmobiliario.com/MLC-2290654451-departamento-en-venta-de-3-dorm-en-santiago-2-banos-_JM) | 3,773 | $155,000,000 | 120 | 31.44 | 62 | 3 | 0 | $80,000 | 2026-10-01 |
| [Departamento En Zocalo (181014)](https://www.portalinmobiliario.com/MLC-4531671308-departamento-en-zocalo-181014-_JM) | 1,582 | $65,000,000 | 50 | 31.64 | 74 | 1 | 0 | $1 | 2026-10-01 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2293134947-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,990 | $122,834,462 | 94 | 31.81 | 55 | 3 | 0 | $60,000 | 2026-10-02 |
| [Venta Departamento 2hab 2ba Santiago](https://www.portalinmobiliario.com/MLC-4519049306-venta-departamento-2hab-2ba-santiago-_JM) | 2,239 | $92,000,000 | 70 | 31.99 | 51 | 2 | 0 | $80,000 | 2026-09-27 |
| [Remate Propiedad Departamento  U Oficina Santiago Centro](https://www.portalinmobiliario.com/MLC-4522144566-remate-propiedad-departamento-u-oficina-santiago-centro-_JM) | 3,286 | $135,000,000 | 102 | 32.22 | 55 | 3 | 0 | $150,000 | 2026-09-28 |
| [Cuarto Piso Con Bodega 2 Dormitorios (183695)](https://www.portalinmobiliario.com/MLC-4510325552-cuarto-piso-con-bodega-2-dormitorios-183695-_JM) | 1,200 | $49,298,112 | 37 | 32.43 | 72 | 2 | 0 | $65,000 | 2026-09-24 |
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
