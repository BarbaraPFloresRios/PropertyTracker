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
| [Departamento - Santiago Centro 54 M2](https://www.portalinmobiliario.com/MLC-4380420442-departamento-santiago-centro-54-m2-_JM) | 1,225 |  | 54 | 22.69 | 53 | 2 | 0 |  | 2026-08-21 |
| [A Pasos De Calle Mapocho (171356)](https://www.portalinmobiliario.com/MLC-2177863393-a-pasos-de-calle-mapocho-171356-_JM) | 1,600 |  | 55 | 29.09 | 47 | 3 | 1 | $15,000 | 2026-08-20 |
| [Cumming 1350 ,excelente Depto 2 D 2 B  (82859)](https://www.portalinmobiliario.com/MLC-2183115821-cumming-1350-excelente-depto-2-d-2-b-82859-_JM) | 2,000 |  | 68 | 29.41 | 47 | 2 | 0 | $90,000 | 2026-08-22 |
| [Departamento Zenteno Id: 17570](https://www.portalinmobiliario.com/MLC-4377606750-departamento-zenteno-id-17570-_JM) | 1,350 |  | 45 | 30.00 | 71 | 2 | 0 | $30,000 | 2026-08-20 |
| [Rebajado Por Viaje, 2500uf!](https://www.portalinmobiliario.com/MLC-2179291421-rebajado-por-viaje-2500uf-_JM) | 2,500 |  | 81 | 30.86 |  | 3 | 0 |  | 2026-08-21 |
| [Luminoso Y Amplio Departamento Santiago](https://www.portalinmobiliario.com/MLC-2195804749-luminoso-y-amplio-departamento-santiago-_JM) | 3,060 |  | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-26 |
| [Venta Depa 2 Dorm 1 Baño Cocina Americana](https://www.portalinmobiliario.com/MLC-2174729491-venta-depa-2-dorm-1-bano-cocina-americana-_JM) | 1,490 |  | 45 | 33.11 | 71 | 2 | 0 | $0 | 2026-08-20 |
| [Departamento San Pablo Id: 178314](https://www.portalinmobiliario.com/MLC-2179806003-departamento-san-pablo-id-178314-_JM) | 1,670 |  | 50 | 33.40 | 71 | 1 | 0 | $90,000 | 2026-08-21 |
| [Departamento 3 Dormitorios Cerca De Futura Estación De Metro](https://www.portalinmobiliario.com/MLC-4381518820-departamento-3-dormitorios-cerca-de-futura-estacion-de-metro-_JM) | 2,200 |  | 65 | 33.85 | 47 | 3 | 0 | $100,000 | 2026-08-21 |
| [Venta Departamento 2d Y 2b Frente A Parque Los Reyes](https://www.portalinmobiliario.com/MLC-2194370419-venta-departamento-2d-y-2b-frente-a-parque-los-reyes-_JM) | 1,837 |  | 53 | 34.66 | 47 | 2 | 0 | $0 | 2026-08-26 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2183099611-metro-parque-ohiggins-_JM) | 1,690 |  | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-22 |
| [Departamento Remodelado 2d1b Centro Historico](https://www.portalinmobiliario.com/MLC-2189298379-departamento-remodelado-2d1b-centro-historico-_JM) | 1,590 |  | 45 | 35.33 | 71 | 2 | 0 | $90,000 | 2026-08-25 |
| [Oportunidad Venta Depto 3d2b+est+bod Cerca Metro Franklin](https://www.portalinmobiliario.com/MLC-4405955940-oportunidad-venta-depto-3d2bestbod-cerca-metro-franklin-_JM) | 2,300 |  | 65 | 35.38 | 54 | 3 | 1 | $100,000 | 2026-08-26 |
| [Oportunidad Para Invertir En Santiago](https://www.portalinmobiliario.com/MLC-4373715664-oportunidad-para-invertir-en-santiago-_JM) | 1,399 |  | 39 | 35.87 | 74 | 2 | 0 | $55,000 | 2026-08-20 |
| [San Antonio / Monjitas / Metro Bellas Artes](https://www.portalinmobiliario.com/MLC-4396273766-san-antonio-monjitas-metro-bellas-artes-_JM) | 1,300 |  | 36 | 36.11 | 73 | 1 | 0 | $70,000 | 2026-08-25 |
| [Duplex Stgo Centro 2d 1b - 62m2 - Metro - 2190uf](https://www.portalinmobiliario.com/MLC-2189069143-duplex-stgo-centro-2d-1b-62m2-metro-2190uf-_JM) | 2,190 |  | 60 | 36.50 | 51 | 2 | 0 | $130,000 | 2026-08-24 |
| [Oportunidad Rebajado!!! Acogedor Departamento Barrio Yungay](https://www.portalinmobiliario.com/MLC-2193649427-oportunidad-rebajado-acogedor-departamento-barrio-yungay-_JM) | 1,650 |  | 45 | 36.67 | 66 | 2 | 0 | $60,000 | 2026-08-26 |
| [Depto Stgo Centro 1d 1b (171535)](https://www.portalinmobiliario.com/MLC-2177863187-depto-stgo-centro-1d-1b-171535-_JM) | 1,840 |  | 50 | 36.80 | 73 | 1 | 0 | $50,000 | 2026-08-20 |
| [Departamento En Venta De 2 Dorm. &#43; Servicios En Santiago](https://www.portalinmobiliario.com/MLC-4366247750-departamento-en-venta-de-2-dorm-43-servicios-en-santiago-_JM) | 3,287 |  | 89 | 36.93 | 55 | 2 | 0 | $100,000 | 2026-08-19 |
| [Inversión O Vivir En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2183125251-inversion-o-vivir-en-excelente-ubicacion-_JM) | 1,959 |  | 53 | 36.96 | 65 | 2 | 1 | $100,000 | 2026-08-22 |
| [Venta Departamento Santiago 2 Dormitorios Parque Almagro](https://www.portalinmobiliario.com/MLC-4398172264-venta-departamento-santiago-2-dormitorios-parque-almagro-_JM) | 1,909 |  | 51 | 37.43 | 74 | 2 | 0 | $100,000 | 2026-08-25 |
| [Departamento Metro Sta Lucía 3d,1b](https://www.portalinmobiliario.com/MLC-2181846623-departamento-metro-sta-lucia-3d1b-_JM) | 1,910 |  | 51 | 37.45 | 74 | 3 | 0 | $125,000 | 2026-08-22 |
| [2d,2b - 48m2 Eleuterio Con Cochrane](https://www.portalinmobiliario.com/MLC-4404571194-2d2b-48m2-eleuterio-con-cochrane-_JM) | 1,800 |  | 48 | 37.50 | 74 | 2 | 0 | $90,000 | 2026-08-26 |
| [Club Hípico](https://www.portalinmobiliario.com/MLC-2194358929-club-hipico-_JM) | 3,200 |  | 85 | 37.65 | 49 | 3 | 0 | $110,000 | 2026-08-26 |
| [Recuperado Banco Depto 2d 1b Cóndor 1291, Santigo Centro](https://www.portalinmobiliario.com/MLC-4391462008-recuperado-banco-depto-2d-1b-condor-1291-santigo-centro-_JM) | 2,448 |  | 65 | 37.66 | 54 | 2 | 0 |  | 2026-08-24 |
| [Departamento San Diego Id: 82768](https://www.portalinmobiliario.com/MLC-4394177834-departamento-san-diego-id-82768-_JM) | 1,700 |  | 45 | 37.78 | 72 | 2 | 0 | $40,000 | 2026-08-24 |
| [Sin Gasto Comun, Amplios 2 Dor+estacionamiento (180128)](https://www.portalinmobiliario.com/MLC-4394159252-sin-gasto-comun-amplios-2-dorestacionamiento-180128-_JM) | 2,199 |  | 58 | 37.91 | 65 | 2 | 1 | $10,000 | 2026-08-24 |
| [Lord Cochrane / Metro Moneda](https://www.portalinmobiliario.com/MLC-2181845321-lord-cochrane-metro-moneda-_JM) | 1,900 |  | 50 | 38.00 | 74 | 2 | 0 |  | 2026-08-22 |
| [Venta Depto 3 Dorm 2bañ Metro Ñuble](https://www.portalinmobiliario.com/MLC-2176943299-venta-depto-3-dorm-2ban-metro-nuble-_JM) | 2,100 |  | 55 | 38.18 | 61 | 3 | 0 | $90,000 | 2026-08-20 |
| [Nuevo Precio , Metro Santa , Ana Manuel Rodriguez Con San Pa](https://www.portalinmobiliario.com/MLC-4386790106-nuevo-precio-metro-santa-ana-manuel-rodriguez-con-san-pa-_JM) | 2,035 |  | 53 | 38.40 | 51 | 2 | 0 | $110,000 | 2026-08-22 |
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
