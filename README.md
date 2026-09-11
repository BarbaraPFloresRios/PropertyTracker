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
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4457875472-departamento-estudio-en-excelente-ubicacion-_JM) | 1,223 | $50,000,000 | 55 | 22.23 | 54 | 1 | 0 | $50 | 2026-09-08 |
| [Metro Santa Ana-metro Plaza De Ar Vendo Depto 4d/3b Balcon](https://www.portalinmobiliario.com/MLC-2213140067-metro-santa-ana-metro-plaza-de-ar-vendo-depto-4d3b-balcon-_JM) | 3,350 | $137,000,000 | 143 | 23.43 | 62 | 4 | 0 | $0 | 2026-09-02 |
| [Departamento/3d1b/usach/estacion Central/planetario](https://www.portalinmobiliario.com/MLC-2212103597-departamento3d1busachestacion-centralplanetario-_JM) | 1,712 | $70,000,000 | 73 | 23.45 | 48 | 3 | 0 |  | 2026-09-02 |
| [Piso Completo Con Estilo Único En Avenida Brasil](https://www.portalinmobiliario.com/MLC-4460679066-piso-completo-con-estilo-unico-en-avenida-brasil-_JM) | 3,750 | $153,351,675 | 147 | 25.51 | 62 | 5 | 0 | $0 | 2026-09-09 |
| [Departamento Grande Pedro Lagos San Diego  (177976)](https://www.portalinmobiliario.com/MLC-4447964648-departamento-grande-pedro-lagos-san-diego-177976-_JM) | 1,800 | $73,608,804 | 70 | 25.71 | 54 | 2 | 0 | $40,000 | 2026-09-04 |
| [Se Vende Metro Cumming (90527)](https://www.portalinmobiliario.com/MLC-4457859102-se-vende-metro-cumming-90527-_JM) | 2,616 | $107,000,000 | 100 | 26.16 | 50 | 3 | 0 | $20,000 | 2026-09-08 |
| [Acogedor Depto. En Condomiino Residencial](https://www.portalinmobiliario.com/MLC-4437185782-acogedor-depto-en-condomiino-residencial-_JM) | 1,290 | $52,752,976 | 49 | 26.33 | 68 | 1 | 0 | $55,000 | 2026-09-01 |
| [Departamento Completamente Remodelado (144421)](https://www.portalinmobiliario.com/MLC-4445106614-departamento-completamente-remodelado-144421-_JM) | 1,650 | $67,474,737 | 60 | 27.50 | 54 | 2 | 0 | $15,000 | 2026-09-03 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-4457888424-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,296 | $53,000,000 | 45 | 28.80 | 74 | 1 | 0 | $50,000 | 2026-09-08 |
| [Departamento San Francisco Id: 137511](https://www.portalinmobiliario.com/MLC-4423667560-departamento-san-francisco-id-137511-_JM) | 1,590 | $65,000,000 | 55 | 28.90 | 61 | 2 | 0 | $5,000 | 2026-08-29 |
| [Departamento 1 Dormitorio - 1 Baño ( Santa Ana - Santiago )](https://www.portalinmobiliario.com/MLC-4443916618-departamento-1-dormitorio-1-bano-santa-ana-santiago--_JM) | 1,600 | $65,430,048 | 54 | 29.63 |  | 1 | 0 |  | 2026-09-03 |
| [Venta Departamento 118 M2 En Santiago](https://www.portalinmobiliario.com/MLC-4454839630-venta-departamento-118-m2-en-santiago-_JM) | 3,546 | $145,000,000 | 118 | 30.05 | 62 | 3 | 0 | $100,000 | 2026-09-07 |
| [Departamento A Pasos Metro](https://www.portalinmobiliario.com/MLC-4468493482-departamento-a-pasos-metro-_JM) | 2,739 | $112,000,000 | 90 | 30.43 | 55 | 4 | 1 | $75,000 | 2026-09-11 |
| [Oportunidad Para Remodelar Y Rentabilizar](https://www.portalinmobiliario.com/MLC-2213117975-oportunidad-para-remodelar-y-rentabilizar-_JM) | 1,880 | $76,880,306 | 60 | 31.33 | 53 | 2 | 0 | $80,000 | 2026-09-02 |
| [Departamento De Dos Dormitorios En Condominio Cerrado](https://www.portalinmobiliario.com/MLC-4449886610-departamento-de-dos-dormitorios-en-condominio-cerrado-_JM) | 2,200 | $89,966,316 | 70 | 31.43 | 48 | 2 | 0 | $75,000 | 2026-09-04 |
| [Amplio Y Céntrico Departamento](https://www.portalinmobiliario.com/MLC-2235126581-amplio-y-centrico-departamento-_JM) | 2,201 | $90,000,000 | 70 | 31.44 | 53 | 2 | 1 | $70,000 | 2026-09-11 |
| [Departamento En Venta De 3 Dorm. En Santiago, 2 Baños.](https://www.portalinmobiliario.com/MLC-4467066450-departamento-en-venta-de-3-dorm-en-santiago-2-banos-_JM) | 3,790 | $155,000,000 | 120 | 31.59 | 62 | 3 | 0 | $80,000 | 2026-09-10 |
| [A 2 Cuadras Metro Los Heroes -barrio Universitario](https://www.portalinmobiliario.com/MLC-2219180467-a-2-cuadras-metro-los-heroes-barrio-universitario-_JM) | 3,179 | $130,000,000 | 100 | 31.79 | 55 | 3 | 0 | $40,000 | 2026-09-05 |
| [Venta Departamento 2hab 2ba Santiago](https://www.portalinmobiliario.com/MLC-4456988782-venta-departamento-2hab-2ba-santiago-_JM) | 2,250 | $92,000,000 | 70 | 32.14 | 51 | 2 | 0 | $80,000 | 2026-09-08 |
| [Venta Depto. 3d/1b Piso De Parquet Centro Histórico De Stgo](https://www.portalinmobiliario.com/MLC-2219777579-venta-depto-3d1b-piso-de-parquet-centro-historico-de-stgo-_JM) | 2,715 | $111,026,613 | 84 | 32.32 | 53 | 3 | 0 | $30,000 | 2026-09-05 |
| [Venta Depto  Av Club Hípico  Excte Conectividad Y Entorno](https://www.portalinmobiliario.com/MLC-4451785758-venta-depto-av-club-hipico-excte-conectividad-y-entorno-_JM) | 3,060 | $125,134,967 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-09-06 |
| [Oferta (174950)](https://www.portalinmobiliario.com/MLC-4465529118-oferta-174950-_JM) | 1,956 | $80,000,000 | 60 | 32.60 | 48 | 2 | 0 | $93,000 | 2026-09-10 |
| [Departamento San Antonio Id: 150326](https://www.portalinmobiliario.com/MLC-4441938264-departamento-san-antonio-id-150326-_JM) | 1,956 | $80,000,000 | 60 | 32.60 | 53 | 1 | 0 | $0 | 2026-09-02 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4441913752-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 1,600 | $65,430,048 | 49 | 32.65 | 72 | 3 | 1 | $80,000 | 2026-09-02 |
| [Departamento 2 Dormitorios En Condominio Cerrado. Santiago](https://www.portalinmobiliario.com/MLC-4428241946-departamento-2-dormitorios-en-condominio-cerrado-santiago-_JM) | 1,800 | $73,608,804 | 55 | 32.73 | 47 | 2 | 0 | $55,000 | 2026-08-30 |
| [Vendo Dpto En Santiago 2d 2b](https://www.portalinmobiliario.com/MLC-2217013745-vendo-dpto-en-santiago-2d-2b-_JM) | 3,277 | $134,000,000 | 100 | 32.77 | 53 | 2 | 0 | $80,000 | 2026-09-04 |
| [Se Vende Depto. Recién Remodelado](https://www.portalinmobiliario.com/MLC-4454057412-se-vende-depto-recien-remodelado-_JM) | 2,300 | $94,055,694 | 70 | 32.86 | 68 | 3 | 0 | $95,000 | 2026-09-07 |
| [Dpto Enventa Manuel De Amat 3d 1b $78.000.000 (139829)](https://www.portalinmobiliario.com/MLC-4462120188-dpto-enventa-manuel-de-amat-3d-1b-78000000-139829-_JM) | 1,907 | $78,000,000 | 58 | 32.89 | 53 | 3 | 0 | $0 | 2026-09-09 |
| [Cómodo Departamento 2 Dor 1 Baño Calle Zenteno](https://www.portalinmobiliario.com/MLC-4467059908-comodo-departamento-2-dor-1-bano-calle-zenteno-_JM) | 1,490 | $60,931,732 | 45 | 33.11 | 72 | 2 | 0 | $0 | 2026-09-10 |
| [Santiago Centro \| Depto 107 M2 Para Remodelar A Tu Gusto](https://www.portalinmobiliario.com/MLC-4449886118-santiago-centro-depto-107-m2-para-remodelar-a-tu-gusto-_JM) | 3,550 | $145,172,919 | 107 | 33.18 | 73 | 3 | 0 |  | 2026-09-04 |
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
