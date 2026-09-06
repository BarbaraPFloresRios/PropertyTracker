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
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2210033553-departamento-estudio-en-excelente-ubicacion-_JM) | 1,223 | $50,000,000 | 55 | 22.24 | 54 | 1 | 0 | $50 | 2026-09-01 |
| [Depto. Primer Piso, Tres Dormitorios, Estac. Compartido](https://www.portalinmobiliario.com/MLC-4417709810-depto-primer-piso-tres-dormitorios-estac-compartido-_JM) | 2,030 | $83,000,000 | 87 | 23.34 | 51 | 3 | 1 |  | 2026-08-28 |
| [Metro Santa Ana-metro Plaza De Ar Vendo Depto 4d/3b Balcon](https://www.portalinmobiliario.com/MLC-2213140067-metro-santa-ana-metro-plaza-de-ar-vendo-depto-4d3b-balcon-_JM) | 3,351 | $137,000,000 | 143 | 23.43 | 62 | 4 | 0 | $0 | 2026-09-02 |
| [Departamento/3d1b/usach/estacion Central/planetario](https://www.portalinmobiliario.com/MLC-2212103597-departamento3d1busachestacion-centralplanetario-_JM) | 1,712 | $70,000,000 | 73 | 23.46 | 48 | 3 | 0 |  | 2026-09-02 |
| [Departamento Antiguo (176985)](https://www.portalinmobiliario.com/MLC-4418552946-departamento-antiguo-176985-_JM) | 1,100 | $44,968,396 | 44 | 25.00 | 73 | 1 | 0 | $50,000 | 2026-08-28 |
| [Departamento San Isidro Id: 178800](https://www.portalinmobiliario.com/MLC-4410875824-departamento-san-isidro-id-178800-_JM) | 2,650 | $108,332,954 | 104 | 25.48 | 73 | 4 | 0 | $0 | 2026-08-27 |
| [Departamento Grande Pedro Lagos San Diego  (177976)](https://www.portalinmobiliario.com/MLC-4447964648-departamento-grande-pedro-lagos-san-diego-177976-_JM) | 1,800 | $73,584,648 | 70 | 25.71 | 54 | 2 | 0 | $40,000 | 2026-09-04 |
| [Acogedor Depto. En Condomiino Residencial](https://www.portalinmobiliario.com/MLC-4437185782-acogedor-depto-en-condomiino-residencial-_JM) | 1,290 | $52,735,664 | 49 | 26.33 | 68 | 1 | 0 | $55,000 | 2026-09-01 |
| [Acogedor Departamento, Piso Doce Incluye Bodega](https://www.portalinmobiliario.com/MLC-4417963028-acogedor-departamento-piso-doce-incluye-bodega-_JM) | 1,761 | $72,000,000 | 65 | 27.10 | 53 | 1 | 0 | $95,000 | 2026-08-28 |
| [Departamento Completamente Remodelado (144421)](https://www.portalinmobiliario.com/MLC-4445106614-departamento-completamente-remodelado-144421-_JM) | 1,650 | $67,452,594 | 60 | 27.50 | 54 | 2 | 0 | $15,000 | 2026-09-03 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2210033561-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,296 | $53,000,000 | 45 | 28.81 | 74 | 1 | 0 | $50,000 | 2026-09-01 |
| [Departamento San Francisco Id: 137511](https://www.portalinmobiliario.com/MLC-4423667560-departamento-san-francisco-id-137511-_JM) | 1,590 | $65,000,000 | 55 | 28.91 | 61 | 2 | 0 | $5,000 | 2026-08-29 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2191204811-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 4,282 | $175,049,702 | 148 | 28.93 |  | 3 |  |  | 2026-08-25 |
| [Departamento En Santiago Argomedo Remate 24 Septiembre 2026](https://www.portalinmobiliario.com/MLC-4421196724-departamento-en-santiago-argomedo-remate-24-septiembre-2026-_JM) | 905 | $37,006,145 | 31 | 29.20 | 82 | 1 | 0 |  | 2026-08-28 |
| [Dúplex 87 M², 5 Terrazas, 2d, 2b, Metro O'higgins](https://www.portalinmobiliario.com/MLC-4397551728-duplex-87-m-5-terrazas-2d-2b-metro-ohiggins-_JM) | 2,568 | $105,000,000 | 87 | 29.52 | 55 | 2 | 0 |  | 2026-08-25 |
| [Departamento 1 Dormitorio - 1 Baño ( Santa Ana - Santiago )](https://www.portalinmobiliario.com/MLC-4443916618-departamento-1-dormitorio-1-bano-santa-ana-santiago--_JM) | 1,600 | $65,408,576 | 54 | 29.63 |  | 1 | 0 |  | 2026-09-03 |
| [Metro Santa Lucia Amplio](https://www.portalinmobiliario.com/MLC-4401223046-metro-santa-lucia-amplio-_JM) | 4,300 | $175,785,548 | 145 | 29.66 | 62 | 7 | 0 | $200,000 | 2026-08-26 |
| [Venta Departamento 118 M2 En Santiago](https://www.portalinmobiliario.com/MLC-2198147163-venta-departamento-118-m2-en-santiago-_JM) | 3,547 | $145,000,000 | 118 | 30.06 | 62 | 3 | 0 | $100,000 | 2026-08-27 |
| [Departamento En Venta De 4 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4411470812-departamento-en-venta-de-4-dorm-en-santiago-_JM) | 4,200 | $171,697,512 | 138 | 30.43 | 64 | 4 | 0 | $180,000 | 2026-08-27 |
| [Departamento En Venta De 4 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4411457616-departamento-en-venta-de-4-dorm-en-santiago-_JM) | 4,200 | $171,697,512 | 138 | 30.43 | 64 | 4 | 0 | $170,000 | 2026-08-27 |
| [Venta Departamento 2hab 1ba Cercano A Estación De Metro](https://www.portalinmobiliario.com/MLC-4433068006-venta-departamento-2hab-1ba-cercano-a-estacion-de-metro-_JM) | 1,835 | $75,000,000 | 60 | 30.58 | 65 | 2 | 0 | $70,000 | 2026-08-31 |
| [Inersion ,comercial O Habutacional 2d/1b Maciver (180206)](https://www.portalinmobiliario.com/MLC-4397559286-inersion-comercial-o-habutacional-2d1b-maciver-180206-_JM) | 1,908 | $78,000,000 | 61 | 31.28 | 53 | 2 | 0 | $75,000 | 2026-08-25 |
| [Vendemos Departamento En Barrio Yungay,piso 17](https://www.portalinmobiliario.com/MLC-4410909834-vendemos-departamento-en-barrio-yungaypiso-17-_JM) | 1,345 | $55,000,000 | 43 | 31.29 | 66 | 1 | 0 | $50,000 | 2026-08-27 |
| [Oportunidad Para Remodelar Y Rentabilizar](https://www.portalinmobiliario.com/MLC-2213117975-oportunidad-para-remodelar-y-rentabilizar-_JM) | 1,880 | $76,855,077 | 60 | 31.33 | 53 | 2 | 0 | $80,000 | 2026-09-02 |
| [Departamento De Dos Dormitorios En Condominio Cerrado](https://www.portalinmobiliario.com/MLC-4449886610-departamento-de-dos-dormitorios-en-condominio-cerrado-_JM) | 2,200 | $89,936,792 | 70 | 31.43 | 48 | 2 | 0 | $75,000 | 2026-09-04 |
| [Departamento En Venta De 3 Dorm. En Santiago, 2 Baños.](https://www.portalinmobiliario.com/MLC-2216002145-departamento-en-venta-de-3-dorm-en-santiago-2-banos-_JM) | 3,792 | $155,000,000 | 120 | 31.60 | 62 | 3 | 0 | $80,000 | 2026-09-04 |
| [A 2 Cuadras Metro Los Heroes -barrio Universitario](https://www.portalinmobiliario.com/MLC-2219180467-a-2-cuadras-metro-los-heroes-barrio-universitario-_JM) | 3,180 | $130,000,000 | 100 | 31.80 | 55 | 3 | 0 | $40,000 | 2026-09-05 |
| [Venta Depto. 3d/1b Piso De Parquet Centro Histórico De Stgo](https://www.portalinmobiliario.com/MLC-2219777579-venta-depto-3d1b-piso-de-parquet-centro-historico-de-stgo-_JM) | 2,715 | $110,990,177 | 84 | 32.32 | 53 | 3 | 0 | $30,000 | 2026-09-05 |
| [Luminoso Y Amplio Departamento Santiago](https://www.portalinmobiliario.com/MLC-2195804749-luminoso-y-amplio-departamento-santiago-_JM) | 3,060 | $125,093,902 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-26 |
| [Departamento San Antonio Id: 150326](https://www.portalinmobiliario.com/MLC-4441938264-departamento-san-antonio-id-150326-_JM) | 1,957 | $80,000,000 | 60 | 32.62 | 53 | 1 | 0 | $0 | 2026-09-02 |
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
