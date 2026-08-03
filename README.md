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
| [Ático De Lujo En Estoril: Tu Nuevo Hogar Espera](https://www.portalinmobiliario.com/MLC-2095434441-atico-de-lujo-en-estoril-tu-nuevo-hogar-espera-_JM) | 2,490 | $101,703,527 | 80 | 31.12 |  |  | 0 |  | 2026-07-29 |
| [Vida De Barrio, En Las Condes, Vital Apoquindo, Paul Harris](https://www.portalinmobiliario.com/MLC-2093367707-vida-de-barrio-en-las-condes-vital-apoquindo-paul-harris-_JM) | 2,595 | $106,000,000 | 67 | 38.73 | 83 | 4 | 0 | $0 | 2026-07-28 |
| [Excelente Conectividad Y Entorno Tranquilo (167211)](https://www.portalinmobiliario.com/MLC-2099536331-excelente-conectividad-y-entorno-tranquilo-167211-_JM) | 2,938 | $120,000,000 | 70 | 41.97 | 84 | 4 | 0 | $5,000 | 2026-07-30 |
| [Comodo Y Excelente Departamento 1 Dormitorio Providencia](https://www.portalinmobiliario.com/MLC-2092609325-comodo-y-excelente-departamento-1-dormitorio-providencia-_JM) | 2,081 | $85,000,000 | 48 | 43.35 | 82 | 1 | 0 | $50,000 | 2026-07-28 |
| [Metro Irarrazaval / Bustamante](https://www.portalinmobiliario.com/MLC-2094699843-metro-irarrazaval-bustamante-_JM) | 4,200 | $171,548,118 | 85 | 49.41 | 73 | 3 | 0 | $30,000 | 2026-07-29 |
| [Departamento En Venta En Las Condes, Alejandro Fleming 9695](https://www.portalinmobiliario.com/MLC-2092642729-departamento-en-venta-en-las-condes-alejandro-fleming-9695-_JM) | 3,060 | $125,000,000 | 60 | 51.01 | 83 | 3 | 1 | $35,000 | 2026-07-28 |
| [Departamento En Venta En Las Condes](https://www.portalinmobiliario.com/MLC-4267984348-departamento-en-venta-en-las-condes-_JM) | 2,816 | $115,000,000 | 52 | 54.14 | 126 | 3 | 1 | $0 | 2026-07-31 |
| [2d  1b En Bosque De La Villa, Las Condes](https://www.portalinmobiliario.com/MLC-2097397397-2d-1b-en-bosque-de-la-villa-las-condes-_JM) | 2,450 | $100,069,736 | 45 | 54.44 | 126 | 2 | 0 | $15,000 | 2026-07-29 |
| [Departamento En Venta De 2 Dorm. En Las Condes](https://www.portalinmobiliario.com/MLC-2109940269-departamento-en-venta-de-2-dorm-en-las-condes-_JM) | 3,305 | $135,000,000 | 60 | 55.09 | 84 | 2 | 0 | $17,000 | 2026-08-03 |
| [Departamento 3d / 2d En Venta - Las Condes](https://www.portalinmobiliario.com/MLC-2098657379-departamento-3d-2d-en-venta-las-condes-_JM) | 4,865 | $198,709,903 | 84 | 57.92 | 89 | 3 | 0 | $90,000 | 2026-07-30 |
| [Venta Depto 3 Habitaciones 2 Baños - Metro Los Leones (5301)](https://www.portalinmobiliario.com/MLC-4268005294-venta-depto-3-habitaciones-2-banos-metro-los-leones-5301-_JM) | 4,600 | $187,886,034 | 79 | 58.23 | 94 | 3 | 0 | $180,000 | 2026-07-31 |
| [Duplex Luminoso Hogar Con Vista A Jardín (173179)](https://www.portalinmobiliario.com/MLC-4257166980-duplex-luminoso-hogar-con-vista-a-jardin-173179-_JM) | 5,250 | $214,435,148 | 89 | 58.99 | 94 | 3 | 0 | $140,000 | 2026-07-29 |
| [Metro Salvador 3d, 2b, Amplia Terraza](https://www.portalinmobiliario.com/MLC-2091484649-metro-salvador-3d-2b-amplia-terraza-_JM) | 5,250 | $214,435,148 | 86 | 61.05 | 94 | 3 | 0 | $140,000 | 2026-07-28 |
| [Departamento En Venta De 3 Dorm. En Las Condes](https://www.portalinmobiliario.com/MLC-4257174920-departamento-en-venta-de-3-dorm-en-las-condes-_JM) | 5,500 | $224,646,345 | 90 | 61.11 | 88 | 3 | 0 | $100,000 | 2026-07-29 |
| [Oportunidad Para Remodelar Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2092639875-oportunidad-para-remodelar-excelente-ubicacion-_JM) | 4,600 | $187,886,034 | 75 | 61.33 | 98 | 3 | 0 | $50,000 | 2026-07-28 |
| [Moderno Depto En Corazón De Las Condes (173909)](https://www.portalinmobiliario.com/MLC-4282528264-moderno-depto-en-corazon-de-las-condes-173909-_JM) | 5,600 | $228,730,824 | 90 | 62.22 | 89 | 3 | 1 | $80,000 | 2026-08-03 |
| [Oportunidad De Remodelar, Invertir Y Realizar Flip...](https://www.portalinmobiliario.com/MLC-4269930986-oportunidad-de-remodelar-invertir-y-realizar-flip-_JM) | 5,000 | $204,223,950 | 80 | 62.50 |  | 4 | 1 |  | 2026-07-31 |
| [Se Vende Amplio Departamento En Providencia](https://www.portalinmobiliario.com/MLC-4275309782-se-vende-amplio-departamento-en-providencia-_JM) | 3,690 | $150,717,275 | 58 | 63.62 | 98 | 2 | 0 | $80,000 | 2026-08-01 |
| [Oportunidad Inversionistas!!!](https://www.portalinmobiliario.com/MLC-4282527870-oportunidad-inversionistas-_JM) | 1,910 | $78,000,000 | 30 | 63.66 | 82 | 1 | 0 | $70,000 | 2026-08-03 |
| [Un Clásico Dúplex Remodelado En El Corazón De Providencia](https://www.portalinmobiliario.com/MLC-4276961740-un-clasico-duplex-remodelado-en-el-corazon-de-providencia-_JM) | 6,000 | $245,068,740 | 94 | 63.83 | 94 | 3 | 1 | $120,000 | 2026-08-01 |
| [Inversión Segura En Providencia Acepta Oferta (173399)](https://www.portalinmobiliario.com/MLC-4263469070-inversion-segura-en-providencia-acepta-oferta-173399-_JM) | 4,897 | $200,000,000 | 76 | 64.43 | 98 | 4 | 0 | $70,000 | 2026-07-30 |
| [Primer Piso Remodelar  Con Jardin Exclusivo](https://www.portalinmobiliario.com/MLC-4269928146-primer-piso-remodelar-con-jardin-exclusivo-_JM) | 5,600 | $228,730,824 | 86 | 65.12 | 85 | 3 | 1 | $100,000 | 2026-07-31 |
| [Departamento En Venta De 2 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4248422652-departamento-en-venta-de-2-dorm-en-providencia-_JM) | 5,990 | $244,660,292 | 91 | 65.82 | 80 | 2 | 0 | $90,000 | 2026-07-28 |
| [Venta Departamento Providencia Tercer Piso Sin Ascensor](https://www.portalinmobiliario.com/MLC-4267988644-venta-departamento-providencia-tercer-piso-sin-ascensor-_JM) | 4,900 | $200,139,471 | 74 | 66.22 | 84 | 3 | 1 | $57,000 | 2026-07-31 |
| [Departamento En Venta De 3 Dorm.2baños En Las Condes](https://www.portalinmobiliario.com/MLC-4268008526-departamento-en-venta-de-3-dorm2banos-en-las-condes-_JM) | 4,652 | $190,000,000 | 70 | 66.45 | 100 | 3 | 1 | $0 | 2026-07-31 |
| [Ubicación Privilegiada Y Vista Panorámica En Providencia](https://www.portalinmobiliario.com/MLC-4275274208-ubicacion-privilegiada-y-vista-panoramica-en-providencia-_JM) | 3,672 | $149,982,069 | 55 | 66.76 |  | 2 | 0 |  | 2026-08-01 |
| [Departamento Con Gran Vista Despejada](https://www.portalinmobiliario.com/MLC-4248044686-departamento-con-gran-vista-despejada-_JM) | 5,800 | $236,899,782 | 85 | 68.24 | 93 | 2 | 1 | $150,000 | 2026-07-28 |
| [Venta Departamento Remodelado 2d 2b - Providencia](https://www.portalinmobiliario.com/MLC-4268011160-venta-departamento-remodelado-2d-2b-providencia-_JM) | 5,150 | $210,350,668 | 75 | 68.67 | 84 | 2 | 1 | $75,000 | 2026-07-31 |
| [Departamento El Golf, Las Condes](https://www.portalinmobiliario.com/MLC-4274550200-departamento-el-golf-las-condes-_JM) | 5,600 | $228,730,824 | 81 | 69.14 | 99 | 1 | 0 | $90,000 | 2026-08-01 |
| [Depto. Remodelado A Pasos Del Metro Salvador 3d/2b](https://www.portalinmobiliario.com/MLC-2092297381-depto-remodelado-a-pasos-del-metro-salvador-3d2b-_JM) | 5,700 | $232,815,303 | 82 | 69.51 |  | 3 | 0 |  | 2026-07-28 |
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
