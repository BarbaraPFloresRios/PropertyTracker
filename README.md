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
| [Dueño Arrienda Departamento Amplio En Las Condes](https://www.portalinmobiliario.com/MLC-4545941784-dueno-arrienda-departamento-amplio-en-las-condes-_JM) | 485 | $20,000,000 | 126 | 3.85 | 4 | 2 | $300,000 | 2026-10-06 |
| [Depto 3d2b Con Estac. Y Bodega, Metro Toesca](https://www.portalinmobiliario.com/MLC-4606769502-depto-3d2b-con-estac-y-bodega-metro-toesca-_JM) | 3,220 | $132,817,369 | 646 | 4.98 | 3 | 1 | $0 | 2026-10-20 |
| [Cesión Promesa Dpto 2d+1b Edif. Diagonal Vicuña](https://www.portalinmobiliario.com/MLC-2356232925-cesion-promesa-dpto-2d1b-edif-diagonal-vicuna-_JM) | 364 | $15,000,000 | 41 | 8.87 | 2 | 0 |  | 2026-10-21 |
| [Se Vende Hermoso Departamento En Las Condes](https://www.portalinmobiliario.com/MLC-4637831488-se-vende-hermoso-departamento-en-las-condes-_JM) | 9,200 | $379,478,196 | 778 | 11.83 | 2 | 1 | $140,000 | 2026-10-31 |
| [Venta Dpto Duplex, Santiago Centro](https://www.portalinmobiliario.com/MLC-4620315448-venta-dpto-duplex-santiago-centro-_JM) | 3,685 | $152,000,000 | 220 | 16.75 | 3 | 0 | $100,000 | 2026-09-21 |
| [Oportunidad De Inversión Cerro Santa Lucía Barrio Lastarria](https://www.portalinmobiliario.com/MLC-2372126551-oportunidad-de-inversion-cerro-santa-lucia-barrio-lastarria-_JM) | 8,990 | $370,816,194 | 510 | 17.63 | 12 | 0 | $0 | 2026-09-23 |
| [Venta Edificio En Barrio República](https://www.portalinmobiliario.com/MLC-4630715400-venta-edificio-en-barrio-republica-_JM) | 9,500 | $391,852,485 | 465 | 20.43 | 9 | 8 | $0 | nan |
| [Rosas -morande Departamento 4hab 3ba 147m2 Piso Parquet](https://www.portalinmobiliario.com/MLC-2382524591-rosas-morande-departamento-4hab-3ba-147m2-piso-parquet-_JM) | 3,079 | $127,000,099 | 143 | 21.53 | 4 | 0 | $60,000 | 2026-10-03 |
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4628702962-departamento-estudio-en-excelente-ubicacion-_JM) | 1,212 | $50,000,000 | 55 | 22.04 | 1 | 0 | $50 | 2026-10-20 |
| [Departamento García Reyes Id: 148816](https://www.portalinmobiliario.com/MLC-2369061385-departamento-garcia-reyes-id-148816-_JM) | 1,000 | $41,247,630 | 42 | 23.81 | 1 | 0 | $100,000 | nan |
| [Dúplex 3d En Barrio Huemul  A 1 Cuadra De Metro Franklin](https://www.portalinmobiliario.com/MLC-2360721669-duplex-3d-en-barrio-huemul-a-1-cuadra-de-metro-franklin-_JM) | 1,600 | $65,996,208 | 67 | 23.88 | 3 | 0 | $15,000 | 2026-10-22 |
| [Departamento Grande Pedro Lagos San Diego  (184015)](https://www.portalinmobiliario.com/MLC-4624200930-departamento-grande-pedro-lagos-san-diego-184015-_JM) | 1,800 | $74,245,734 | 70 | 25.71 | 2 | 0 | $45,000 | 2026-09-26 |
| [Terraza En Lo Fontecilla Con Las Condes](https://www.portalinmobiliario.com/MLC-2352128235-terraza-en-lo-fontecilla-con-las-condes-_JM) | 2,100 | $86,620,023 | 80 | 26.25 |  | 0 |  | 2026-10-20 |
| [Gran Departamento 4d-2b Venta Santiago!](https://www.portalinmobiliario.com/MLC-4622099536-gran-departamento-4d-2b-venta-santiago-_JM) | 3,800 | $156,740,994 | 142 | 26.76 | 4 | 0 | $50,000 | 2026-10-14 |
| [Excelente Oportunidad Estudio Con Bodega](https://www.portalinmobiliario.com/MLC-2356200365-excelente-oportunidad-estudio-con-bodega-_JM) | 1,212 | $50,000,000 | 45 | 26.94 |  | 0 | $50,000 | 2026-10-20 |
| [Vendo Dpto 4d/3b Metro Plaza Armas Huérfanos (147830)](https://www.portalinmobiliario.com/MLC-4607519702-vendo-dpto-4d3b-metro-plaza-armas-huerfanos-147830-_JM) | 3,100 | $127,867,653 | 112 | 27.68 | 4 | 0 | $200,000 | 2026-10-21 |
| [Factibilidad Comercial \| 146 M2 \| 1er Piso  (107718)](https://www.portalinmobiliario.com/MLC-4599180860-factibilidad-comercial-146-m2-1er-piso-107718-_JM) | 4,100 | $169,115,283 | 146 | 28.08 | 3 | 1 | $0 | 2026-10-20 |
| [Cesión De Promesa De Cv De Depto Nuevo Entrega En Dic-2026](https://www.portalinmobiliario.com/MLC-4536724996-cesion-de-promesa-de-cv-de-depto-nuevo-entrega-en-dic-2026-_JM) | 1,800 | $74,245,734 | 64 | 28.12 | 2 | 1 |  | 2026-10-03 |
| [Oportunidad De Inversión En El Corazón De Santiago $65 Mm](https://www.portalinmobiliario.com/MLC-2378850569-oportunidad-de-inversion-en-el-corazon-de-santiago-65-mm-_JM) | 1,576 | $65,000,000 | 56 | 28.14 | 2 | 0 | $90,000 | nan |
| [Venta Departamento Remodelar 4d Centro Histórico - Santiago](https://www.portalinmobiliario.com/MLC-4625367366-venta-departamento-remodelar-4d-centro-historico-santiago-_JM) | 3,273 | $135,000,000 | 116 | 28.21 | 4 | 0 | $150,000 | 2026-10-06 |
| [Departamento Remodelado , 3d Y Terraza](https://www.portalinmobiliario.com/MLC-2374461871-departamento-remodelado-3d-y-terraza-_JM) | 2,250 | $92,807,168 | 78 | 28.85 | 3 | 0 | $44,000 | nan |
| [Oportunidad Inversionista: 3d/2b Santiago Centro (171236)](https://www.portalinmobiliario.com/MLC-4599180482-oportunidad-inversionista-3d2b-santiago-centro-171236-_JM) | 1,818 | $75,000,000 | 62 | 29.33 | 3 | 0 | $60,000 | 2026-08-21 |
| [Departamento Piso Completo, 2do Piso, Providencia 329](https://www.portalinmobiliario.com/MLC-2303304327-departamento-piso-completo-2do-piso-providencia-329-_JM) | 9,000 | $371,228,670 | 305 | 29.51 | 8 | 1 | $700,000 | 2026-10-08 |
| [Oportunidad Unica Precio Onfire En Santiago Centro](https://www.portalinmobiliario.com/MLC-2384947141-oportunidad-unica-precio-onfire-en-santiago-centro-_JM) | 1,960 | $80,845,355 | 66 | 29.70 | 3 | 0 | $110,000 | 2026-10-31 |
| [Venta Departamento 118 En Santiago](https://www.portalinmobiliario.com/MLC-4639915428-venta-departamento-118-en-santiago-_JM) | 3,515 | $145,000,000 | 118 | 29.79 | 3 | 0 | $100,000 | 2026-10-21 |
| [Departamento 2 Dortmitorios Mac Iver Con Moneda (180206)](https://www.portalinmobiliario.com/MLC-2370395365-departamento-2-dortmitorios-mac-iver-con-moneda-180206-_JM) | 1,818 | $75,000,000 | 61 | 29.81 | 2 | 0 | $75,000 | 2026-09-01 |
| [Venta Departamento 2hab 1ba Santiago](https://www.portalinmobiliario.com/MLC-4633576604-venta-departamento-2hab-1ba-santiago-_JM) | 1,818 | $75,000,000 | 60 | 30.30 | 2 | 0 | $70,000 | nan |
| [Depto 2 Dormitorios 2 Baños Vista Despejada Parque Los Reyes](https://www.portalinmobiliario.com/MLC-4620302012-depto-2-dormitorios-2-banos-vista-despejada-parque-los-reyes-_JM) | 1,818 | $74,988,191 | 60 | 30.30 | 2 | 0 | $125,000 | 2026-09-10 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (183263)](https://www.portalinmobiliario.com/MLC-4607517402-unico-3-dormitorios-bodega-metro-rondizzoni-183263-_JM) | 1,320 | $54,446,872 | 43 | 30.70 | 3 | 0 | $80,000 | 2026-09-01 |
| [Departamento  Santiago Centro  San Antonio / Oportunidad](https://www.portalinmobiliario.com/MLC-2358407495-departamento-santiago-centro-san-antonio-oportunidad-_JM) | 2,303 | $95,000,000 | 75 | 30.71 | 3 | 0 | $0 | 2026-09-30 |
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
