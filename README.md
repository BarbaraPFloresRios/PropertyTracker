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
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2050886405-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 1,250 | $51,055,988 | 55 | 22.73 | 84 | 2 | 0 | $60,000 | 2026-07-22 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4146269686-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,000 | $81,689,580 | 46 | 43.48 | 73 | 2 | 0 | $80,000 | 2026-07-16 |
| [Vicuña Mackenna Plaza Italia Providencia](https://www.portalinmobiliario.com/MLC-4217921504-vicuna-mackenna-plaza-italia-providencia-_JM) | 3,000 | $122,534,370 | 66 | 45.45 | 68 | 2 | 0 | $68,000 | 2026-07-22 |
| [Venta Depto., En Torres De Tajamar, Corazón De Providencia](https://www.portalinmobiliario.com/MLC-2020550193-venta-depto-en-torres-de-tajamar-corazon-de-providencia-_JM) | 3,900 | $159,294,681 | 82 | 47.56 | 94 | 2 | 0 | $110,000 | 2026-07-22 |
| [Depto / Metro Los Leones](https://www.portalinmobiliario.com/MLC-4198200752-depto-metro-los-leones-_JM) | 4,500 | $183,801,555 | 93 | 48.39 | 94 | 3 | 0 | $155,000 | 2026-07-18 |
| [Gran Departamento Sobre Av. Providencia](https://www.portalinmobiliario.com/MLC-2076883265-gran-departamento-sobre-av-providencia-_JM) | 4,500 | $183,801,555 | 92 | 48.91 | 94 | 2 | 0 | $155,000 | 2026-07-22 |
| [Vendo Departamento  Antonio Varas Providencia 2 Dorm](https://www.portalinmobiliario.com/MLC-4105556362-vendo-departamento-antonio-varas-providencia-2-dorm-_JM) | 4,300 | $175,632,597 | 87 | 49.43 | 94 | 2 | 0 | $50,000 | 2026-07-21 |
| [Departamento En Venta De 1d + 2b En Providencia, 75mts.](https://www.portalinmobiliario.com/MLC-4155493916-departamento-en-venta-de-1d-2b-en-providencia-75mts-_JM) | 3,890 | $158,886,233 | 75 | 51.87 | 98 | 1 | 0 | $140,000 | 2026-07-16 |
| [Vendemos Depto  3 Dorm + 2 Baños  - Providencia](https://www.portalinmobiliario.com/MLC-2046335163-vendemos-depto-3-dorm-2-banos-providencia-_JM) | 4,680 | $191,153,617 | 87 | 53.79 | 85 | 3 | 0 | $95,000 | 2026-07-16 |
| [Metro Sant Isabel / Seminario](https://www.portalinmobiliario.com/MLC-4202055572-metro-sant-isabel-seminario-_JM) | 4,040 | $165,000,000 | 75 | 53.86 | 65 | 3 | 0 | $65,000 | 2026-07-22 |
| [Vendo Dpto Remodelado De 3d, 2b En Providencia. Metro](https://www.portalinmobiliario.com/MLC-4155689346-vendo-dpto-remodelado-de-3d-2b-en-providencia-metro-_JM) | 4,700 | $191,970,513 | 86 | 54.65 | 73 | 3 | 0 | $10,000 | 2026-07-22 |
| [Providencia](https://www.portalinmobiliario.com/MLC-4198493428-providencia-_JM) | 4,500 | $183,801,555 | 82 | 54.88 | 94 | 3 | 0 | $120,000 | 2026-07-22 |
| [Departamento Oportunidad 4d2b Duplex Metro Pedro Valdivia](https://www.portalinmobiliario.com/MLC-4170191206-departamento-oportunidad-4d2b-duplex-metro-pedro-valdivia-_JM) | 5,200 | $212,392,908 | 94 | 55.32 | 94 | 4 | 0 | $90,000 | 2026-07-16 |
| [Lindo Departamento En Felix Cabrera / Pedro De Valdivia](https://www.portalinmobiliario.com/MLC-2016417437-lindo-departamento-en-felix-cabrera-pedro-de-valdivia-_JM) | 4,600 |  | 83 | 55.42 | 94 | 3 | 0 | $55,000 | 2026-07-16 |
| [Depto 4 Dormitorios, 2 Baños, 90 M2 (75040)](https://www.portalinmobiliario.com/MLC-4209724852-depto-4-dormitorios-2-banos-90-m2-75040-_JM) | 4,990 | $203,815,502 | 90 | 55.44 | 94 | 4 | 0 | $120,000 | 2026-07-20 |
| [Hermoso Departamento Providencia](https://www.portalinmobiliario.com/MLC-2039845269-hermoso-departamento-providencia-_JM) | 3,917 | $160,000,000 | 70 | 55.96 | 98 | 1 | 2 | $140,000 | 2026-07-22 |
| [Exclusivo Departamento En Barrio Italia](https://www.portalinmobiliario.com/MLC-2042167777-exclusivo-departamento-en-barrio-italia-_JM) | 3,670 | $149,900,379 | 65 | 56.46 | 65 | 2 | 0 | $20,000 | 2026-07-22 |
| [Miguel Claro / Metro Manuel Montt / Andres Bello](https://www.portalinmobiliario.com/MLC-2055379503-miguel-claro-metro-manuel-montt-andres-bello-_JM) | 3,800 | $155,210,202 | 67 | 56.72 | 98 | 2 | 0 | $100,000 | 2026-07-22 |
| [Primer Piso Con Patio, Se Aceptan Ofertas!!](https://www.portalinmobiliario.com/MLC-2042155509-primer-piso-con-patio-se-aceptan-ofertas-_JM) | 4,290 | $175,224,149 | 75 | 57.20 |  | 3 | 0 |  | 2026-07-22 |
| [Oportunidad De Inversión Providencia Lyon](https://www.portalinmobiliario.com/MLC-2018145889-oportunidad-de-inversion-providencia-lyon-_JM) | 4,590 | $187,477,586 | 80 | 57.38 |  | 2 | 0 |  | 2026-07-16 |
| [Departamento Duplex Antonio Varas](https://www.portalinmobiliario.com/MLC-2076880913-departamento-duplex-antonio-varas-_JM) | 5,400 | $220,561,866 | 94 | 57.45 | 94 | 3 | 0 | $30,000 | 2026-07-22 |
| [Dpto Alto Potencial En Metro Los Leones (161344)](https://www.portalinmobiliario.com/MLC-4134717372-dpto-alto-potencial-en-metro-los-leones-161344-_JM) | 4,600 | $187,886,034 | 80 | 57.50 | 94 | 2 | 0 | $127,000 | 2026-07-22 |
| [Ubicación Estratégica Para Renta Corta](https://www.portalinmobiliario.com/MLC-2037612333-ubicacion-estrategica-para-renta-corta-_JM) | 3,893 | $159,000,000 | 66 | 58.98 | 98 | 2 | 0 | $170,000 | 2026-07-16 |
| [Remodelado En La Unidad Vecinal Providencia (173179)](https://www.portalinmobiliario.com/MLC-2027786989-remodelado-en-la-unidad-vecinal-providencia-173179-_JM) | 5,250 | $214,435,148 | 89 | 58.99 | 94 | 3 |  |  | 2026-07-22 |
| [Excelente Departamento En Parque Forestal, A Pasos Del Metro](https://www.portalinmobiliario.com/MLC-2076805191-excelente-departamento-en-parque-forestal-a-pasos-del-metro-_JM) | 4,284 | $175,000,000 | 72 | 59.51 | 68 | 3 | 0 | $50,000 | 2026-07-22 |
| [Venta Departamento 1d 2b - Parque Padre Hurtado](https://www.portalinmobiliario.com/MLC-2076882511-venta-departamento-1d-2b-parque-padre-hurtado-_JM) | 4,850 | $198,097,232 | 80 | 60.62 | 88 | 1 | 0 | $130,000 | 2026-07-22 |
| [Departamento Andrés De Fuenzalida Id: 44819](https://www.portalinmobiliario.com/MLC-4105566916-departamento-andres-de-fuenzalida-id-44819-_JM) | 5,200 | $212,392,908 | 85 | 61.18 | 94 | 3 | 0 | $115,000 | 2026-07-16 |
| [Andrés De Fuenzalida (piso 7)](https://www.portalinmobiliario.com/MLC-4211492140-andres-de-fuenzalida-piso-7-_JM) | 5,200 | $212,392,908 | 85 | 61.18 |  | 3 |  |  | 2026-07-21 |
| [Andrés De Fuenzalida (remodelado Completo)](https://www.portalinmobiliario.com/MLC-4210790912-andres-de-fuenzalida-remodelado-completo-_JM) | 5,200 | $212,392,908 | 85 | 61.18 | 94 | 3 | 0 | $115,000 | 2026-07-21 |
| [Gran Oportunidad En El Corazon De Providencia (139579)](https://www.portalinmobiliario.com/MLC-4160975038-gran-oportunidad-en-el-corazon-de-providencia-139579-_JM) | 4,897 | $200,000,000 | 80 | 61.21 | 94 | 4 | 0 | $105,000 | 2026-07-16 |
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
