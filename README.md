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
| [Ático De Lujo En Estoril: Tu Nuevo Hogar Espera](https://www.portalinmobiliario.com/MLC-2095434441-atico-de-lujo-en-estoril-tu-nuevo-hogar-espera-_JM) | 2,490 | $101,703,527 | 80 | 31.12 |  |  | 0 |  | 2026-07-29 |
| [Vida De Barrio, En Las Condes, Vital Apoquindo, Paul Harris](https://www.portalinmobiliario.com/MLC-2093367707-vida-de-barrio-en-las-condes-vital-apoquindo-paul-harris-_JM) | 2,595 | $106,000,000 | 67 | 38.73 | 83 | 4 | 0 | $0 | 2026-07-28 |
| [Comodo Y Excelente Departamento 1 Dormitorio Providencia](https://www.portalinmobiliario.com/MLC-2092609325-comodo-y-excelente-departamento-1-dormitorio-providencia-_JM) | 2,081 | $85,000,000 | 48 | 43.35 | 82 | 1 | 0 | $50,000 | 2026-07-28 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4146269686-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,000 | $81,689,580 | 46 | 43.48 | 73 | 2 | 0 | $80,000 | 2026-07-16 |
| [Departamento De Prueba Brp - Insomnia](https://www.portalinmobiliario.com/MLC-4223752016-departamento-de-prueba-brp-insomnia-_JM) | 3,500 | $142,956,765 | 80 | 43.75 | 94 | 2 | 0 |  | 2026-07-23 |
| [Vicuña Mackenna Plaza Italia Providencia](https://www.portalinmobiliario.com/MLC-4217921504-vicuna-mackenna-plaza-italia-providencia-_JM) | 3,000 | $122,534,370 | 66 | 45.45 | 68 | 2 | 0 | $68,000 | 2026-07-22 |
| [Gran Departamento Sobre Av. Providencia](https://www.portalinmobiliario.com/MLC-2076883265-gran-departamento-sobre-av-providencia-_JM) | 4,500 | $183,801,555 | 92 | 48.91 | 94 | 2 | 0 | $155,000 | 2026-07-22 |
| [Metro Irarrazaval / Bustamante](https://www.portalinmobiliario.com/MLC-2094699843-metro-irarrazaval-bustamante-_JM) | 4,200 | $171,548,118 | 85 | 49.41 | 73 | 3 | 0 | $30,000 | 2026-07-29 |
| [Departamento En Venta En Las Condes, Alejandro Fleming 9695](https://www.portalinmobiliario.com/MLC-2092642729-departamento-en-venta-en-las-condes-alejandro-fleming-9695-_JM) | 3,060 | $125,000,000 | 60 | 51.01 | 83 | 3 | 1 | $35,000 | 2026-07-28 |
| [Amplio Duplex / 94m2 / 4d / Parque Con Laguna](https://www.portalinmobiliario.com/MLC-4234530462-amplio-duplex-94m2-4d-parque-con-laguna-_JM) | 4,800 | $196,054,992 | 94 | 51.06 | 94 | 4 | 0 | $126,000 | 2026-07-25 |
| [Departamento En Venta De 1d + 2b En Providencia, 75mts.](https://www.portalinmobiliario.com/MLC-4155493916-departamento-en-venta-de-1d-2b-en-providencia-75mts-_JM) | 3,890 | $158,886,233 | 75 | 51.87 | 98 | 1 | 0 | $140,000 | 2026-07-16 |
| [2d  1b En Bosque De La Villa, Las Condes](https://www.portalinmobiliario.com/MLC-2097397397-2d-1b-en-bosque-de-la-villa-las-condes-_JM) | 2,399 | $98,000,000 | 45 | 53.32 | 126 | 2 | 0 | $15,000 | 2026-07-29 |
| [Vendemos Depto  3 Dorm + 2 Baños  - Providencia](https://www.portalinmobiliario.com/MLC-2046335163-vendemos-depto-3-dorm-2-banos-providencia-_JM) | 4,680 | $191,153,617 | 87 | 53.79 | 85 | 3 | 0 | $95,000 | 2026-07-16 |
| [Metro Sant Isabel / Seminario](https://www.portalinmobiliario.com/MLC-4202055572-metro-sant-isabel-seminario-_JM) | 4,040 | $165,000,000 | 75 | 53.86 | 65 | 3 | 0 | $65,000 | 2026-07-22 |
| [Vendo Dpto Remodelado De 3d, 2b En Providencia. Metro](https://www.portalinmobiliario.com/MLC-4155689346-vendo-dpto-remodelado-de-3d-2b-en-providencia-metro-_JM) | 4,700 | $191,970,513 | 86 | 54.65 | 73 | 3 | 0 | $10,000 | 2026-07-22 |
| [Providencia](https://www.portalinmobiliario.com/MLC-4198493428-providencia-_JM) | 4,500 | $183,801,555 | 82 | 54.88 | 94 | 3 | 0 | $120,000 | 2026-07-22 |
| [Departamento Oportunidad 4d2b Duplex Metro Pedro Valdivia](https://www.portalinmobiliario.com/MLC-4170191206-departamento-oportunidad-4d2b-duplex-metro-pedro-valdivia-_JM) | 5,200 | $212,392,908 | 94 | 55.32 | 94 | 4 | 0 | $90,000 | 2026-07-16 |
| [Depto 4 Dormitorios, 2 Baños, 90 M2 (75040)](https://www.portalinmobiliario.com/MLC-4209724852-depto-4-dormitorios-2-banos-90-m2-75040-_JM) | 4,990 | $203,815,502 | 90 | 55.44 | 94 | 4 | 0 | $120,000 | 2026-07-20 |
| [Hermoso Departamento Providencia](https://www.portalinmobiliario.com/MLC-2039845269-hermoso-departamento-providencia-_JM) | 3,917 | $160,000,000 | 70 | 55.96 | 98 | 1 | 2 | $140,000 | 2026-07-22 |
| [Exclusivo Departamento En Barrio Italia](https://www.portalinmobiliario.com/MLC-2042167777-exclusivo-departamento-en-barrio-italia-_JM) | 3,670 | $149,900,379 | 65 | 56.46 | 65 | 2 | 0 | $20,000 | 2026-07-22 |
| [Miguel Claro / Metro Manuel Montt / Andres Bello](https://www.portalinmobiliario.com/MLC-2055379503-miguel-claro-metro-manuel-montt-andres-bello-_JM) | 3,800 | $155,210,202 | 67 | 56.72 | 98 | 2 | 0 | $100,000 | 2026-07-22 |
| [Primer Piso Con Patio !!!](https://www.portalinmobiliario.com/MLC-2042155509-primer-piso-con-patio--_JM) | 4,290 | $175,224,149 | 75 | 57.20 |  | 3 | 0 |  | 2026-07-22 |
| [Departamento Duplex Antonio Varas](https://www.portalinmobiliario.com/MLC-2076880913-departamento-duplex-antonio-varas-_JM) | 5,400 | $220,561,866 | 94 | 57.45 | 94 | 3 | 0 | $30,000 | 2026-07-22 |
| [Dpto Alto Potencial En Metro Los Leones (161344)](https://www.portalinmobiliario.com/MLC-4134717372-dpto-alto-potencial-en-metro-los-leones-161344-_JM) | 4,600 | $187,886,034 | 80 | 57.50 | 94 | 2 | 0 | $127,000 | 2026-07-22 |
| [Venta Depto 3 Habitaciones 2 Baños - Metro Los Leones (5301)](https://www.portalinmobiliario.com/MLC-4239748584-venta-depto-3-habitaciones-2-banos-metro-los-leones-5301-_JM) | 4,600 | $187,886,034 | 79 | 58.23 | 94 | 3 | 0 | $180,000 | 2026-07-27 |
| [Departamento En Venta De 4 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-2084194649-departamento-en-venta-de-4-dorm-en-providencia-_JM) | 5,400 | $220,561,866 | 92 | 58.70 | 80 | 4 | 0 | $100,000 | 2026-07-25 |
| [Ubicación Estratégica Para Renta Corta](https://www.portalinmobiliario.com/MLC-2037612333-ubicacion-estrategica-para-renta-corta-_JM) | 3,893 | $159,000,000 | 66 | 58.98 | 98 | 2 | 0 | $170,000 | 2026-07-16 |
| [Duplex Luminoso Hogar Con Vista A Jardín (173179)](https://www.portalinmobiliario.com/MLC-4257166980-duplex-luminoso-hogar-con-vista-a-jardin-173179-_JM) | 5,250 | $214,435,148 | 89 | 58.99 | 94 | 3 | 0 | $140,000 | 2026-07-29 |
| [Duplex Luminoso Hogar Con Vista A Jardín (173179)](https://www.portalinmobiliario.com/MLC-2027786989-duplex-luminoso-hogar-con-vista-a-jardin-173179-_JM) | 5,250 | $214,435,148 | 89 | 58.99 | 94 | 3 |  |  | 2026-07-22 |
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
