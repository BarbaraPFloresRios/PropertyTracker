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
| [Departamento - Santiago Centro 54 M2](https://www.portalinmobiliario.com/MLC-4380420442-departamento-santiago-centro-54-m2-_JM) | 1,225 | $50,063,912 | 54 | 22.69 | 53 | 2 | 0 |  | 2026-08-21 |
| [Venta Departamento Santiago De 3 Dorm 2 Baños Antiguo Piso 1](https://www.portalinmobiliario.com/MLC-4382357728-venta-departamento-santiago-de-3-dorm-2-banos-antiguo-piso-1-_JM) | 2,692 | $110,000,000 | 94 | 28.63 | 55 | 3 | 0 | $68,000 | 2026-08-21 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2191909941-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,297 | $53,000,000 | 45 | 28.82 | 74 | 1 | 0 | $50,000 | 2026-08-25 |
| [Cumming 1350 ,excelente Depto 2 D 2 B  (82859)](https://www.portalinmobiliario.com/MLC-2183115821-cumming-1350-excelente-depto-2-d-2-b-82859-_JM) | 2,000 | $81,737,000 | 68 | 29.41 | 47 | 2 | 0 | $90,000 | 2026-08-22 |
| [Dúplex 87 M², 5 Terrazas, 2d, 2b, Metro O'higgins](https://www.portalinmobiliario.com/MLC-4397551728-duplex-87-m-5-terrazas-2d-2b-metro-ohiggins-_JM) | 2,569 | $105,000,000 | 87 | 29.53 |  | 2 |  |  | 2026-08-25 |
| [Departamento 2hab 1ba Cercano A Estación De Metro](https://www.portalinmobiliario.com/MLC-4375123120-departamento-2hab-1ba-cercano-a-estacion-de-metro-_JM) | 1,835 | $75,000,000 | 60 | 30.59 | 65 | 2 | 0 | $70,000 | 2026-08-20 |
| [Rebajado Por Viaje, 2500uf!](https://www.portalinmobiliario.com/MLC-2179291421-rebajado-por-viaje-2500uf-_JM) | 2,500 | $102,171,250 | 81 | 30.86 |  | 3 | 0 |  | 2026-08-21 |
| [Inersion ,comercial O Habutacional 2d/1b Maciver (180206)](https://www.portalinmobiliario.com/MLC-4397559286-inersion-comercial-o-habutacional-2d1b-maciver-180206-_JM) | 1,909 | $78,000,000 | 61 | 31.29 | 53 | 2 | 0 | $75,000 | 2026-08-25 |
| [Vendemos Departamento En Barrio Yungay,piso 17](https://www.portalinmobiliario.com/MLC-4410909834-vendemos-departamento-en-barrio-yungaypiso-17-_JM) | 1,346 | $55,000,000 | 43 | 31.30 | 66 | 1 | 0 | $50,000 | 2026-08-27 |
| [Luminoso Y Amplio Departamento Santiago](https://www.portalinmobiliario.com/MLC-2195804749-luminoso-y-amplio-departamento-santiago-_JM) | 3,060 | $125,057,610 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-26 |
| [Toesca, Bascuñan Con Terraza](https://www.portalinmobiliario.com/MLC-2193319145-toesca-bascunan-con-terraza-_JM) | 2,028 | $82,900,000 | 61 | 33.25 | 48 | 3 | 0 | $160,000 | 2026-08-26 |
| [Departamento San Pablo Id: 178314](https://www.portalinmobiliario.com/MLC-2179806003-departamento-san-pablo-id-178314-_JM) | 1,670 | $68,250,395 | 50 | 33.40 | 71 | 1 | 0 | $90,000 | 2026-08-21 |
| [Departamento 3 Dormitorios Cerca De Futura Estación De Metro](https://www.portalinmobiliario.com/MLC-4381518820-departamento-3-dormitorios-cerca-de-futura-estacion-de-metro-_JM) | 2,200 | $89,910,700 | 65 | 33.85 | 47 | 3 | 0 | $100,000 | 2026-08-21 |
| [Oportunidad 2d-2b 52m2](https://www.portalinmobiliario.com/MLC-2180372065-oportunidad-2d-2b-52m2-_JM) | 1,713 | $70,000,000 | 50 | 34.26 | 82 | 2 | 0 | $80,000 | 2026-08-21 |
| [Vendo Amplio Depto  3dorm 2ba Santiago Centro](https://www.portalinmobiliario.com/MLC-4375125666-vendo-amplio-depto-3dorm-2ba-santiago-centro-_JM) | 2,398 | $98,000,000 | 70 | 34.26 | 53 | 3 | 0 | $85,000 | 2026-08-20 |
| [Acogedor Departamento Libertad Con Presidente Balmaceda](https://www.portalinmobiliario.com/MLC-4391458976-acogedor-departamento-libertad-con-presidente-balmaceda-_JM) | 2,422 | $99,000,000 | 70 | 34.61 | 47 | 3 | 1 | $95,000 | 2026-08-23 |
| [Venta Departamento 2d Y 2b Frente A Parque Los Reyes](https://www.portalinmobiliario.com/MLC-2194370419-venta-departamento-2d-y-2b-frente-a-parque-los-reyes-_JM) | 1,837 | $75,075,434 | 53 | 34.66 | 47 | 2 | 0 | $0 | 2026-08-26 |
| [Oportunidad Venta Dpto Inversión](https://www.portalinmobiliario.com/MLC-2189299553-oportunidad-venta-dpto-inversion-_JM) | 1,321 | $54,000,000 | 38 | 34.77 | 66 | 2 | 0 | $60,000 | 2026-08-25 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2183099611-metro-parque-ohiggins-_JM) | 1,690 | $69,067,765 | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-22 |
| [Departamento Remodelado 2d1b Centro Historico](https://www.portalinmobiliario.com/MLC-2189298379-departamento-remodelado-2d1b-centro-historico-_JM) | 1,590 | $64,980,915 | 45 | 35.33 | 71 | 2 | 0 | $90,000 | 2026-08-25 |
| [Cómodo Departamento En Quinta Normal](https://www.portalinmobiliario.com/MLC-2181839211-comodo-departamento-en-quinta-normal-_JM) | 1,805 | $73,750,000 | 51 | 35.38 | 68 | 3 | 0 | $80,000 | 2026-08-22 |
| [Oportunidad Venta Depto 3d2b+est+bod Cerca Metro Franklin](https://www.portalinmobiliario.com/MLC-4405955940-oportunidad-venta-depto-3d2bestbod-cerca-metro-franklin-_JM) | 2,300 | $93,997,550 | 65 | 35.38 | 54 | 3 | 1 | $100,000 | 2026-08-26 |
| [Teatinos Piso De Parquet](https://www.portalinmobiliario.com/MLC-4414850548-teatinos-piso-de-parquet-_JM) | 3,328 | $136,000,000 | 94 | 35.40 | 56 | 3 | 0 | $120,000 | 2026-08-27 |
| [Hermoso Depto 3d Y Estacionmiento En Nataniel Cox](https://www.portalinmobiliario.com/MLC-4385505918-hermoso-depto-3d-y-estacionmiento-en-nataniel-cox-_JM) | 1,737 | $71,000,000 | 49 | 35.46 | 72 | 3 | 1 | $70,000 | 2026-08-22 |
| [Se Vende Cercano Al Metro 107 Mt 3d 2 B (176461)](https://www.portalinmobiliario.com/MLC-2183956043-se-vende-cercano-al-metro-107-mt-3d-2-b-176461-_JM) | 3,303 | $135,000,000 | 93 | 35.52 | 49 | 3 | 0 | $0 | 2026-08-22 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4411470800-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,958 | $80,000,000 | 55 | 35.59 | 51 | 2 | 0 | $96,000 | 2026-08-27 |
| [Oportunidad Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2184927301-oportunidad-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,422 | $99,000,000 | 68 | 35.62 |  | 3 | 0 |  | 2026-08-23 |
| [Departamento Aldunate Id: 178552](https://www.portalinmobiliario.com/MLC-2177117803-departamento-aldunate-id-178552-_JM) | 1,786 | $73,000,000 | 50 | 35.72 | 71 | 3 | 0 | $0 | 2026-08-20 |
| [Acogedor Departamento 2d Con Vista Despejada En Santiago](https://www.portalinmobiliario.com/MLC-2179249535-acogedor-departamento-2d-con-vista-despejada-en-santiago-_JM) | 1,762 | $72,000,000 | 49 | 35.95 | 74 | 2 | 0 | $61,000 | 2026-08-21 |
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
