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
| [Depto / Metro Los Leones](https://www.portalinmobiliario.com/MLC-4198200752-depto-metro-los-leones-_JM) | 4,500 | $183,801,555 | 93 | 48.39 | 94 | 3 | 0 | $155,000 | 2026-07-18 |
| [Vendo Departamento  Antonio Varas Providencia 2 Dorm](https://www.portalinmobiliario.com/MLC-4105556362-vendo-departamento-antonio-varas-providencia-2-dorm-_JM) | 4,300 |  | 87 | 49.43 | 94 | 2 | 0 | $50,000 | 2026-07-21 |
| [Depto 4 Dormitorios, 2 Baños, 90 M2 (75040)](https://www.portalinmobiliario.com/MLC-4209724852-depto-4-dormitorios-2-banos-90-m2-75040-_JM) | 4,990 |  | 90 | 55.44 | 94 | 4 | 0 | $120,000 | 2026-07-20 |
| [Andrés De Fuenzalida (piso 7)](https://www.portalinmobiliario.com/MLC-4211492140-andres-de-fuenzalida-piso-7-_JM) | 5,200 |  | 85 | 61.18 |  | 3 |  |  | 2026-07-21 |
| [Andrés De Fuenzalida (remodelado Completo)](https://www.portalinmobiliario.com/MLC-4210790912-andres-de-fuenzalida-remodelado-completo-_JM) | 5,200 |  | 85 | 61.18 | 94 | 3 | 0 | $115,000 | 2026-07-21 |
| [Primer Piso Con Jardin Propio Ideal Para Remodelar](https://www.portalinmobiliario.com/MLC-4208897282-primer-piso-con-jardin-propio-ideal-para-remodelar-_JM) | 5,600 |  | 86 | 65.12 | 85 | 3 | 1 | $100,000 | 2026-07-20 |
| [Conectividad Y Confort Garantizados (170733)](https://www.portalinmobiliario.com/MLC-4198492680-conectividad-y-confort-garantizados-170733-_JM) | 4,300 |  | 65 | 66.15 | 84 | 2 | 0 | $0 | 2026-07-17 |
| [Espacioso Y Luminoso En Excelente Ubicación (176324)](https://www.portalinmobiliario.com/MLC-2074126301-espacioso-y-luminoso-en-excelente-ubicacion-176324-_JM) | 5,000 |  | 75 | 66.67 | 98 | 3 | 1 | $80,000 | 2026-07-21 |
| [Lindo Departamento En Juana  De  Lestonac Providencia](https://www.portalinmobiliario.com/MLC-4201707636-lindo-departamento-en-juana-de-lestonac-providencia-_JM) | 4,294 |  | 61 | 70.39 | 82 | 2 | 0 | $50,000 | 2026-07-18 |
| [Venta Dpto Remodelado 3dormitorios 2baños Estacionamiento](https://www.portalinmobiliario.com/MLC-4201744688-venta-dpto-remodelado-3dormitorios-2banos-estacionamiento-_JM) | 6,690 | $273,251,645 | 94 | 71.17 | 138 | 3 | 1 | $180,000 | 2026-07-18 |
| [Andres De Fuenzalida, Remodelado](https://www.portalinmobiliario.com/MLC-2068828621-andres-de-fuenzalida-remodelado-_JM) | 6,100 |  | 85 | 71.76 | 94 | 3 | 0 | $100,000 | 2026-07-18 |
| [Remodelado 2d/2b \| Barrio Italia \| Metro Parque Bustamante](https://www.portalinmobiliario.com/MLC-2039832321-remodelado-2d2b-barrio-italia-metro-parque-bustamante-_JM) | 5,800 |  | 80 | 72.50 |  | 2 | 1 |  | 2026-07-17 |
| [Oportunidad Remodelado A Pasos Del Metro](https://www.portalinmobiliario.com/MLC-4201707202-oportunidad-remodelado-a-pasos-del-metro-_JM) | 6,190 |  | 85 | 72.82 | 94 | 2 | 0 | $140,000 | 2026-07-18 |
| [Amplio Studio 42m2 Ubicacion Excepcional  (170799)](https://www.portalinmobiliario.com/MLC-4198492614-amplio-studio-42m2-ubicacion-excepcional-170799-_JM) | 3,100 |  | 42 | 73.81 | 112 | 1 | 0 | $50,000 | 2026-07-17 |
| [Suecia Amplio Depto 70 M2 \| 1d Suite \| 2e + 2b \| Providencia](https://www.portalinmobiliario.com/MLC-2073964391-suecia-amplio-depto-70-m2-1d-suite-2e-2b-providencia-_JM) | 5,200 |  | 70 | 74.29 | 98 | 1 | 2 | $220,000 | 2026-07-21 |
| [Remodelado De 2 Dormitorios En Clasico Barrio De Providencia](https://www.portalinmobiliario.com/MLC-4211822678-remodelado-de-2-dormitorios-en-clasico-barrio-de-providencia-_JM) | 5,550 |  | 74 | 75.00 | 98 | 2 | 0 | $25,000 | 2026-07-21 |
| [Venta De Departamento De 3 Dormitorios.sector Parque Ines De](https://www.portalinmobiliario.com/MLC-4201743910-venta-de-departamento-de-3-dormitoriossector-parque-ines-de-_JM) | 6,500 |  | 84 | 77.38 | 85 | 3 | 1 | $160,000 | 2026-07-18 |
| [Vive Con Comodidad Y Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4198197136-vive-con-comodidad-y-excelente-ubicacion-_JM) | 4,800 |  | 62 | 77.42 | 68 | 2 | 1 | $200,000 | 2026-07-18 |
| [Providencia, Buscamos Departamentos](https://www.portalinmobiliario.com/MLC-4201705404-providencia-buscamos-departamentos-_JM) | 5,500 |  | 70 | 78.57 | 112 | 2 | 1 | $11,111 | 2026-07-18 |
| [Grace Kelm Vende Espacioso Depto Gran Terraza De 3 Dorm Y 3](https://www.portalinmobiliario.com/MLC-4201706426-grace-kelm-vende-espacioso-depto-gran-terraza-de-3-dorm-y-3-_JM) | 7,200 |  | 90 | 80.00 | 94 | 3 | 1 | $125,000 | 2026-07-18 |
| [Remodelado Duplex De 2d2b A Pasos De Metro Manuel Montt](https://www.portalinmobiliario.com/MLC-2070925703-remodelado-duplex-de-2d2b-a-pasos-de-metro-manuel-montt-_JM) | 7,200 |  | 90 | 80.00 | 94 | 2 | 0 | $40,000 | 2026-07-19 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4206489696-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 7,499 |  | 92 | 81.51 | 94 | 3 | 1 | $150,000 | 2026-07-20 |
| [Excelente Departamento Metro Manuel Montt (171371)](https://www.portalinmobiliario.com/MLC-2071198175-excelente-departamento-metro-manuel-montt-171371-_JM) | 6,290 |  | 76 | 82.76 | 84 | 2 | 1 | $180,000 | 2026-07-19 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4143962996-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 7,750 | $316,547,122 | 93 | 83.33 |  | 3 | 1 |  | 2026-07-20 |
| [Departamento Metro Los Leones 2d 2b Y Estacionamiento](https://www.portalinmobiliario.com/MLC-4209022406-departamento-metro-los-leones-2d-2b-y-estacionamiento-_JM) | 4,850 |  | 58 | 83.62 | 98 | 2 | 1 | $230,000 | 2026-07-20 |
| [Remodelado, Vista Norte, Dos Dormitorios Estacionamiento](https://www.portalinmobiliario.com/MLC-2068821979-remodelado-vista-norte-dos-dormitorios-estacionamiento-_JM) | 4,950 |  | 59 | 83.90 | 68 | 2 | 1 | $80,000 | 2026-07-19 |
| [Hermoso Depto En Venta En Providencia](https://www.portalinmobiliario.com/MLC-2069547893-hermoso-depto-en-venta-en-providencia-_JM) | 5,900 |  | 70 | 84.29 | 98 | 2 | 1 | $89,000 | 2026-07-19 |
| [Metro Ines De Suarez / Providencia](https://www.portalinmobiliario.com/MLC-2074074503-metro-ines-de-suarez-providencia-_JM) | 7,300 |  | 86 | 84.88 | 85 | 2 | 0 | $160,000 | 2026-07-21 |
| [En Venta \| Departamento Con Gran Potencial En Plaza Las Lila](https://www.portalinmobiliario.com/MLC-4201732136-en-venta-departamento-con-gran-potencial-en-plaza-las-lila-_JM) | 6,800 |  | 80 | 85.00 | 95 | 2 | 1 | $190,000 | 2026-07-18 |
| [Providencia 3d+2b+dorm. Serv+b+e+bod. Las Lilas](https://www.portalinmobiliario.com/MLC-4155685302-providencia-3d2bdorm-servbebod-las-lilas-_JM) | 7,990 |  | 94 | 85.00 |  | 4 | 1 |  | 2026-07-18 |
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
