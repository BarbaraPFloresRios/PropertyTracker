# PropertyTracker

[![Scrape Listings](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml/badge.svg)](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml)

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

This repository is the **data pipeline**: it collects, enriches and publishes the dataset. The goal is for that dataset to support detecting investment opportunities — undervalued listings, price drops, and neighborhoods trending above or below their historical price per m². Any ranking built on personal criteria (budget, preferred area, shortlist) is deliberately kept out of this repo and lives locally.

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings published in the last 90 days, still live. Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Beds | Parking | Common exp. | Published |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Dueño Arrienda Departamento Amplio En Las Condes](https://www.portalinmobiliario.com/MLC-4545941784-dueno-arrienda-departamento-amplio-en-las-condes-_JM) | 486 | $20,000,000 | 126 | 3.86 | 4 | 2 | $300,000 | 2026-10-06 |
| [Departamento En Venta De 1 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2308607395-departamento-en-venta-de-1-dorm-en-santiago-_JM) | 1,604 | $66,000,000 | 345 | 4.65 | 1 | 0 | $0 | 2026-09-03 |
| [En Venta Nuevo Sin Uso Depto. 1d 1b Ideal Inversión Excelent](https://www.portalinmobiliario.com/MLC-2305697135-en-venta-nuevo-sin-uso-depto-1d-1b-ideal-inversion-excelent-_JM) | 2,000 | $82,293,660 | 379 | 5.28 | 1 | 0 | $50,000 | 2026-10-08 |
| [Depto. Nuevo 1d/1b Con Balcón En Edificio Full Equipamiento](https://www.portalinmobiliario.com/MLC-4536353126-depto-nuevo-1d1b-con-balcon-en-edificio-full-equipamiento-_JM) | 2,000 | $82,293,660 | 379 | 5.28 | 1 | 0 | $50,000 | 2026-08-05 |
| [Cesión Promesa Depto 2d+1b Edif. Diagonal Vicuña](https://www.portalinmobiliario.com/MLC-4576380346-cesion-promesa-depto-2d1b-edif-diagonal-vicuna-_JM) | 364 | $15,000,000 | 48 | 7.59 | 2 | 0 |  | 2026-10-13 |
| [Arturo Prat (133742)](https://www.portalinmobiliario.com/MLC-4542162148-arturo-prat-133742-_JM) | 2,910 | $119,737,275 | 311 | 9.36 | 1 | 0 | $60,000 | 2026-09-05 |
| [Departamento Duplex Barrio Republica](https://www.portalinmobiliario.com/MLC-4572416946-departamento-duplex-barrio-republica-_JM) | 3,694 | $152,000,000 | 220 | 16.79 | 3 | 0 | $100,000 | 2026-09-21 |
| [Venta Edificio Cerro Santa Lucía Barrio Lastarria](https://www.portalinmobiliario.com/MLC-2296555483-venta-edificio-cerro-santa-lucia-barrio-lastarria-_JM) | 8,990 | $369,910,002 | 510 | 17.63 | 12 | 0 | $0 | 2026-09-23 |
| [Se Vende Cesión De Promesa](https://www.portalinmobiliario.com/MLC-4510326138-se-vende-cesion-de-promesa-_JM) | 405 | $16,664,466 | 21 | 19.29 | 1 | 1 | $60,000 | 2026-09-23 |
| [Depto Rosas  4hab 3ba 147m2-metros Plaza D Armas -santa Ana-](https://www.portalinmobiliario.com/MLC-4534638388-depto-rosas-4hab-3ba-147m2-metros-plaza-d-armas-santa-ana--_JM) | 3,086 | $127,000,099 | 143 | 21.58 | 4 | 0 | $60,000 | 2026-10-02 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2303279751-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 1 | 0 | $50,000 | 2026-10-07 |
| [Vendo Dpto. Estudio Con Bodega Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2303267269-vendo-dpto-estudio-con-bodega-excelente-ubicacion-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 1 | 0 | $50,000 | 2026-10-07 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2303267273-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,094 | $45,000,000 | 45 | 24.30 | 1 | 0 | $50,000 | 2026-10-07 |
| [Metro Toesca, / Parque Almagro](https://www.portalinmobiliario.com/MLC-2300503211-metro-toesca-parque-almagro-_JM) | 2,600 | $106,981,758 | 105 | 24.76 | 3 | 0 | $1 | 2026-10-06 |
| [Se Vende Metro Cumming (90527)](https://www.portalinmobiliario.com/MLC-4552224588-se-vende-metro-cumming-90527-_JM) | 2,600 | $107,000,000 | 100 | 26.00 | 3 | 0 | $20,000 | 2026-09-08 |
| [Excelente Departamento 2 Dormitorios/barrio Yungay](https://www.portalinmobiliario.com/MLC-4534638246-excelente-departamento-2-dormitoriosbarrio-yungay-_JM) | 1,300 | $53,490,879 | 50 | 26.00 | 2 | 0 | $50,000 | 2026-10-02 |
| [Venta Departamento Duplex Cerca Metro Rondizzonni](https://www.portalinmobiliario.com/MLC-2291497239-venta-departamento-duplex-cerca-metro-rondizzonni-_JM) | 1,580 | $65,000,000 | 60 | 26.33 | 2 | 0 | $20,000 | 2026-10-02 |
| [Departamento En Venta  Santiago Centro \| Conversable](https://www.portalinmobiliario.com/MLC-4544892924-departamento-en-venta-santiago-centro-conversable-_JM) | 1,069 | $44,000,000 | 40 | 26.73 | 1 | 0 | $80,000 | 2026-10-06 |
| [Amplitud Y Conexión Inigualable! Venta 4d Y 2b Santiago](https://www.portalinmobiliario.com/MLC-4576342484-amplitud-y-conexion-inigualable-venta-4d-y-2b-santiago-_JM) | 3,800 | $156,357,954 | 142 | 26.76 | 4 | 0 | $50,000 | 2026-10-13 |
| [Departamento Completamente Remodelado (144421)](https://www.portalinmobiliario.com/MLC-2293686871-departamento-completamente-remodelado-144421-_JM) | 1,650 | $67,892,270 | 60 | 27.50 | 2 | 0 | $15,000 | 2026-09-03 |
| [Departamento En Venta De 4 Dorm.3 Baños 160 M2 En Santiago](https://www.portalinmobiliario.com/MLC-4557232746-departamento-en-venta-de-4-dorm3-banos-160-m2-en-santiago-_JM) | 3,600 | $148,128,588 | 130 | 27.69 | 4 | 0 | $0 | 2026-10-09 |
| [Cesión De Promesa De Cv De Depto Nuevo Entrega En Dic-2026](https://www.portalinmobiliario.com/MLC-4536724996-cesion-de-promesa-de-cv-de-depto-nuevo-entrega-en-dic-2026-_JM) | 1,800 | $74,064,294 | 64 | 28.12 | 2 | 1 |  | 2026-10-03 |
| [Oportunidad De Inversión En El Corazón De Santiago $65 Mm](https://www.portalinmobiliario.com/MLC-2293289251-oportunidad-de-inversion-en-el-corazon-de-santiago-65-mm-_JM) | 1,580 | $65,000,000 | 56 | 28.21 | 2 | 0 |  | 2026-10-02 |
| [Venta Departamento Santiago De 3 Dorm 2 Baños Antiguo Piso 1](https://www.portalinmobiliario.com/MLC-4574289876-venta-departamento-santiago-de-3-dorm-2-banos-antiguo-piso-1-_JM) | 2,673 | $110,000,000 | 94 | 28.44 | 3 | 0 | $68,000 | 2026-08-21 |
| [Venta Departamento 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-4576368068-venta-departamento-4d-centro-historico-santiago-_JM) | 3,330 | $137,000,000 | 116 | 28.70 | 4 | 0 | $150,000 | 2026-10-05 |
| [Se Remata Departamento Santiago Centro](https://www.portalinmobiliario.com/MLC-4552202306-se-remata-departamento-santiago-centro-_JM) | 1,580 | $65,000,000 | 55 | 28.72 | 2 | 0 | $75,000 | 2026-10-08 |
| [Depto En Santiago Centro: Oportunidad Inversión (171236)](https://www.portalinmobiliario.com/MLC-2312819831-depto-en-santiago-centro-oportunidad-inversion-171236-_JM) | 1,823 | $75,000,000 | 62 | 29.40 | 3 | 0 | $60,000 | 2026-08-19 |
| [Departamento Piso Completo, 2do Piso, Providencia 329](https://www.portalinmobiliario.com/MLC-2303304327-departamento-piso-completo-2do-piso-providencia-329-_JM) | 9,000 | $370,321,470 | 305 | 29.51 | 8 | 1 | $700,000 | 2026-10-08 |
| [Departamento 1 Dormitorio - 1 Baño ( Santa Ana - Santiago )](https://www.portalinmobiliario.com/MLC-4574289770-departamento-1-dormitorio-1-bano-santa-ana-santiago--_JM) | 1,600 | $65,834,928 | 54 | 29.63 | 1 | 0 | $46,000 | 2026-10-13 |
| [Venta Depto. 3d/1b Piso De Parquet Centro Histórico De Stgo](https://www.portalinmobiliario.com/MLC-4551120574-venta-depto-3d1b-piso-de-parquet-centro-historico-de-stgo-_JM) | 2,490 | $102,455,607 | 84 | 29.64 | 3 | 0 | $30,000 | 2026-09-05 |
<!-- RECENT_LISTINGS:END -->

## How it works

Each run:

* Scrapes all search result pages for the configured searches (no browser needed — the site embeds structured JSON in its HTML)
* Compares against the stored dataset by listing ID
* Reports **truly new listings** and **price changes** since the last run
* Tracks `first_seen_date`, `last_seen_date` and `first_seen_price` per listing
* Stores the full history in `data/raw/portalinmobiliario_listings.csv`
* Re-checks the currently published set and flags listings whose detail page now reads *"Publicación finalizada"*
* Exports the **recent set** to `data/recent_listings.csv`: published in the last 14 days, under 150 m², under $500M CLP, and still live (the thresholds are the `RECENT_*` constants in `src/pipeline.py`, and the README table caption is generated from them so it cannot drift)

There are two independent pipelines, each with its own entry point, its own CSV and its own schedule. Nothing in one touches the other's files:

```bash
python3 main.py            # sale listings  -> data/raw/portalinmobiliario_listings.csv (+ map + README)
python3 main_arriendo.py   # rental listings -> data/raw/portalinmobiliario_rentals.csv
```

**On publication dates.** The site never exposes an exact one, but each detail page says *"Publicado hoy / ayer / hace N días"*. That text is parsed into `publicado_fecha_est` (`publicado_hace` keeps the raw string), which is precise to the day for anything published within the last month. This matters because listings rotate into the newest-first search window months after being published: filtering by `first_seen_date` would label them as new, which is why the recent set filters by publication date instead.

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

Searches live in `scrapers/portalinmobiliario.py`: `SEARCHES` for sales and `SEARCHES_ARRIENDO` for rentals. Both currently cover three comunas — Providencia, Las Condes and Santiago Centro:

```python
SEARCHES = [
    {"operation": "venta", "property_type": "departamento", "location": "providencia-metropolitana"},
    # ... las-condes-metropolitana, santiago-metropolitana
]
```

Adding a comuna is one entry in that list and nothing else: the display name, the map title, the README table and the filters are all derived from the data. The `location` slug is the one that appears in the site URL when searching for a comuna.

## Automation

Both pipelines run daily via GitHub Actions — `.github/workflows/scrape.yml` and `scrape_arriendo.yml` — and commit their own data. They run on a self-hosted runner, triggered from that machine at 20:00 local (rentals first, so the map the sale pipeline builds carries the same night's rental layer). The `schedule:` block in each workflow is a backup at 00:30 UTC, an hour and a half later, for nights the machine missed.

They run on a **self-hosted runner**, not on GitHub's hosted ones: since 2026-09-29 the site answers HTTP 200 with no content to datacenter IPs, for both search pages and detail pages, so the scrape only works from a residential connection. The runner takes one job at a time, so the two pipelines serialize instead of hammering the site in parallel.

A guard aborts the run if the scrape comes back empty. An empty scrape is not "no new listings", it's the source refusing to answer — and continuing would rebuild the recent set, the map and the README from a frozen dataset, quietly publishing a map that empties itself as the 14-day window moves while the badge stayed green.

## Notes

* Paid placements (`is_pad`) are excluded: they often belong to other comunas and duplicate organic results
* For new developments, m² comes as a range, so `uf_per_m2` is only computed for listings with a single m² value
* One run per pipeline per day, sequential, with a pause between requests. A sale run is roughly 126 search pages (42 per comuna, the site's pagination cap) plus up to 300 detail pages for enrichment and ~1,900 for the re-check; a rental run is ~92 search pages plus enrichment
* Detail pages are fetched once per listing and cached, and the source throttles (HTTP 429) past a few thousand requests in a day — which is why enrichment is capped per run and the pipelines are spread across the evening rather than bunched up

## Status

Active personal project focused on real estate data collection, price tracking, and investment opportunity modeling.
