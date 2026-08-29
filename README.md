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
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4399815310-departamento-estudio-en-excelente-ubicacion-_JM) | 1,223 | $50,000,000 | 55 | 22.24 | 54 | 1 | 0 | $50 | 2026-08-25 |
| [Depto. Primer Piso, Tres Dormitorios, Estac. Compartido](https://www.portalinmobiliario.com/MLC-4417709810-depto-primer-piso-tres-dormitorios-estac-compartido-_JM) | 2,031 | $83,000,000 | 87 | 23.34 | 51 | 3 | 1 |  | 2026-08-28 |
| [Acogedor Departamento, Piso Doce Incluye Bodega](https://www.portalinmobiliario.com/MLC-4417963028-acogedor-departamento-piso-doce-incluye-bodega-_JM) | 1,762 | $72,000,000 | 65 | 27.10 | 53 | 1 | 0 | $95,000 | 2026-08-28 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2191909941-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,297 | $53,000,000 | 45 | 28.82 | 74 | 1 | 0 | $50,000 | 2026-08-25 |
| [Departamento San Francisco Id: 137511](https://www.portalinmobiliario.com/MLC-4423667560-departamento-san-francisco-id-137511-_JM) | 1,590 | $65,000,000 | 55 | 28.92 | 61 | 2 | 0 | $5,000 | 2026-08-29 |
| [Departamento En Santiago Argomedo Remate 24 Septiembre 2026](https://www.portalinmobiliario.com/MLC-4421196724-departamento-en-santiago-argomedo-remate-24-septiembre-2026-_JM) | 905 | $37,006,145 | 31 | 29.21 | 82 | 1 | 0 |  | 2026-08-28 |
| [Dúplex 87 M², 5 Terrazas, 2d, 2b, Metro O'higgins](https://www.portalinmobiliario.com/MLC-4397551728-duplex-87-m-5-terrazas-2d-2b-metro-ohiggins-_JM) | 2,569 | $105,000,000 | 87 | 29.53 | 55 | 2 | 0 |  | 2026-08-25 |
| [Liquido (176985)](https://www.portalinmobiliario.com/MLC-4418552946-liquido-176985-_JM) | 1,300 | $53,132,482 | 44 | 29.55 | 73 | 1 | 0 | $50,000 | 2026-08-28 |
| [Inersion ,comercial O Habutacional 2d/1b Maciver (180206)](https://www.portalinmobiliario.com/MLC-4397559286-inersion-comercial-o-habutacional-2d1b-maciver-180206-_JM) | 1,908 | $78,000,000 | 61 | 31.29 | 53 | 2 | 0 | $75,000 | 2026-08-25 |
| [Vendemos Departamento En Barrio Yungay,piso 17](https://www.portalinmobiliario.com/MLC-4410909834-vendemos-departamento-en-barrio-yungaypiso-17-_JM) | 1,346 | $55,000,000 | 43 | 31.30 | 66 | 1 | 0 | $50,000 | 2026-08-27 |
| [Luminoso Y Amplio Departamento Santiago](https://www.portalinmobiliario.com/MLC-2195804749-luminoso-y-amplio-departamento-santiago-_JM) | 3,060 | $125,065,688 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-26 |
| [Toesca, Bascuñan Con Terraza](https://www.portalinmobiliario.com/MLC-2193319145-toesca-bascunan-con-terraza-_JM) | 2,028 | $82,900,000 | 61 | 33.25 | 48 | 3 | 0 | $160,000 | 2026-08-26 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (166664)](https://www.portalinmobiliario.com/MLC-4419209280-unico-3-dormitorios-bodega-metro-rondizzoni-166664-_JM) | 1,450 | $59,263,153 | 43 | 33.72 | 72 | 3 | 0 | $80,000 | 2026-08-28 |
| [Oportunidad  En El Corazón De Santiago Venta O Arriendo](https://www.portalinmobiliario.com/MLC-4419782700-oportunidad-en-el-corazon-de-santiago-venta-o-arriendo-_JM) | 2,031 | $83,000,000 | 60 | 33.85 | 48 | 2 | 0 | $70,000 | 2026-08-28 |
| [Departamento Remodelado 2d1b Centro Historico](https://www.portalinmobiliario.com/MLC-2189298379-departamento-remodelado-2d1b-centro-historico-_JM) | 1,541 | $62,982,427 | 45 | 34.24 | 71 | 2 | 0 | $90,000 | 2026-08-25 |
| [Acogedor Departamento Libertad Con Presidente Balmaceda](https://www.portalinmobiliario.com/MLC-4391458976-acogedor-departamento-libertad-con-presidente-balmaceda-_JM) | 2,422 | $99,000,000 | 70 | 34.60 | 47 | 3 | 1 | $95,000 | 2026-08-23 |
| [Venta Departamento 2d Y 2b Frente A Parque Los Reyes](https://www.portalinmobiliario.com/MLC-2194370419-venta-departamento-2d-y-2b-frente-a-parque-los-reyes-_JM) | 1,837 | $75,080,284 | 53 | 34.66 | 47 | 2 | 0 | $0 | 2026-08-26 |
| [Oportunidad Venta Dpto Inversión](https://www.portalinmobiliario.com/MLC-2189299553-oportunidad-venta-dpto-inversion-_JM) | 1,321 | $54,000,000 | 38 | 34.77 | 66 | 2 | 0 | $60,000 | 2026-08-25 |
| [Departamento Arturo Prat (104322)](https://www.portalinmobiliario.com/MLC-4422465716-departamento-arturo-prat-104322-_JM) | 1,466 | $59,900,000 | 42 | 34.90 | 74 | 1 | 0 | $30,000 | 2026-08-29 |
| [Departamento General Bulnes Id: 135630](https://www.portalinmobiliario.com/MLC-4423667550-departamento-general-bulnes-id-135630-_JM) | 2,004 | $81,900,000 | 57 | 35.16 | 47 | 2 | 0 | $27,000 | 2026-08-29 |
| [Excelente Inversión En Pleno Centro (160833)](https://www.portalinmobiliario.com/MLC-4419427990-excelente-inversion-en-pleno-centro-160833-_JM) | 2,398 | $98,000,000 | 68 | 35.26 | 53 | 3 | 0 | $0 | 2026-08-28 |
| [Oportunidad Venta Depto 3d2b+est+bod Cerca Metro Franklin](https://www.portalinmobiliario.com/MLC-4405955940-oportunidad-venta-depto-3d2bestbod-cerca-metro-franklin-_JM) | 2,300 | $94,003,622 | 65 | 35.38 | 54 | 3 | 1 | $100,000 | 2026-08-26 |
| [Teatinos Piso De Parquet](https://www.portalinmobiliario.com/MLC-4414850548-teatinos-piso-de-parquet-_JM) | 3,328 | $136,000,000 | 94 | 35.40 | 56 | 3 | 0 | $120,000 | 2026-08-27 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4411470800-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,957 | $80,000,000 | 55 | 35.59 | 51 | 2 | 0 | $96,000 | 2026-08-27 |
| [Oportunidad Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2184927301-oportunidad-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,422 | $99,000,000 | 68 | 35.62 |  | 3 | 0 |  | 2026-08-23 |
| [¡oportunidad! 2d &#43; 1b &#43; Bodega, Zenteno, Santiago Ce](https://www.portalinmobiliario.com/MLC-2196882833-oportunidad-2d-43-1b-43-bodega-zenteno-santiago-ce-_JM) | 1,444 | $59,000,000 | 40 | 36.09 | 72 | 2 | 0 | $70,000 | 2026-08-27 |
| [San Antonio / Monjitas / Metro Bellas Artes](https://www.portalinmobiliario.com/MLC-4396273766-san-antonio-monjitas-metro-bellas-artes-_JM) | 1,300 | $53,132,482 | 36 | 36.11 | 73 | 1 | 0 | $70,000 | 2026-08-25 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2196894795-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,890 | $118,117,595 | 80 | 36.12 | 55 | 3 | 0 | $0 | 2026-08-27 |
| [Departamento Libertad Id: 158886](https://www.portalinmobiliario.com/MLC-4422153388-departamento-libertad-id-158886-_JM) | 2,320 | $94,821,045 | 64 | 36.25 | 47 | 3 | 0 | $65,000 | 2026-08-29 |
| [Duplex Stgo Centro 2d 1b - 62m2 - Metro - 2190uf](https://www.portalinmobiliario.com/MLC-2189069143-duplex-stgo-centro-2d-1b-62m2-metro-2190uf-_JM) | 2,190 | $89,507,797 | 60 | 36.50 | 51 | 2 | 0 | $130,000 | 2026-08-24 |
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
