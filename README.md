# PropertyTracker

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 7 days (under 100 m²). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Zona UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Depto / Metro Los Leones](https://www.portalinmobiliario.com/MLC-4198200752-depto-metro-los-leones-_JM) | 4,500 | $183,801,555 | 93 | 48.39 | 94 | 3 | 0 | $155,000 | 2026-07-18 |
| [Metro Santa Isabel / 3 Dormitorios 2 Baños](https://www.portalinmobiliario.com/MLC-4198500546-metro-santa-isabel-3-dormitorios-2-banos-_JM) | 4,200 |  | 85 | 49.41 | 73 | 3 | 0 | $30,000 | 2026-07-18 |
| [Vendo Departamento  Antonio Varas Providencia 2 Dorm](https://www.portalinmobiliario.com/MLC-4105556362-vendo-departamento-antonio-varas-providencia-2-dorm-_JM) | 4,300 |  | 87 | 49.43 | 94 | 2 | 0 | $50,000 | 2026-07-21 |
| [Metro Pedro De Valdivia A 5 Min - Dpto 4 Dormitorios - 90m2](https://www.portalinmobiliario.com/MLC-1966055801-metro-pedro-de-valdivia-a-5-min-dpto-4-dormitorios-90m2-_JM) | 4,580 |  | 90 | 50.89 | 94 | 4 | 0 | $120,000 | 2026-07-21 |
| [Depto 4 Dormitorios, 2 Baños, 90 M2 (75040)](https://www.portalinmobiliario.com/MLC-4209724852-depto-4-dormitorios-2-banos-90-m2-75040-_JM) | 4,990 |  | 90 | 55.44 | 94 | 4 | 0 | $120,000 | 2026-07-20 |
| [Venta Depto 3 Habitaciones 2 Baños - Metro Los Leones (5301)](https://www.portalinmobiliario.com/MLC-4203939854-venta-depto-3-habitaciones-2-banos-metro-los-leones-5301-_JM) | 4,600 |  | 79 | 58.23 | 94 | 3 | 0 | $180,000 | 2026-07-19 |
| [Departamento En Venta De 4 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4146254574-departamento-en-venta-de-4-dorm-en-providencia-_JM) | 5,400 | $220,561,866 | 92 | 58.70 | 80 | 4 | 0 | $100,000 | 2026-07-20 |
| [Departamento En Venta De 4 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-3960426866-departamento-en-venta-de-4-dorm-en-providencia-_JM) | 5,500 |  | 90 | 61.11 | 94 | 4 | 0 | $110,000 | 2026-07-19 |
| [Andrés De Fuenzalida (piso 7)](https://www.portalinmobiliario.com/MLC-4211492140-andres-de-fuenzalida-piso-7-_JM) | 5,200 |  | 85 | 61.18 |  | 3 |  |  | 2026-07-21 |
| [Andrés De Fuenzalida (remodelado Completo)](https://www.portalinmobiliario.com/MLC-4210790912-andres-de-fuenzalida-remodelado-completo-_JM) | 5,200 |  | 85 | 61.18 | 94 | 3 | 0 | $115,000 | 2026-07-21 |
| [Duplex Remodelado En Venta En Providencia](https://www.portalinmobiliario.com/MLC-3578657700-duplex-remodelado-en-venta-en-providencia-_JM) | 5,990 |  | 94 | 63.72 | 94 | 3 | 1 | $130,000 | 2026-07-21 |
| [Primer Piso Con Jardin Propio Ideal Para Remodelar](https://www.portalinmobiliario.com/MLC-4208897282-primer-piso-con-jardin-propio-ideal-para-remodelar-_JM) | 5,600 |  | 86 | 65.12 | 85 | 3 | 1 | $100,000 | 2026-07-20 |
| [Conectividad Y Confort Garantizados (170733)](https://www.portalinmobiliario.com/MLC-4198492680-conectividad-y-confort-garantizados-170733-_JM) | 4,300 |  | 65 | 66.15 | 84 | 2 | 0 | $0 | 2026-07-17 |
| [Cercano A Colegios:  Mariano, Sagrados Corazones, Regina Pac](https://www.portalinmobiliario.com/MLC-4198327076-cercano-a-colegios-mariano-sagrados-corazones-regina-pac-_JM) | 4,900 | $200,139,471 | 74 | 66.22 | 84 | 3 | 1 | $57,000 | 2026-07-18 |
| [Cercano A Colegios:  Mariano, Sagrados Corazones, Regina Pac](https://www.portalinmobiliario.com/MLC-4210801820-cercano-a-colegios-mariano-sagrados-corazones-regina-pac-_JM) | 4,900 |  | 74 | 66.22 | 84 | 3 | 1 | $57,000 | 2026-07-21 |
| [Espacioso Y Luminoso En Excelente Ubicación (176324)](https://www.portalinmobiliario.com/MLC-2074126301-espacioso-y-luminoso-en-excelente-ubicacion-176324-_JM) | 5,000 |  | 75 | 66.67 | 98 | 3 | 1 | $80,000 | 2026-07-21 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-3773172372-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 5,990 |  | 86 | 69.65 | 95 | 3 | 0 | $80,000 | 2026-07-21 |
| [Venta Depto Santiago Centro 3 Dorm Y 3 Baños Providencia](https://www.portalinmobiliario.com/MLC-4198325742-venta-depto-santiago-centro-3-dorm-y-3-banos-providencia-_JM) | 6,290 |  | 90 | 69.89 | 80 | 3 | 0 | $130,000 | 2026-07-18 |
| [Lindo Departamento En Juana  De  Lestonac Providencia](https://www.portalinmobiliario.com/MLC-4201707636-lindo-departamento-en-juana-de-lestonac-providencia-_JM) | 4,294 |  | 61 | 70.39 | 82 | 2 | 0 | $50,000 | 2026-07-18 |
| [Venta Dpto Remodelado 3dormitorios 2baños Estacionamiento](https://www.portalinmobiliario.com/MLC-4201744688-venta-dpto-remodelado-3dormitorios-2banos-estacionamiento-_JM) | 6,690 | $273,251,645 | 94 | 71.17 | 138 | 3 | 1 | $180,000 | 2026-07-18 |
| [Andres De Fuenzalida, Remodelado](https://www.portalinmobiliario.com/MLC-2068828621-andres-de-fuenzalida-remodelado-_JM) | 6,100 |  | 85 | 71.76 | 94 | 3 | 0 | $100,000 | 2026-07-18 |
| [Depto 2 Dormitorios 2 Baños Metro Manuel Montt](https://www.portalinmobiliario.com/MLC-4198325300-depto-2-dormitorios-2-banos-metro-manuel-montt-_JM) | 4,550 |  | 63 | 72.22 | 98 | 2 | 0 | $150,000 | 2026-07-18 |
| [Remodelado 2d/2b \| Barrio Italia \| Metro Parque Bustamante](https://www.portalinmobiliario.com/MLC-2039832321-remodelado-2d2b-barrio-italia-metro-parque-bustamante-_JM) | 5,800 |  | 80 | 72.50 |  | 2 | 1 |  | 2026-07-17 |
| [Venta Depto. 3 Habitaciones Remodelado J.m. Infante (5172)](https://www.portalinmobiliario.com/MLC-4211499724-venta-depto-3-habitaciones-remodelado-jm-infante-5172-_JM) | 6,175 |  | 85 | 72.65 | 94 | 3 | 0 | $80,000 | 2026-07-21 |
| [Oportunidad Remodelado A Pasos Del Metro](https://www.portalinmobiliario.com/MLC-4201707202-oportunidad-remodelado-a-pasos-del-metro-_JM) | 6,190 |  | 85 | 72.82 | 94 | 2 | 0 | $140,000 | 2026-07-18 |
| [Venta Departamento 3hab 2ba Providencia](https://www.portalinmobiliario.com/MLC-4210801150-venta-departamento-3hab-2ba-providencia-_JM) | 6,800 |  | 93 | 73.12 | 85 | 3 | 1 | $200,000 | 2026-07-21 |
| [Amplio Studio 42m2 Ubicacion Excepcional  (170799)](https://www.portalinmobiliario.com/MLC-4198492614-amplio-studio-42m2-ubicacion-excepcional-170799-_JM) | 3,100 |  | 42 | 73.81 | 112 | 1 | 0 | $50,000 | 2026-07-17 |
| [Suecia Amplio Depto 70 M2 \| 1d Suite \| 2e + 2b \| Providencia](https://www.portalinmobiliario.com/MLC-2073964391-suecia-amplio-depto-70-m2-1d-suite-2e-2b-providencia-_JM) | 5,200 |  | 70 | 74.29 | 98 | 1 | 2 | $220,000 | 2026-07-21 |
| [Remodelado De 2 Dormitorios En Clasico Barrio De Providencia](https://www.portalinmobiliario.com/MLC-4211822678-remodelado-de-2-dormitorios-en-clasico-barrio-de-providencia-_JM) | 5,550 |  | 74 | 75.00 | 98 | 2 | 0 | $25,000 | 2026-07-21 |
| [Depto Remodelado En Calle Dinamarca](https://www.portalinmobiliario.com/MLC-2072646613-depto-remodelado-en-calle-dinamarca-_JM) | 6,690 |  | 89 | 75.17 | 89 | 3 | 1 |  | 2026-07-21 |
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
