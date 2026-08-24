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
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2170303589-departamento-estudio-en-excelente-ubicacion-_JM) | 1,224 | $50,000,000 | 55 | 22.25 | 54 | 1 | 0 | $50 | 2026-08-18 |
| [Departamento - Santiago Centro 54 M2](https://www.portalinmobiliario.com/MLC-4380420442-departamento-santiago-centro-54-m2-_JM) | 1,225 | $50,059,074 | 54 | 22.69 | 53 | 2 | 0 |  | 2026-08-21 |
| [Oportunidad Única Vendo Dpto. Estudio Con Bodega Excelente](https://www.portalinmobiliario.com/MLC-2169832273-oportunidad-unica-vendo-dpto-estudio-con-bodega-excelente-_JM) | 1,150 | $47,000,000 | 50 | 23.00 | 74 | 1 | 0 | $50,000 | 2026-08-18 |
| [Venta Departamento Santiago De 3 Dorm 2 Baños Antiguo Piso 1](https://www.portalinmobiliario.com/MLC-4382357728-venta-departamento-santiago-de-3-dorm-2-banos-antiguo-piso-1-_JM) | 2,692 | $110,000,000 | 94 | 28.64 | 55 | 3 | 0 | $68,000 | 2026-08-21 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2170328349-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,297 | $53,000,000 | 45 | 28.82 | 74 | 1 | 0 | $50,000 | 2026-08-18 |
| [A Pasos De Calle Mapocho (171356)](https://www.portalinmobiliario.com/MLC-2177863393-a-pasos-de-calle-mapocho-171356-_JM) | 1,600 | $65,383,280 | 55 | 29.09 | 47 | 3 | 1 | $15,000 | 2026-08-20 |
| [Cumming 1350 ,excelente Depto 2 D 2 B  (82859)](https://www.portalinmobiliario.com/MLC-2183115821-cumming-1350-excelente-depto-2-d-2-b-82859-_JM) | 2,000 | $81,729,100 | 68 | 29.41 | 47 | 2 | 0 | $90,000 | 2026-08-22 |
| [Oportunidad Unica Precio Onfire En Santiago Centro](https://www.portalinmobiliario.com/MLC-4362223316-oportunidad-unica-precio-onfire-en-santiago-centro-_JM) | 1,969 | $80,462,299 | 66 | 29.83 | 53 | 3 | 0 | $110,000 | 2026-08-18 |
| [Departamento Zenteno Id: 17570](https://www.portalinmobiliario.com/MLC-4377606750-departamento-zenteno-id-17570-_JM) | 1,350 | $55,167,143 | 45 | 30.00 | 71 | 2 | 0 | $30,000 | 2026-08-20 |
| [Departamento 2hab 1ba Cercano A Estación De Metro](https://www.portalinmobiliario.com/MLC-4375123120-departamento-2hab-1ba-cercano-a-estacion-de-metro-_JM) | 1,835 | $75,000,000 | 60 | 30.59 | 65 | 2 | 0 | $70,000 | 2026-08-20 |
| [Rebajado Por Viaje, 2500uf!](https://www.portalinmobiliario.com/MLC-2179291421-rebajado-por-viaje-2500uf-_JM) | 2,500 | $102,161,375 | 81 | 30.86 |  | 3 | 0 |  | 2026-08-21 |
| [Acogedor Departamento Libertad Con Presidente Balmaceda](https://www.portalinmobiliario.com/MLC-4391458976-acogedor-departamento-libertad-con-presidente-balmaceda-_JM) | 2,202 | $90,000,000 | 70 | 31.46 | 47 | 3 | 1 | $95,000 | 2026-08-23 |
| [Casco Histórico, Metro Santa Ana](https://www.portalinmobiliario.com/MLC-2169759145-casco-historico-metro-santa-ana-_JM) | 2,700 | $110,334,285 | 84 | 32.14 |  | 2 | 0 |  | 2026-08-18 |
| [Vendo Departamento 2d + 2b, Calle Porvenir, Santiago](https://www.portalinmobiliario.com/MLC-2171595503-vendo-departamento-2d-2b-calle-porvenir-santiago-_JM) | 1,933 | $79,000,000 | 60 | 32.22 | 54 | 2 | 0 | $90,000 | 2026-08-19 |
| [Departamento Zenteno Id: 136284](https://www.portalinmobiliario.com/MLC-4362613680-departamento-zenteno-id-136284-_JM) | 1,782 | $72,800,000 | 55 | 32.39 | 53 | 2 | 0 | $0 | 2026-08-18 |
| [Venta Depa 2 Dorm 1 Baño Cocina Americana](https://www.portalinmobiliario.com/MLC-2174729491-venta-depa-2-dorm-1-bano-cocina-americana-_JM) | 1,490 | $60,888,180 | 45 | 33.11 | 71 | 2 | 0 | $0 | 2026-08-20 |
| [Departamento General Gana Id: 148539](https://www.portalinmobiliario.com/MLC-2170328421-departamento-general-gana-id-148539-_JM) | 930 | $38,000,000 | 28 | 33.21 | 71 | 1 | 0 | $38,540 | 2026-08-18 |
| [Departamento San Pablo Id: 178314](https://www.portalinmobiliario.com/MLC-2179806003-departamento-san-pablo-id-178314-_JM) | 1,670 | $68,243,798 | 50 | 33.40 | 71 | 1 | 0 | $90,000 | 2026-08-21 |
| [Oportunidad  En El Corazón De Santiago Venta O Arriendo](https://www.portalinmobiliario.com/MLC-2170305383-oportunidad-en-el-corazon-de-santiago-venta-o-arriendo-_JM) | 2,031 | $83,000,000 | 60 | 33.85 | 48 | 2 | 0 | $70,000 | 2026-08-18 |
| [Amplio Departamento Sector Cumming (171236)](https://www.portalinmobiliario.com/MLC-4368445534-amplio-departamento-sector-cumming-171236-_JM) | 2,099 | $85,774,690 | 62 | 33.85 | 47 | 3 | 0 | $60,000 | 2026-08-19 |
| [Departamento 3 Dormitorios Cerca De Futura Estación De Metro](https://www.portalinmobiliario.com/MLC-4381518820-departamento-3-dormitorios-cerca-de-futura-estacion-de-metro-_JM) | 2,200 | $89,902,010 | 65 | 33.85 | 47 | 3 | 0 | $100,000 | 2026-08-21 |
| [Atencion! Departamento En Venta Martinez De Rozas N°2375](https://www.portalinmobiliario.com/MLC-4366668686-atencion-departamento-en-venta-martinez-de-rozas-n2375-_JM) | 1,468 | $60,000,000 | 43 | 34.15 | 65 | 1 | 0 |  | 2026-08-19 |
| [Oportunidad 2d-2b 52m2](https://www.portalinmobiliario.com/MLC-2180372065-oportunidad-2d-2b-52m2-_JM) | 1,713 | $70,000,000 | 50 | 34.26 | 82 | 2 | 0 | $80,000 | 2026-08-21 |
| [Vendo Amplio Depto  3dorm 2ba Santiago Centro](https://www.portalinmobiliario.com/MLC-4375125666-vendo-amplio-depto-3dorm-2ba-santiago-centro-_JM) | 2,398 | $98,000,000 | 70 | 34.26 | 53 | 3 | 0 | $85,000 | 2026-08-20 |
| [Oportunidad De Remodelar, Junto A Metro U. De Chile](https://www.portalinmobiliario.com/MLC-2169840785-oportunidad-de-remodelar-junto-a-metro-u-de-chile-_JM) | 2,300 | $93,988,465 | 67 | 34.33 | 53 | 2 | 0 | $120,000 | 2026-08-18 |
| [Departamento En Venta - Santiago Centro - Rafael Sotomayor](https://www.portalinmobiliario.com/MLC-2173240103-departamento-en-venta-santiago-centro-rafael-sotomayor-_JM) | 2,250 | $91,945,238 | 65 | 34.62 | 48 | 2 | 1 | $98,000 | 2026-08-19 |
| [Depto 3d 2b, Cueto 1221, Santiago](https://www.portalinmobiliario.com/MLC-2174695595-depto-3d-2b-cueto-1221-santiago-_JM) | 2,080 | $85,000,000 | 60 | 34.67 | 47 | 3 | 0 | $0 | 2026-08-19 |
| [Metro Parque O´higgins](https://www.portalinmobiliario.com/MLC-2183099611-metro-parque-ohiggins-_JM) | 1,690 | $69,061,090 | 48 | 35.21 | 74 | 2 | 0 | $55,000 | 2026-08-22 |
| [Nataniel Cox Depto En Venta 2 D / 1b](https://www.portalinmobiliario.com/MLC-4362191528-nataniel-cox-depto-en-venta-2-d-1b-_JM) | 1,835 | $75,000,000 | 52 | 35.29 | 54 | 2 | 0 | $61,000 | 2026-08-18 |
| [Cómodo Departamento En Quinta Normal](https://www.portalinmobiliario.com/MLC-2181839211-comodo-departamento-en-quinta-normal-_JM) | 1,805 | $73,750,000 | 51 | 35.39 | 68 | 3 | 0 | $80,000 | 2026-08-22 |
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
