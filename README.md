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
| [A Pasos De Calle Mapocho (171356)](https://www.portalinmobiliario.com/MLC-2177863393-a-pasos-de-calle-mapocho-171356-_JM) | 1,600 |  | 55 | 29.09 | 47 | 3 | 1 | $15,000 | 2026-08-20 |
| [Oportunidad Unica Precio Onfire En Santiago Centro](https://www.portalinmobiliario.com/MLC-4362223316-oportunidad-unica-precio-onfire-en-santiago-centro-_JM) | 1,969 |  | 66 | 29.83 | 53 | 3 | 0 | $110,000 | 2026-08-18 |
| [Departamento Zenteno Id: 17570](https://www.portalinmobiliario.com/MLC-4377606750-departamento-zenteno-id-17570-_JM) | 1,350 |  | 45 | 30.00 | 71 | 2 | 0 | $30,000 | 2026-08-20 |
| [Departamento En Venta De 2 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4351490460-departamento-en-venta-de-2-dorm-en-santiago-_JM) | 2,217 |  | 72 | 30.79 | 53 | 2 | 0 | $45,000 | 2026-08-15 |
| [Casco Histórico, Metro Santa Ana](https://www.portalinmobiliario.com/MLC-2169759145-casco-historico-metro-santa-ana-_JM) | 2,700 |  | 84 | 32.14 |  | 2 | 0 |  | 2026-08-18 |
| [Departamento Como Nuevo En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4352651460-departamento-como-nuevo-en-excelente-ubicacion-_JM) | 3,060 |  | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-16 |
| [3 Dormitorios Metro Rondizzoni (164475)](https://www.portalinmobiliario.com/MLC-2164064429-3-dormitorios-metro-rondizzoni-164475-_JM) | 1,400 |  | 43 | 32.56 | 71 | 3 | 0 | $80,000 | 2026-08-16 |
| [Venta Depa 2 Dorm 1 Baño Cocina Americana](https://www.portalinmobiliario.com/MLC-2174729491-venta-depa-2-dorm-1-bano-cocina-americana-_JM) | 1,490 |  | 45 | 33.11 | 71 | 2 | 0 | $0 | 2026-08-20 |
| [Amplio Y Luminoso, Vendo Depto Stgo (170838)](https://www.portalinmobiliario.com/MLC-2167513311-amplio-y-luminoso-vendo-depto-stgo-170838-_JM) | 1,990 |  | 60 | 33.17 | 54 | 2 | 0 | $20,000 | 2026-08-17 |
| [Amplio Departamento Sector Cumming (171236)](https://www.portalinmobiliario.com/MLC-4368445534-amplio-departamento-sector-cumming-171236-_JM) | 2,099 |  | 62 | 33.85 | 47 | 3 | 0 | $60,000 | 2026-08-19 |
| [Venta Departamento Santiago Centro, San Pablo (141336)](https://www.portalinmobiliario.com/MLC-4358675422-venta-departamento-santiago-centro-san-pablo-141336-_JM) | 2,360 |  | 69 | 34.20 | 51 | 3 | 1 | $70,000 | 2026-08-17 |
| [Oportunidad De Remodelar, Junto A Metro U. De Chile](https://www.portalinmobiliario.com/MLC-2169840785-oportunidad-de-remodelar-junto-a-metro-u-de-chile-_JM) | 2,300 |  | 67 | 34.33 | 53 | 2 | 0 | $120,000 | 2026-08-18 |
| [Departamento En Venta - Santiago Centro - Rafael Sotomayor](https://www.portalinmobiliario.com/MLC-2173240103-departamento-en-venta-santiago-centro-rafael-sotomayor-_JM) | 2,250 |  | 65 | 34.62 | 48 | 2 | 1 | $98,000 | 2026-08-19 |
| [Metro La Moneda Antiguo](https://www.portalinmobiliario.com/MLC-4342839466-metro-la-moneda-antiguo-_JM) | 2,600 |  | 75 | 34.67 | 53 | 3 | 0 | $100,000 | 2026-08-14 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2154926369-metro-parque-ohiggins-_JM) | 1,690 |  | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-14 |
| [Depto 2 Dormitorios 2 Baños Vista Despejada Parque Los Reyes](https://www.portalinmobiliario.com/MLC-2174707087-depto-2-dormitorios-2-banos-vista-despejada-parque-los-reyes-_JM) | 2,137 |  | 60 | 35.62 | 47 | 2 | 0 | $0 | 2026-08-19 |
| [Oportunidad Para Invertir En Santiago](https://www.portalinmobiliario.com/MLC-4373715664-oportunidad-para-invertir-en-santiago-_JM) | 1,399 |  | 39 | 35.87 | 74 | 2 | 0 | $55,000 | 2026-08-20 |
| [Lindo Dpto En Venta: Espacioso, Bien Ubicado, Recién Pintado](https://www.portalinmobiliario.com/MLC-4364241194-lindo-dpto-en-venta-espacioso-bien-ubicado-recien-pintado-_JM) | 1,650 |  | 46 | 35.87 | 74 | 2 | 0 | $0 | 2026-08-19 |
| [Depto Stgo Centro 1d 1b (171535)](https://www.portalinmobiliario.com/MLC-2177863187-depto-stgo-centro-1d-1b-171535-_JM) | 1,840 |  | 50 | 36.80 | 73 | 1 | 0 | $50,000 | 2026-08-20 |
| [Oportunidad De Venta De Depto En Toesca 2946 Cerca Metro Ula](https://www.portalinmobiliario.com/MLC-4364239510-oportunidad-de-venta-de-depto-en-toesca-2946-cerca-metro-ula-_JM) | 1,400 |  | 38 | 36.84 | 68 | 1 | 0 | $40,000 | 2026-08-19 |
| [Departamento De 3 Dorm. A Pasos De Metro La Moneda](https://www.portalinmobiliario.com/MLC-4368434044-departamento-de-3-dorm-a-pasos-de-metro-la-moneda-_JM) | 3,287 |  | 89 | 36.93 | 55 | 3 | 0 | $0 | 2026-08-19 |
| [Departamento En Venta De 2 Dorm. &#43; Servicios En Santiago](https://www.portalinmobiliario.com/MLC-4366247750-departamento-en-venta-de-2-dorm-43-servicios-en-santiago-_JM) | 3,287 |  | 89 | 36.93 |  | 2 |  |  | 2026-08-19 |
| [Inversión O Vivir En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-4345189968-inversion-o-vivir-en-excelente-ubicacion-_JM) | 1,959 |  | 53 | 36.96 | 65 | 2 | 1 | $100,000 | 2026-08-14 |
| [Vendemos Depto 2 Dormitorios  - Frente Teatro Teletón](https://www.portalinmobiliario.com/MLC-2154940207-vendemos-depto-2-dormitorios-frente-teatro-teleton-_JM) | 1,850 |  | 50 | 37.00 | 73 | 2 | 0 | $90,000 | 2026-08-14 |
| [Ideal Inversión \| Depto 1d Mac Iver,santiago (179104)](https://www.portalinmobiliario.com/MLC-4342891950-ideal-inversion-depto-1d-mac-iversantiago-179104-_JM) | 1,600 |  | 43 | 37.21 | 73 | 1 | 0 | $60,000 | 2026-08-14 |
| [2d 1b En Venta \| Arriendo Vigente $500.000](https://www.portalinmobiliario.com/MLC-2159717235-2d-1b-en-venta-arriendo-vigente-500000-_JM) | 2,500 |  | 67 | 37.31 | 54 | 2 | 0 | $80,000 | 2026-08-15 |
| [Depto. Vista Despejada Barrio Yungay/brasil  2d 2b + Bodega](https://www.portalinmobiliario.com/MLC-4362223096-depto-vista-despejada-barrio-yungaybrasil-2d-2b-bodega-_JM) | 2,100 |  | 56 | 37.50 | 48 | 2 | 0 | $120,000 | 2026-08-18 |
| [Se Vende 3 Dormitorios Santiago Metro Matta](https://www.portalinmobiliario.com/MLC-2170331869-se-vende-3-dormitorios-santiago-metro-matta-_JM) | 1,650 |  | 44 | 37.50 | 81 | 3 | 0 | $55,000 | 2026-08-18 |
| [Venta Dpto. Carmen, Santiago Centro (141282)](https://www.portalinmobiliario.com/MLC-2164064681-venta-dpto-carmen-santiago-centro-141282-_JM) | 1,840 |  | 49 | 37.55 | 81 | 2 | 0 | $90,000 | 2026-08-16 |
| [Renovado Studio Con Bodega Stgo Centro (152207)](https://www.portalinmobiliario.com/MLC-4345187646-renovado-studio-con-bodega-stgo-centro-152207-_JM) | 1,130 |  | 30 | 37.67 | 68 |  | 0 | $40,000 | 2026-08-14 |
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
