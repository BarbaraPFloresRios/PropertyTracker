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
| [Terraza De Lujo En Estoril](https://www.portalinmobiliario.com/MLC-4328827246-terraza-de-lujo-en-estoril-_JM) | 2,100 | $85,785,126 | 80 | 26.25 |  |  | 0 |  | 2026-08-13 |
| [Tu Nuevo Hogar Economico En Las Condes](https://www.portalinmobiliario.com/MLC-4313531944-tu-nuevo-hogar-economico-en-las-condes-_JM) | 2,595 | $106,000,000 | 67 | 38.73 | 85 | 4 | 0 | $0 | 2026-08-13 |
| [Malaquias Concha / Parque Bustamante](https://www.portalinmobiliario.com/MLC-4313537430-malaquias-concha-parque-bustamante-_JM) | 4,200 | $171,570,252 | 85 | 49.41 | 73 | 3 | 0 | $30,000 | 2026-08-13 |
| [Departamento En Venta En Las Condes, Alejandro Fleming 9695](https://www.portalinmobiliario.com/MLC-4336831592-departamento-en-venta-en-las-condes-alejandro-fleming-9695-_JM) | 3,060 | $125,000,000 | 60 | 51.00 | 85 | 3 | 1 | $35,000 | 2026-08-13 |
| [Excelente Oportunidad En Las Condes](https://www.portalinmobiliario.com/MLC-4324785732-excelente-oportunidad-en-las-condes-_JM) | 2,717 | $111,000,000 | 51 | 53.28 | 113 | 3 | 0 | $20,000 | 2026-08-13 |
| [2d +1b  / Piso 5 / Remodelado / Vista Poniente (178678)](https://www.portalinmobiliario.com/MLC-4324779558-2d-1b-piso-5-remodelado-vista-poniente-178678-_JM) | 2,940 | $120,099,176 | 55 | 53.45 | 85 | 2 | 1 | $18,000 | 2026-08-13 |
| [Departamento En Venta De 3 Dorm. En Recoleta](https://www.portalinmobiliario.com/MLC-2120250149-departamento-en-venta-de-3-dorm-en-recoleta-_JM) | 3,990 | $162,991,739 | 74 | 53.92 | 68 | 3 | 1 | $150,000 | 2026-08-13 |
| [Departamento Oportunidad 4d2b Duplex Metro Pedro Valdivia](https://www.portalinmobiliario.com/MLC-4335436850-departamento-oportunidad-4d2b-duplex-metro-pedro-valdivia-_JM) | 5,200 | $212,420,312 | 94 | 55.32 | 94 | 4 | 0 | $90,000 | 2026-08-13 |
| [3 Dormitorios. 2 Baños. Metro Salvador](https://www.portalinmobiliario.com/MLC-4296876496-3-dormitorios-2-banos-metro-salvador-_JM) | 4,600 | $187,910,276 | 82 | 56.10 | 94 | 3 | 1 | $110,000 | 2026-08-13 |
| [Miguel Claro / Providencia (157981)](https://www.portalinmobiliario.com/MLC-2145464573-miguel-claro-providencia-157981-_JM) | 3,427 | $140,000,000 | 60 | 57.12 | 98 | 2 | 0 | $140,000 | 2026-08-13 |
| [Departamento Duplex Antonio Varas](https://www.portalinmobiliario.com/MLC-4336837536-departamento-duplex-antonio-varas-_JM) | 5,400 | $220,590,324 | 94 | 57.45 | 94 | 3 | 0 | $30,000 | 2026-08-13 |
| [Venta Departamento Av. Salvador / Los Jesuitas. Providencia.](https://www.portalinmobiliario.com/MLC-2134048965-venta-departamento-av-salvador-los-jesuitas-providencia-_JM) | 5,000 | $204,250,300 | 87 | 57.47 | 85 | 4 | 1 | $88,000 | 2026-08-13 |
| [Departamento Con Alto Potencial De Inversión En Providencia](https://www.portalinmobiliario.com/MLC-4296983494-departamento-con-alto-potencial-de-inversion-en-providencia-_JM) | 5,190 | $212,011,811 | 90 | 57.67 | 94 | 2 | 1 | $70,000 | 2026-08-13 |
| [Venta Depto 3 Habitaciones 2 Baños - Metro Los Leones (5301)](https://www.portalinmobiliario.com/MLC-4329441930-venta-depto-3-habitaciones-2-banos-metro-los-leones-5301-_JM) | 4,600 | $187,910,276 | 79 | 58.23 | 94 | 3 | 0 | $180,000 | 2026-08-13 |
| [Departamento Venta 3dor/2b/ Bilbao Metro Bustamante/parquet](https://www.portalinmobiliario.com/MLC-4317263846-departamento-venta-3dor2b-bilbao-metro-bustamanteparquet-_JM) | 5,300 | $216,505,318 | 90 | 58.89 | 80 | 3 | 0 | $0 | 2026-08-13 |
| [Departamento En Venta De 3 Dorm. En Las Condes](https://www.portalinmobiliario.com/MLC-4303194812-departamento-en-venta-de-3-dorm-en-las-condes-_JM) | 5,500 | $224,675,330 | 90 | 61.11 | 89 | 3 | 0 | $100,000 | 2026-08-13 |
| [Gran Oportunidad En El Corazon De Providencia (139579)](https://www.portalinmobiliario.com/MLC-2130632029-gran-oportunidad-en-el-corazon-de-providencia-139579-_JM) | 4,896 | $200,000,000 | 80 | 61.20 | 94 | 4 | 0 | $105,000 | 2026-08-13 |
| [Depto. Metro Salvador / Seminario 2d+2b+1b](https://www.portalinmobiliario.com/MLC-2140920507-depto-metro-salvador-seminario-2d2b1b-_JM) | 4,000 | $163,400,240 | 65 | 61.54 | 68 | 2 | 0 | $55,000 | 2026-08-13 |
| [Excelente Oportunidad 3d, 3b,  E Y B. Serv. Imago Mundi](https://www.portalinmobiliario.com/MLC-4324532318-excelente-oportunidad-3d-3b-e-y-b-serv-imago-mundi-_JM) | 5,000 | $204,250,300 | 80 | 62.50 | 93 | 4 | 1 | $190,000 | 2026-08-13 |
| [Duplex Remodelado En Venta En Providencia](https://www.portalinmobiliario.com/MLC-4320354400-duplex-remodelado-en-venta-en-providencia-_JM) | 5,990 | $244,691,859 | 94 | 63.72 | 94 | 3 | 1 | $130,000 | 2026-08-13 |
| [Un Departamento Con Historia Y Mucha Vida De Barrio](https://www.portalinmobiliario.com/MLC-2146541265-un-departamento-con-historia-y-mucha-vida-de-barrio-_JM) | 6,000 | $245,100,360 | 94 | 63.83 | 94 | 3 | 1 | $120,000 | 2026-08-13 |
| [Venta\|3d\|2b\|clemente Fabres Y J. M.  Infante\|providencia](https://www.portalinmobiliario.com/MLC-2120244881-venta3d2bclemente-fabres-y-j-m-infanteprovidencia-_JM) | 4,500 | $183,825,270 | 70 | 64.29 | 84 | 3 | 0 | $80,000 | 2026-08-13 |
| [Dpto Con Antejardín Exclusivo Y Estac En Pq Inés De Suárez](https://www.portalinmobiliario.com/MLC-2141518765-dpto-con-antejardin-exclusivo-y-estac-en-pq-ines-de-suarez-_JM) | 5,630 | $230,000,000 | 87 | 64.72 | 85 | 4 | 1 | $20,000 | 2026-08-13 |
| [Departamento Remodelado Clasico A Pasos Metro Baquedano](https://www.portalinmobiliario.com/MLC-2140924711-departamento-remodelado-clasico-a-pasos-metro-baquedano-_JM) | 5,900 | $241,015,354 | 91 | 64.84 | 80 | 2 | 0 | $96,000 | 2026-08-13 |
| [Fabuloso Departamento En Manuel Montt 0115 (151867)](https://www.portalinmobiliario.com/MLC-4337110602-fabuloso-departamento-en-manuel-montt-0115-151867-_JM) | 6,300 | $257,355,378 | 97 | 64.95 | 94 | 4 | 1 | $90,000 | 2026-08-13 |
| [Primer Piso Con Jardin Gran Potencial](https://www.portalinmobiliario.com/MLC-4325112790-primer-piso-con-jardin-gran-potencial-_JM) | 5,600 | $228,760,336 | 86 | 65.12 | 85 | 3 | 1 | $100,000 | 2026-08-13 |
| [Departamento En Venta De 3 Dorm. En Providencia Salvador](https://www.portalinmobiliario.com/MLC-2130624159-departamento-en-venta-de-3-dorm-en-providencia-salvador-_JM) | 4,700 | $191,995,282 | 72 | 65.28 | 78 | 3 | 0 | $0 | 2026-08-13 |
| [Venta Departamento Remodelar 3d 2b - Las Condes](https://www.portalinmobiliario.com/MLC-4324779424-venta-departamento-remodelar-3d-2b-las-condes-_JM) | 4,896 | $200,000,000 | 75 | 65.28 | 107 | 3 | 1 | $110 | 2026-08-13 |
| [Tradicional Depto 4d 3b Prov. Sector Residencial (174496)](https://www.portalinmobiliario.com/MLC-4306697680-tradicional-depto-4d-3b-prov-sector-residencial-174496-_JM) | 6,350 | $259,397,881 | 96 | 66.15 | 85 | 4 | 1 | $110,000 | 2026-08-13 |
| [Departamento En Venta De 3 Dorm.2baños En Las Condes](https://www.portalinmobiliario.com/MLC-4303194552-departamento-en-venta-de-3-dorm2banos-en-las-condes-_JM) | 4,651 | $190,000,000 | 70 | 66.45 | 101 | 3 | 1 | $0 | 2026-08-13 |
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
