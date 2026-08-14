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
| [Terraza De Lujo En Estoril](https://www.portalinmobiliario.com/MLC-4328827246-terraza-de-lujo-en-estoril-_JM) | 2,100 | $85,787,898 | 80 | 26.25 |  |  | 0 |  | 2026-08-13 |
| [Metro La Moneda Antiguo](https://www.portalinmobiliario.com/MLC-4342839466-metro-la-moneda-antiguo-_JM) | 2,600 | $106,213,588 | 75 | 34.67 | 53 | 3 | 0 | $100,000 | 2026-08-14 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2154926369-metro-parque-ohiggins-_JM) | 1,690 | $69,038,832 | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-14 |
| [Inversión O Vivir En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4345189968-inversion-o-vivir-en-excelente-ubicacion-_JM) | 1,959 | $80,027,853 | 53 | 36.96 | 65 | 2 | 1 | $100,000 | 2026-08-14 |
| [Vendemos Depto 2 Dormitorios  - Frente Teatro Teletón](https://www.portalinmobiliario.com/MLC-2154940207-vendemos-depto-2-dormitorios-frente-teatro-teleton-_JM) | 1,850 | $75,575,053 | 50 | 37.00 | 73 | 2 | 0 | $90,000 | 2026-08-14 |
| [Ideal Inversión \| Depto 1d Mac Iver,santiago (179104)](https://www.portalinmobiliario.com/MLC-4342891950-ideal-inversion-depto-1d-mac-iversantiago-179104-_JM) | 1,600 | $65,362,208 | 43 | 37.21 | 73 | 1 | 0 | $60,000 | 2026-08-14 |
| [Renovado Studio Con Bodega Stgo Centro (152207)](https://www.portalinmobiliario.com/MLC-4345187646-renovado-studio-con-bodega-stgo-centro-152207-_JM) | 1,130 | $46,162,059 | 30 | 37.67 | 68 |  | 0 | $40,000 | 2026-08-14 |
| [Venta Departamento 2hab 1ba Santiago](https://www.portalinmobiliario.com/MLC-4342891226-venta-departamento-2hab-1ba-santiago-_JM) | 2,203 | $90,000,000 | 58 | 37.98 | 65 | 2 | 0 | $90,000 | 2026-08-14 |
| [Inversión Única: Dpto. 2d/2b En Santiago Centro](https://www.portalinmobiliario.com/MLC-2153981671-inversion-unica-dpto-2d2b-en-santiago-centro-_JM) | 1,983 | $81,008,287 | 52 | 38.13 |  | 2 | 0 |  | 2026-08-14 |
| [Dpto 2 Dormitorios,2 Baños, Metro Santa Ana (172571)](https://www.portalinmobiliario.com/MLC-2154957663-dpto-2-dormitorios2-banos-metro-santa-ana-172571-_JM) | 2,448 | $100,000,000 | 64 | 38.25 | 47 | 2 | 0 | $100,000 | 2026-08-14 |
| [Vendemos Confortable Departamento En Calle Cóndor](https://www.portalinmobiliario.com/MLC-2154940181-vendemos-confortable-departamento-en-calle-condor-_JM) | 1,990 | $81,294,246 | 52 | 38.27 | 54 | 2 | 0 | $40,000 | 2026-08-14 |
| [Tu Nuevo Hogar Economico En Las Condes](https://www.portalinmobiliario.com/MLC-4313531944-tu-nuevo-hogar-economico-en-las-condes-_JM) | 2,595 | $106,000,000 | 67 | 38.73 | 85 | 4 | 0 | $0 | 2026-08-13 |
| [Barrio Republica Dos Dormitorios Dos Baños](https://www.portalinmobiliario.com/MLC-2155655283-barrio-republica-dos-dormitorios-dos-banos-_JM) | 2,700 | $110,298,726 | 69 | 39.13 | 54 | 2 | 0 | $160,000 | 2026-08-14 |
| [Se Vende Departamento 2d+2b En Cumming 1350 Santiago](https://www.portalinmobiliario.com/MLC-4345167112-se-vende-departamento-2d2b-en-cumming-1350-santiago-_JM) | 2,400 | $98,043,312 | 61 | 39.34 | 47 | 2 | 0 | $0 | 2026-08-14 |
| [San Pablo Barroso Oportunidad](https://www.portalinmobiliario.com/MLC-4342838216-san-pablo-barroso-oportunidad-_JM) | 1,200 | $49,000,000 | 30 | 39.98 | 71 | 1 | 0 | $60,000 | 2026-08-14 |
| [Departamento En Venta En Santiago](https://www.portalinmobiliario.com/MLC-2153960801-departamento-en-venta-en-santiago-_JM) | 2,421 | $98,900,000 | 60 | 40.35 | 48 | 2 | 0 | $0 | 2026-08-14 |
| [Departamento En Venta De 2 Dorm 1 Baño Cerca U. Católica](https://www.portalinmobiliario.com/MLC-4345188142-departamento-en-venta-de-2-dorm-1-bano-cerca-u-catolica-_JM) | 2,200 | $89,873,036 | 54 | 40.74 | 68 | 2 | 0 | $36,000 | 2026-08-14 |
| [Depto En Venta 1d Con Bodega Metro U De Chile Santiago](https://www.portalinmobiliario.com/MLC-2155650931-depto-en-venta-1d-con-bodega-metro-u-de-chile-santiago-_JM) | 1,590 | $64,953,694 | 39 | 40.77 | 74 | 1 | 0 | $60,000 | 2026-08-14 |
| [Departamento En Venta De 2 Dormitorios En Santiago](https://www.portalinmobiliario.com/MLC-4344757154-departamento-en-venta-de-2-dormitorios-en-santiago-_JM) | 1,600 | $65,362,208 | 39 | 41.03 |  | 2 | 0 |  | 2026-08-14 |
| [San Pablo / Amunategui](https://www.portalinmobiliario.com/MLC-2155654957-san-pablo-amunategui-_JM) | 2,275 | $92,936,890 | 55 | 41.36 | 51 | 2 | 0 |  | 2026-08-14 |
| [Atención Inversionistas!!, ¡¡rebajado!!, 2d-1b, 44m2, Stgo.](https://www.portalinmobiliario.com/MLC-2155628749-atencion-inversionistas-rebajado-2d-1b-44m2-stgo-_JM) | 1,824 | $74,500,000 | 44 | 41.45 | 74 | 2 | 0 | $90,000 | 2026-08-14 |
| [Departamento1d1b Recien Romedelado. Ideal Para Inversion ...](https://www.portalinmobiliario.com/MLC-4343904232-departamento1d1b-recien-romedelado-ideal-para-inversion--_JM) | 1,950 | $79,660,191 | 47 | 41.49 | 73 | 1 | 0 | $80,000 | 2026-08-14 |
| [Departamento Venta 1 Dorm. 1 Baño Santiago Metro U Chile.](https://www.portalinmobiliario.com/MLC-2154931897-departamento-venta-1-dorm-1-bano-santiago-metro-u-chile-_JM) | 1,469 | $60,000,000 | 35 | 41.96 | 74 | 1 | 0 | $40,000 | 2026-08-14 |
| [Avenida Manuel Rodríguez (163964)](https://www.portalinmobiliario.com/MLC-4345161494-avenida-manuel-rodriguez-163964-_JM) | 2,100 | $85,787,898 | 50 | 42.00 | 73 | 2 | 0 | $150,000 | 2026-08-14 |
| [Oportunidad De Inversión: Depto En Venta Alto Potencial D...](https://www.portalinmobiliario.com/MLC-2154941557-oportunidad-de-inversion-depto-en-venta-alto-potencial-d-_JM) | 1,850 | $75,575,053 | 44 | 42.05 | 73 | 1 | 0 | $80,000 | 2026-08-14 |
| [Amplio; Metro Los Heroes Inacap, Cocina A Parte, Termopanel](https://www.portalinmobiliario.com/MLC-4344783356-amplio-metro-los-heroes-inacap-cocina-a-parte-termopanel-_JM) | 2,400 | $98,043,312 | 57 | 42.11 | 53 | 2 | 0 | $120,000 | 2026-08-14 |
| [Metro Parque Ohiggins](https://www.portalinmobiliario.com/MLC-4342839104-metro-parque-ohiggins-_JM) | 1,811 | $74,000,000 | 43 | 42.13 | 74 | 3 | 0 | $80,000 | 2026-08-14 |
| [Venta Depto.  3 Habitaciones 2 Baños San Isidro (5331)](https://www.portalinmobiliario.com/MLC-2153960345-venta-depto-3-habitaciones-2-banos-san-isidro-5331-_JM) | 2,950 | $120,511,571 | 70 | 42.14 | 65 | 3 | 0 | $150,000 | 2026-08-14 |
| [Acogedor, 2dorms, 2baños, 1estac. 1bodega. Metro O Higgins](https://www.portalinmobiliario.com/MLC-4344771872-acogedor-2dorms-2banos-1estac-1bodega-metro-o-higgins-_JM) | 2,154 | $88,000,000 | 51 | 42.24 | 74 | 2 | 1 | $115,000 | 2026-08-14 |
| [Dpto 2d 1b En Matta](https://www.portalinmobiliario.com/MLC-4343903676-dpto-2d-1b-en-matta-_JM) | 1,395 | $57,000,000 | 33 | 42.28 | 81 | 2 | 0 | $30,000 | 2026-08-14 |
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
