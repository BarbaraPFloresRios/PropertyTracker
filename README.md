# PropertyTracker

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 7 days (under 100 m²). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [Depto / Metro Los Leones](https://www.portalinmobiliario.com/MLC-4198200752-depto-metro-los-leones-_JM) | 4,500 | $183,801,555 | 93 | 48.39 | 3 | 0 | $155,000 | 2026-07-18 |
| [Metro Santa Isabel / 3 Dormitorios 2 Baños](https://www.portalinmobiliario.com/MLC-4198500546-metro-santa-isabel-3-dormitorios-2-banos-_JM) | 4,200 | $171,548,118 | 85 | 49.41 | 3 | 0 | $30,000 | 2026-07-18 |
| [Venta Depto 3 Habitaciones 2 Baños - Metro Los Leones (5301)](https://www.portalinmobiliario.com/MLC-4203939854-venta-depto-3-habitaciones-2-banos-metro-los-leones-5301-_JM) | 4,600 | $187,886,034 | 79 | 58.23 | 3 | 0 | $180,000 | 2026-07-19 |
| [Departamento En Venta De 4 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-3960426866-departamento-en-venta-de-4-dorm-en-providencia-_JM) | 5,500 | $224,646,345 | 90 | 61.11 | 4 | 0 | $110,000 | 2026-07-19 |
| [Conectividad Y Confort Garantizados (170733)](https://www.portalinmobiliario.com/MLC-4198492680-conectividad-y-confort-garantizados-170733-_JM) | 4,300 | $175,632,597 | 65 | 66.15 | 2 | 0 | $0 | 2026-07-17 |
| [Cercano A Colegios:  Mariano, Sagrados Corazones, Regina Pac](https://www.portalinmobiliario.com/MLC-4198327076-cercano-a-colegios-mariano-sagrados-corazones-regina-pac-_JM) | 4,900 | $200,139,471 | 74 | 66.22 | 3 | 1 | $57,000 | 2026-07-18 |
| [Se Vende Departamento Remodelado Con Máxima Seguridad, Frent](https://www.portalinmobiliario.com/MLC-4201707146-se-vende-departamento-remodelado-con-maxima-seguridad-frent-_JM) | 4,404 | $179,900,000 | 66 | 66.73 | 3 | 0 | $140,000 | 2026-07-18 |
| [Amplio Departamento A La Salida Del Metro Los Leones](https://www.portalinmobiliario.com/MLC-4201706584-amplio-departamento-a-la-salida-del-metro-los-leones-_JM) | 5,876 | $239,990,000 | 85 | 69.13 | 2 | 0 | $80,000 | 2026-07-18 |
| [Venta Depto Santiago Centro 3 Dorm Y 3 Baños Providencia](https://www.portalinmobiliario.com/MLC-4198325742-venta-depto-santiago-centro-3-dorm-y-3-banos-providencia-_JM) | 6,290 | $256,913,729 | 90 | 69.89 | 3 | 0 | $130,000 | 2026-07-18 |
| [Lindo Departamento En Juana  De  Lestonac Providencia](https://www.portalinmobiliario.com/MLC-4201707636-lindo-departamento-en-juana-de-lestonac-providencia-_JM) | 4,294 | $175,387,528 | 61 | 70.39 | 2 | 0 | $50,000 | 2026-07-18 |
| [Venta Dpto Remodelado 3dormitorios 2baños Estacionamiento](https://www.portalinmobiliario.com/MLC-4201744688-venta-dpto-remodelado-3dormitorios-2banos-estacionamiento-_JM) | 6,690 | $273,251,645 | 94 | 71.17 | 3 | 1 | $180,000 | 2026-07-18 |
| [Andres De Fuenzalida, Remodelado](https://www.portalinmobiliario.com/MLC-2068828621-andres-de-fuenzalida-remodelado-_JM) | 6,100 | $249,153,219 | 85 | 71.76 | 3 | 0 | $100,000 | 2026-07-18 |
| [Depto 2 Dormitorios 2 Baños Metro Manuel Montt](https://www.portalinmobiliario.com/MLC-4198325300-depto-2-dormitorios-2-banos-metro-manuel-montt-_JM) | 4,550 | $185,843,794 | 63 | 72.22 | 2 | 0 | $150,000 | 2026-07-18 |
| [Remodelado 2d/2b \| Barrio Italia \| Metro Parque Bustamante](https://www.portalinmobiliario.com/MLC-2039832321-remodelado-2d2b-barrio-italia-metro-parque-bustamante-_JM) | 5,800 | $236,899,782 | 80 | 72.50 | 2 | 1 |  | 2026-07-17 |
| [Oportunidad Remodelado A Pasos Del Metro](https://www.portalinmobiliario.com/MLC-4201707202-oportunidad-remodelado-a-pasos-del-metro-_JM) | 6,190 | $252,829,250 | 85 | 72.82 | 2 | 0 | $140,000 | 2026-07-18 |
| [Amplio Studio 42m2 Ubicacion Excepcional  (170799)](https://www.portalinmobiliario.com/MLC-4198492614-amplio-studio-42m2-ubicacion-excepcional-170799-_JM) | 3,100 | $126,618,849 | 42 | 73.81 | 1 | 0 | $50,000 | 2026-07-17 |
| [Departamento En ¡ Venta ! Providencia](https://www.portalinmobiliario.com/MLC-4203943108-departamento-en-venta-providencia-_JM) | 3,655 | $149,287,707 | 48 | 76.15 | 2 | 0 |  | 2026-07-19 |
| [Venta De Departamento De 3 Dormitorios.sector Parque Ines De](https://www.portalinmobiliario.com/MLC-4201743910-venta-de-departamento-de-3-dormitoriossector-parque-ines-de-_JM) | 6,500 | $265,491,135 | 84 | 77.38 | 3 | 1 | $160,000 | 2026-07-18 |
| [Vive Con Comodidad Y Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4198197136-vive-con-comodidad-y-excelente-ubicacion-_JM) | 4,800 | $196,054,992 | 62 | 77.42 | 2 | 1 | $200,000 | 2026-07-18 |
| [Providencia, Buscamos Departamentos](https://www.portalinmobiliario.com/MLC-4201705404-providencia-buscamos-departamentos-_JM) | 5,500 | $224,646,345 | 70 | 78.57 | 2 | 1 | $11,111 | 2026-07-18 |
| [Metro Inés De Suárez / Pocuro - Pedro De Valdivia](https://www.portalinmobiliario.com/MLC-2068822359-metro-ines-de-suarez-pocuro-pedro-de-valdivia-_JM) | 7,000 | $285,913,530 | 89 | 78.65 | 2 | 1 | $180,000 | 2026-07-18 |
| [Amplio Departamento En Providencia 2 Dormitorios 2b 1e1bo](https://www.portalinmobiliario.com/MLC-2069469175-amplio-departamento-en-providencia-2-dormitorios-2b-1e1bo-_JM) | 5,600 | $228,730,824 | 70 | 80.00 | 2 | 1 | $280,000 | 2026-07-18 |
| [Grace Kelm Vende Espacioso Depto Gran Terraza De 3 Dorm Y 3](https://www.portalinmobiliario.com/MLC-4201706426-grace-kelm-vende-espacioso-depto-gran-terraza-de-3-dorm-y-3-_JM) | 7,200 | $294,082,488 | 90 | 80.00 | 3 | 1 | $125,000 | 2026-07-18 |
| [Remodelado Duplex De 2d2b A Pasos De Metro Manuel Montt](https://www.portalinmobiliario.com/MLC-2070925703-remodelado-duplex-de-2d2b-a-pasos-de-metro-manuel-montt-_JM) | 7,200 | $294,082,488 | 90 | 80.00 | 2 | 0 | $40,000 | 2026-07-19 |
| [3 Dorm+2 Baños 80 Mts2 - Sin Estac.](https://www.portalinmobiliario.com/MLC-2068832575-3-dorm2-banos-80-mts2-sin-estac-_JM) | 6,250 | $255,279,938 | 78 | 80.13 | 3 | 0 | $170,000 | 2026-07-18 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4198494134-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 7,499 | $306,295,080 | 92 | 81.51 | 3 | 1 | $150,000 | 2026-07-18 |
| [Excelente Departamento Metro Manuel Montt (171371)](https://www.portalinmobiliario.com/MLC-2071198175-excelente-departamento-metro-manuel-montt-171371-_JM) | 6,290 | $256,913,729 | 76 | 82.76 | 2 | 1 | $180,000 | 2026-07-19 |
| [Luminoso Y Amplio Departamento De 3d + 2b En Providencia](https://www.portalinmobiliario.com/MLC-3894935818-luminoso-y-amplio-departamento-de-3d-2b-en-providencia-_JM) | 7,000 | $285,913,530 | 84 | 83.33 | 3 | 1 | $145,000 | 2026-07-19 |
| [Remodelado, Vista Norte, Dos Dormitorios Estacionamiento](https://www.portalinmobiliario.com/MLC-2068821979-remodelado-vista-norte-dos-dormitorios-estacionamiento-_JM) | 4,950 | $202,181,710 | 59 | 83.90 | 2 | 1 | $80,000 | 2026-07-19 |
| [Hermoso Depto En Venta En Providencia](https://www.portalinmobiliario.com/MLC-2069547893-hermoso-depto-en-venta-en-providencia-_JM) | 5,900 | $240,984,261 | 70 | 84.29 | 2 | 1 | $89,000 | 2026-07-19 |
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
