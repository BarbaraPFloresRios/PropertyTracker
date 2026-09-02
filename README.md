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
| [Departamento Antiguo (176985)](https://www.portalinmobiliario.com/MLC-4418552946-departamento-antiguo-176985-_JM) | 1,100 |  | 44 | 25.00 | 73 | 1 | 0 | $50,000 | 2026-08-28 |
| [Acogedor Depto. En Condomiino Residencial](https://www.portalinmobiliario.com/MLC-4437185782-acogedor-depto-en-condomiino-residencial-_JM) | 1,290 |  | 49 | 26.33 | 68 | 1 | 0 | $55,000 | 2026-09-01 |
| [Oportunidad Para Remodelar Y Rentabilizar](https://www.portalinmobiliario.com/MLC-2213117975-oportunidad-para-remodelar-y-rentabilizar-_JM) | 1,880 |  | 60 | 31.33 | 53 | 2 | 0 | $80,000 | 2026-09-02 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4441913752-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 1,600 |  | 49 | 32.65 | 72 | 3 | 1 | $80,000 | 2026-09-02 |
| [Departamento 2 Dormitorios En Condominio Cerrado. Santiago](https://www.portalinmobiliario.com/MLC-4428241946-departamento-2-dormitorios-en-condominio-cerrado-santiago-_JM) | 1,800 |  | 55 | 32.73 | 47 | 2 | 0 | $55,000 | 2026-08-30 |
| [Venta Depa 2 Dorm 1 Baño Zenteno, Santiago](https://www.portalinmobiliario.com/MLC-4430068580-venta-depa-2-dorm-1-bano-zenteno-santiago-_JM) | 1,490 |  | 45 | 33.11 | 72 | 2 | 0 | $0 | 2026-08-30 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (166664)](https://www.portalinmobiliario.com/MLC-4419209280-unico-3-dormitorios-bodega-metro-rondizzoni-166664-_JM) | 1,450 |  | 43 | 33.72 | 72 | 3 | 0 | $80,000 | 2026-08-28 |
| [Real Oportunidad  2.450 Uf  71 M2  3 Dormitorios / 2 Baño](https://www.portalinmobiliario.com/MLC-4434841762-real-oportunidad-2450-uf-71-m2-3-dormitorios-2-bano-_JM) | 2,450 |  | 71 | 34.51 | 54 | 3 | 1 | $45,000 | 2026-08-31 |
| [Depto 2 Dormitorios 2 Baños Vista Despejada Parque Los Reyes](https://www.portalinmobiliario.com/MLC-4428251344-depto-2-dormitorios-2-banos-vista-despejada-parque-los-reyes-_JM) | 2,137 |  | 60 | 35.62 | 47 | 2 | 0 | $0 | 2026-08-30 |
| [Inversión Segura En Entorno Privilegiado (177305)](https://www.portalinmobiliario.com/MLC-2205295335-inversion-segura-en-entorno-privilegiado-177305-_JM) | 1,900 |  | 53 | 35.85 | 65 | 2 | 0 | $80,000 | 2026-08-30 |
| [Oportunidad Para Invertir En Santiago](https://www.portalinmobiliario.com/MLC-4430391272-oportunidad-para-invertir-en-santiago-_JM) | 1,399 |  | 39 | 35.87 | 74 | 2 | 0 | $55,000 | 2026-08-31 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2196894795-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 2,890 |  | 80 | 36.12 | 55 | 3 | 0 | $0 | 2026-08-27 |
| [Departamento Libertad Id: 158886](https://www.portalinmobiliario.com/MLC-4422153388-departamento-libertad-id-158886-_JM) | 2,320 | $94,830,209 | 64 | 36.25 | 47 | 3 | 0 | $65,000 | 2026-08-29 |
| [Gran Departamento 3d+2b Estac Y Bodega](https://www.portalinmobiliario.com/MLC-4436479828-gran-departamento-3d2b-estac-y-bodega-_JM) | 2,800 |  | 77 | 36.36 | 51 | 3 | 1 | $128,000 | 2026-09-01 |
| [Oportunidad Rebajado!!! Acogedor Departamento Barrio Yungay](https://www.portalinmobiliario.com/MLC-4421860068-oportunidad-rebajado-acogedor-departamento-barrio-yungay-_JM) | 1,650 |  | 45 | 36.67 | 66 | 2 | 0 | $60,000 | 2026-08-29 |
| [Inversionistas Venta De Depto En Toesca](https://www.portalinmobiliario.com/MLC-4425460054-inversionistas-venta-de-depto-en-toesca-_JM) | 1,400 |  | 38 | 36.84 | 68 | 1 | 0 | $40,000 | 2026-08-29 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-2196891963-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 3,180 |  | 86 | 36.98 | 55 | 3 | 0 | $60,000 | 2026-08-27 |
| [Precio Liquidación Inversionistas Departamento 3d,1b](https://www.portalinmobiliario.com/MLC-4439742534-precio-liquidacion-inversionistas-departamento-3d1b-_JM) | 1,910 |  | 51 | 37.45 | 74 | 3 | 0 | $125,000 | 2026-09-01 |
| [Oportunidad Inversionista 2d1b Santiago](https://www.portalinmobiliario.com/MLC-2196956031-oportunidad-inversionista-2d1b-santiago-_JM) | 1,390 |  | 37 | 37.57 | 74 | 2 | 0 | $55,000 | 2026-08-27 |
| [Cómodo Departamento A Pasos Del Parque O'higgins](https://www.portalinmobiliario.com/MLC-2212095841-comodo-departamento-a-pasos-del-parque-ohiggins-_JM) | 1,882 |  | 50 | 37.64 | 72 | 2 | 0 | $95,000 | 2026-09-02 |
| [Departamento A Pasos Del Metro La Moneda](https://www.portalinmobiliario.com/MLC-4421809588-departamento-a-pasos-del-metro-la-moneda-_JM) | 3,390 |  | 90 | 37.67 | 50 | 3 | 0 | $78,000 | 2026-08-29 |
| [Departamento De 2 Dormitorios Y 1 Baño A Pasos Del Metro](https://www.portalinmobiliario.com/MLC-2203503059-departamento-de-2-dormitorios-y-1-bano-a-pasos-del-metro-_JM) | 2,500 |  | 66 | 37.88 | 54 | 2 | 0 | $0 | 2026-08-29 |
| [Excelente Depto 3d/1b En Santiago, En Calle Nataniel Cox](https://www.portalinmobiliario.com/MLC-4430391226-excelente-depto-3d1b-en-santiago-en-calle-nataniel-cox-_JM) | 2,200 |  | 58 | 37.93 | 54 | 3 | 0 | $60,000 | 2026-08-31 |
| [Depto 3d 1b Oriente 41m2 Herrera Esq San Pablo Rebajado!](https://www.portalinmobiliario.com/MLC-4414862004-depto-3d-1b-oriente-41m2-herrera-esq-san-pablo-rebajado-_JM) | 1,560 |  | 41 | 38.05 | 66 | 3 | 0 | $38,000 | 2026-08-27 |
| [Inversion Segura A Pasos De Metro Linea 7](https://www.portalinmobiliario.com/MLC-4437063866-inversion-segura-a-pasos-de-metro-linea-7-_JM) | 2,300 |  | 60 | 38.33 | 47 | 2 | 0 | $100,000 | 2026-09-01 |
| [Departamento 2 Dormitorios Plaza De Armas](https://www.portalinmobiliario.com/MLC-4437055102-departamento-2-dormitorios-plaza-de-armas-_JM) | 2,500 |  | 65 | 38.46 | 53 | 2 | 0 | $110,000 | 2026-09-01 |
| [Venta Ubicacion Estrategica Depto 50 M2 Cerca De Metro Ula](https://www.portalinmobiliario.com/MLC-2203504099-venta-ubicacion-estrategica-depto-50-m2-cerca-de-metro-ula-_JM) | 1,848 |  | 48 | 38.50 | 68 | 3 | 0 | $50,000 | 2026-08-29 |
| [Tu Proxima Propiedad  De Inversion Esta  Aqui!!](https://www.portalinmobiliario.com/MLC-4416375912-tu-proxima-propiedad-de-inversion-esta-aqui-_JM) | 1,700 |  | 44 | 38.64 | 74 | 2 | 0 | $120,000 | 2026-08-27 |
| [Inversión Venta 2 Dormitorios 2 Baños Terraza](https://www.portalinmobiliario.com/MLC-4439468150-inversion-venta-2-dormitorios-2-banos-terraza-_JM) | 1,700 |  | 44 | 38.64 | 72 | 2 | 0 | $80,000 | 2026-09-01 |
| [Se Vende Departamento Av. Balmaceda, Santiago](https://www.portalinmobiliario.com/MLC-4409961016-se-vende-departamento-av-balmaceda-santiago-_JM) | 2,400 |  | 62 | 38.71 | 47 | 2 | 1 | $170,000 | 2026-08-27 |
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
