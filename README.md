# PropertyTracker

[![Scrape Listings](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml/badge.svg)](https://github.com/BarbaraPFloresRios/PropertyTracker/actions/workflows/scrape.yml)

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

This repository is the **data pipeline**: it collects, enriches and publishes the dataset. The goal is for that dataset to support detecting investment opportunities — undervalued listings, price drops, and neighborhoods trending above or below their historical price per m². Any ranking built on personal criteria (budget, preferred area, shortlist) is deliberately kept out of this repo and lives locally.

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings published in the last 14 days, under 150 m², under $500M CLP, still live. Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Beds | Parking | Common exp. | Published |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Dueño Arrienda Departamento Amplio En Las Condes](https://www.portalinmobiliario.com/MLC-4545941784-dueno-arrienda-departamento-amplio-en-las-condes-_JM) | 486 | $20,000,000 | 126 | 3.86 | 4 | 2 | $300,000 | 2026-10-06 |
| [Depto Rosas  4hab 3ba 147m2-metros Plaza D Armas -santa Ana-](https://www.portalinmobiliario.com/MLC-4534638388-depto-rosas-4hab-3ba-147m2-metros-plaza-d-armas-santa-ana--_JM) | 3,087 | $127,000,099 | 143 | 21.59 | 4 | 0 | $60,000 | 2026-10-02 |
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2303279741-departamento-estudio-en-excelente-ubicacion-_JM) | 1,215 | $50,000,000 | 55 | 22.10 | 1 | 0 | $50 | 2026-10-07 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2303279751-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 1 | 0 | $50,000 | 2026-10-07 |
| [Vendo Dpto. Estudio Con Bodega Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2303267269-vendo-dpto-estudio-con-bodega-excelente-ubicacion-_JM) | 1,142 | $47,000,000 | 50 | 22.85 | 1 | 0 | $50,000 | 2026-10-07 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2303267273-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,094 | $45,000,000 | 45 | 24.31 | 1 | 0 | $50,000 | 2026-10-07 |
| [Metro Toesca, / Parque Almagro](https://www.portalinmobiliario.com/MLC-2300503211-metro-toesca-parque-almagro-_JM) | 2,600 | $106,967,978 | 105 | 24.76 | 3 | 0 | $1 | 2026-10-06 |
| [Excelente Departamento 2 Dormitorios/barrio Yungay](https://www.portalinmobiliario.com/MLC-4534638246-excelente-departamento-2-dormitoriosbarrio-yungay-_JM) | 1,300 | $53,483,989 | 50 | 26.00 | 2 | 0 | $50,000 | 2026-10-02 |
| [Venta Departamento Duplex Cerca Metro Rondizzonni](https://www.portalinmobiliario.com/MLC-2291497239-venta-departamento-duplex-cerca-metro-rondizzonni-_JM) | 1,580 | $65,000,000 | 60 | 26.33 | 2 | 0 | $20,000 | 2026-10-02 |
| [Departamento En Venta  Santiago Centro \| Conversable](https://www.portalinmobiliario.com/MLC-4544892924-departamento-en-venta-santiago-centro-conversable-_JM) | 1,070 | $44,000,000 | 40 | 26.74 | 1 | 0 | $80,000 | 2026-10-06 |
| [Amplitud Y Conexión Inigualable! Venta 4d Y 2b Santiago](https://www.portalinmobiliario.com/MLC-2300655587-amplitud-y-conexion-inigualable-venta-4d-y-2b-santiago-_JM) | 3,800 | $156,337,814 | 142 | 26.76 | 4 | 0 | $50,000 | 2026-10-06 |
| [Departamento Santiago Av. Balmaceda Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4526099734-departamento-santiago-av-balmaceda-remate-15-octubre-2026-_JM) | 1,155 | $47,500,000 | 43 | 26.85 | 2 | 0 |  | nan |
| [Departamento En Venta De 4 Dorm.3 Baños 160 M2 En Santiago](https://www.portalinmobiliario.com/MLC-4557232746-departamento-en-venta-de-4-dorm3-banos-160-m2-en-santiago-_JM) | 3,600 | $148,109,508 | 130 | 27.69 | 4 | 0 | $0 | 2026-10-09 |
| [Cesión De Promesa De Cv De Depto Nuevo Entrega En Dic-2026](https://www.portalinmobiliario.com/MLC-4536724996-cesion-de-promesa-de-cv-de-depto-nuevo-entrega-en-dic-2026-_JM) | 1,800 | $74,054,754 | 64 | 28.12 | 2 | 1 |  | 2026-10-03 |
| [Oportunidad De Inversión En El Corazón De Santiago $65 Mm](https://www.portalinmobiliario.com/MLC-2293289251-oportunidad-de-inversion-en-el-corazon-de-santiago-65-mm-_JM) | 1,580 | $65,000,000 | 56 | 28.21 | 2 | 0 |  | 2026-10-02 |
| [Venta Departamento 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-4543942130-venta-departamento-4d-centro-historico-santiago-_JM) | 3,330 | $137,000,000 | 116 | 28.71 | 4 | 0 | $150,000 | 2026-10-05 |
| [Se Remata Departamento Santiago Centro](https://www.portalinmobiliario.com/MLC-4552202306-se-remata-departamento-santiago-centro-_JM) | 1,580 | $65,000,000 | 55 | 28.73 | 2 | 0 | $75,000 | 2026-10-08 |
| [(185419)](https://www.portalinmobiliario.com/MLC-4552189244-185419-_JM) | 1,500 | $61,712,295 | 50 | 30.00 | 1 | 0 | $60,000 | 2026-10-08 |
| [Oportunidad Única, San Isidro 635, 3dor 2b, Sin Comisión](https://www.portalinmobiliario.com/MLC-2282587525-oportunidad-unica-san-isidro-635-3dor-2b-sin-comision-_JM) | 1,590 | $65,415,033 | 53 | 30.00 | 3 | 0 | $170,000 | 2026-09-28 |
| [Se Vende Departamento En Arturo Prat/alameda](https://www.portalinmobiliario.com/MLC-4534632972-se-vende-departamento-en-arturo-pratalameda-_JM) | 1,823 | $75,000,000 | 60 | 30.38 | 2 | 1 | $90,000 | 2026-10-02 |
| [Departamento  Santiago Centro  San Antonio / Oportunidad](https://www.portalinmobiliario.com/MLC-4560593032-departamento-santiago-centro-san-antonio-oportunidad-_JM) | 2,309 | $95,000,000 | 75 | 30.79 | 3 | 0 | $0 | 2026-09-29 |
| [Departamento Stgo Miguel León Prado Remate 15 Octubre 2026](https://www.portalinmobiliario.com/MLC-4525972044-departamento-stgo-miguel-leon-prado-remate-15-octubre-2026-_JM) | 991 | $40,767,020 | 32 | 30.97 | 1 | 0 |  | nan |
| [Departamento En Venta  Calle Porvenir 630, Santiago 3d 1b+ E](https://www.portalinmobiliario.com/MLC-2293358745-departamento-en-venta-calle-porvenir-630-santiago-3d-1b-e-_JM) | 2,133 | $87,754,883 | 68 | 31.37 | 3 | 1 | $68,000 | 2026-10-02 |
| [Departamento En Zocalo (181014)](https://www.portalinmobiliario.com/MLC-4531671308-departamento-en-zocalo-181014-_JM) | 1,580 | $65,000,000 | 50 | 31.60 | 1 | 0 | $1 | 2026-10-01 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2293134947-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,990 | $123,013,175 | 94 | 31.81 | 3 | 0 | $60,000 | 2026-10-02 |
| [Vendo Departamento 2d + 2b, Calle Porvenir, Santiago](https://www.portalinmobiliario.com/MLC-4543829842-vendo-departamento-2d-2b-calle-porvenir-santiago-_JM) | 1,920 | $79,000,000 | 60 | 32.00 | 2 | 0 | $90,000 | 2026-10-05 |
| [Departamento  U Oficina Santiago Centro Paseo Bulnes](https://www.portalinmobiliario.com/MLC-4557229082-departamento-u-oficina-santiago-centro-paseo-bulnes-_JM) | 3,281 | $135,000,000 | 102 | 32.17 | 3 | 0 | $150,000 | 2026-09-28 |
| [Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-2317929639-departamento-en-venta-en-santiago-_JM) | 1,288 | $53,000,000 | 40 | 32.20 | 1 | 0 |  | 2026-10-11 |
| [Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-2317942583-departamento-en-venta-en-santiago-_JM) | 1,264 | $52,000,000 | 39 | 32.41 | 1 | 0 | $22,000 | 2026-10-11 |
| [Plaza Yungay Oportunidad](https://www.portalinmobiliario.com/MLC-4545940608-plaza-yungay-oportunidad-_JM) | 1,750 | $72,000,000 | 54 | 32.41 | 3 | 0 | $67,000 | 2026-10-06 |
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

Both pipelines run daily at 23:00 UTC (20:00 in Chile during DST, 19:00 otherwise) via GitHub Actions — `.github/workflows/scrape.yml` and `scrape_arriendo.yml` — and commit their own data.

They run on a **self-hosted runner**, not on GitHub's hosted ones: since 2026-09-29 the site answers HTTP 200 with no content to datacenter IPs, for both search pages and detail pages, so the scrape only works from a residential connection. The runner takes one job at a time, so the two pipelines serialize instead of hammering the site in parallel.

A guard aborts the run if the scrape comes back empty. An empty scrape is not "no new listings", it's the source refusing to answer — and continuing would rebuild the recent set, the map and the README from a frozen dataset, quietly publishing a map that empties itself as the 14-day window moves while the badge stayed green.

## Notes

* Paid placements (`is_pad`) are excluded: they often belong to other comunas and duplicate organic results
* For new developments, m² comes as a range, so `uf_per_m2` is only computed for listings with a single m² value
* One run per pipeline per day, sequential, with a pause between requests. A sale run is roughly 126 search pages (42 per comuna, the site's pagination cap) plus up to 300 detail pages for enrichment and ~1,900 for the re-check; a rental run is ~92 search pages plus enrichment
* Detail pages are fetched once per listing and cached, and the source throttles (HTTP 429) past a few thousand requests in a day — which is why enrichment is capped per run and the pipelines are spread across the evening rather than bunched up

## Status

Active personal project focused on real estate data collection, price tracking, and investment opportunity modeling.
