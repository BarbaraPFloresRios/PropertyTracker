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
| [Dueño Arrienda Departamento Amplio En Las Condes](https://www.portalinmobiliario.com/MLC-4545941784-dueno-arrienda-departamento-amplio-en-las-condes-_JM) | 486 | $20,000,000 | 126 | 3.86 | 90 | 4 | 2 | $300,000 | 2026-10-06 |
| [Depto Rosas  4hab 3ba 147m2-metros Plaza D Armas -santa Ana-](https://www.portalinmobiliario.com/MLC-4534638388-depto-rosas-4hab-3ba-147m2-metros-plaza-d-armas-santa-ana--_JM) | 3,087 | $127,000,099 | 143 | 21.59 | 62 | 4 | 0 | $60,000 | 2026-10-02 |
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2303279741-departamento-estudio-en-excelente-ubicacion-_JM) | 1,216 | $50,000,000 | 55 | 22.10 | 54 | 1 | 0 | $50 | 2026-10-07 |
| [Vendo Dpto. Estudio Con Bodega Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2303267269-vendo-dpto-estudio-con-bodega-excelente-ubicacion-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 75 | 1 | 0 | $50,000 | 2026-10-07 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2303279751-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 75 | 1 | 0 | $50,000 | 2026-10-07 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2303267273-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,094 | $45,000,000 | 45 | 24.31 | 75 | 1 | 0 | $50,000 | 2026-10-07 |
| [Metro Toesca, / Parque Almagro](https://www.portalinmobiliario.com/MLC-2300503211-metro-toesca-parque-almagro-_JM) | 2,600 | $106,954,224 | 105 | 24.76 | 55 | 3 | 0 | $1 | 2026-10-06 |
| [Excelente Departamento 2 Dormitorios/barrio Yungay](https://www.portalinmobiliario.com/MLC-4534638246-excelente-departamento-2-dormitoriosbarrio-yungay-_JM) | 1,300 | $53,477,112 | 50 | 26.00 | 66 | 2 | 0 | $50,000 | 2026-10-02 |
| [Venta Departamento Duplex Cerca Metro Rondizzonni](https://www.portalinmobiliario.com/MLC-2291497239-venta-departamento-duplex-cerca-metro-rondizzonni-_JM) | 1,580 | $65,000,000 | 60 | 26.33 | 61 | 2 | 0 | $20,000 | 2026-10-02 |
| [Departamento En Venta  Santiago Centro \| Conversable](https://www.portalinmobiliario.com/MLC-4544892924-departamento-en-venta-santiago-centro-conversable-_JM) | 1,070 | $44,000,000 | 40 | 26.74 | 66 | 1 | 0 | $80,000 | 2026-10-06 |
| [Amplitud Y Conexión Inigualable! Venta 4d Y 2b Santiago](https://www.portalinmobiliario.com/MLC-2300655587-amplitud-y-conexion-inigualable-venta-4d-y-2b-santiago-_JM) | 3,800 | $156,317,712 | 142 | 26.76 | 64 | 4 | 0 | $50,000 | 2026-10-06 |
| [Departamento Santiago Av. Balmaceda Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4526099734-departamento-santiago-av-balmaceda-remate-15-octubre-2026-_JM) | 1,155 | $47,500,000 | 43 | 26.85 | 66 | 2 | 0 |  | 2026-10-01 |
| [Departamento En Venta De 4 Dorm.3 Baños 160 M2 En Santiago](https://www.portalinmobiliario.com/MLC-4557232746-departamento-en-venta-de-4-dorm3-banos-160-m2-en-santiago-_JM) | 3,600 | $148,090,464 | 130 | 27.69 |  | 4 | 0 | $0 | 2026-10-09 |
| [Cesión De Promesa De Cv De Depto Nuevo Entrega En Dic-2026](https://www.portalinmobiliario.com/MLC-4536724996-cesion-de-promesa-de-cv-de-depto-nuevo-entrega-en-dic-2026-_JM) | 1,800 | $74,045,232 | 64 | 28.12 | 111 | 2 | 1 |  | 2026-10-03 |
| [Oportunidad De Inversión En El Corazón De Santiago $65 Mm](https://www.portalinmobiliario.com/MLC-2293289251-oportunidad-de-inversion-en-el-corazon-de-santiago-65-mm-_JM) | 1,580 | $65,000,000 | 56 | 28.22 | 53 | 2 | 0 |  | 2026-10-02 |
| [Venta Departamento 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-4543942130-venta-departamento-4d-centro-historico-santiago-_JM) | 3,330 | $137,000,000 | 116 | 28.71 |  | 4 | 0 | $150,000 | 2026-10-05 |
| [Se Remata Departamento Santiago Centro](https://www.portalinmobiliario.com/MLC-4552202306-se-remata-departamento-santiago-centro-_JM) | 1,580 | $65,000,000 | 55 | 28.73 | 54 | 2 | 0 | $75,000 | 2026-10-08 |
| [(185419)](https://www.portalinmobiliario.com/MLC-4552189244-185419-_JM) | 1,500 | $61,704,360 | 50 | 30.00 | 74 | 1 | 0 | $60,000 | 2026-10-08 |
| [Oportunidad Única, San Isidro 635, 3dor 2b, Sin Comisión](https://www.portalinmobiliario.com/MLC-2282587525-oportunidad-unica-san-isidro-635-3dor-2b-sin-comision-_JM) | 1,590 | $65,406,622 | 53 | 30.00 | 65 | 3 | 0 | $170,000 | 2026-09-29 |
| [Se Vende Departamento En Arturo Prat/alameda](https://www.portalinmobiliario.com/MLC-4534632972-se-vende-departamento-en-arturo-pratalameda-_JM) | 1,823 | $75,000,000 | 60 | 30.39 | 54 | 2 | 1 | $90,000 | 2026-10-02 |
| [Departamento Stgo Miguel León Prado Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4525972044-departamento-stgo-miguel-leon-prado-remate-15-octubre-2026-_JM) | 991 | $40,767,020 | 32 | 30.97 | 83 | 1 | 0 |  | 2026-10-01 |
| [Departamento En Venta  Calle Porvenir 630, Santiago 3d 1b+ E](https://www.portalinmobiliario.com/MLC-2293358745-departamento-en-venta-calle-porvenir-630-santiago-3d-1b-e-_JM) | 2,133 | $87,743,600 | 68 | 31.37 | 54 | 3 | 1 | $68,000 | 2026-10-02 |
| [Departamento En Zocalo (181014)](https://www.portalinmobiliario.com/MLC-4531671308-departamento-en-zocalo-181014-_JM) | 1,580 | $65,000,000 | 50 | 31.60 | 74 | 1 | 0 | $1 | 2026-10-01 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2293134947-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,990 | $122,997,358 | 94 | 31.81 | 55 | 3 | 0 | $60,000 | 2026-10-02 |
| [Vendo Departamento 2d + 2b, Calle Porvenir, Santiago](https://www.portalinmobiliario.com/MLC-4543829842-vendo-departamento-2d-2b-calle-porvenir-santiago-_JM) | 1,920 | $79,000,000 | 60 | 32.01 | 54 | 2 | 0 | $90,000 | 2026-10-05 |
| [Departamento  U Oficina Santiago Centro Paseo Bulnes](https://www.portalinmobiliario.com/MLC-4557229082-departamento-u-oficina-santiago-centro-paseo-bulnes-_JM) | 3,282 | $135,000,000 | 102 | 32.17 | 55 | 3 | 0 | $150,000 | 2026-10-09 |
| [Departamento En Venta De 1 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4560591710-departamento-en-venta-de-1-dorm-en-santiago-_JM) | 1,288 | $53,000,000 | 40 | 32.21 | 75 | 1 | 0 | $50,000 | 2026-10-10 |
| [Plaza Yungay Oportunidad](https://www.portalinmobiliario.com/MLC-4545940608-plaza-yungay-oportunidad-_JM) | 1,750 | $72,000,000 | 54 | 32.41 | 47 | 3 | 0 | $67,000 | 2026-10-06 |
| [Departamento En Venta De 1 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4560604704-departamento-en-venta-de-1-dorm-en-santiago-_JM) | 1,264 | $52,000,000 | 39 | 32.41 | 83 | 1 | 0 | $22,000 | 2026-10-10 |
| [Excelente Ubicacion, Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-4534651350-excelente-ubicacion-departamento-en-venta-en-santiago-_JM) | 3,060 | $125,876,894 | 94 | 32.55 | 57 | 3 | 1 | $0 | 2026-10-02 |
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
