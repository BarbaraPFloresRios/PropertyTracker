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
| [Departamento Portugal 564 Metro Santa Isabel  (178033)](https://www.portalinmobiliario.com/MLC-2114827717-departamento-portugal-564-metro-santa-isabel-178033-_JM) | 1,861 | $76,000,000 | 41 | 45.38 | 81 | 2 | 0 | $90,000 | 2026-08-05 |
| [Departamento En Venta De 3 Dorm. En Providencia](https://www.portalinmobiliario.com/MLC-4288411968-departamento-en-venta-de-3-dorm-en-providencia-_JM) | 5,200 | $212,392,908 | 98 | 53.06 | 94 | 3 | 0 | $140,000 | 2026-08-05 |
| [Primer Piso Con Patio !!!](https://www.portalinmobiliario.com/MLC-2116719077-primer-piso-con-patio--_JM) | 4,290 | $175,224,149 | 75 | 57.20 |  | 3 | 0 |  | 2026-08-05 |
| [En La Mejor Ubicación De Providencia (178133)](https://www.portalinmobiliario.com/MLC-4293357458-en-la-mejor-ubicacion-de-providencia-178133-_JM) | 4,040 | $165,000,000 | 70 | 57.71 | 98 | 3 | 0 | $120,000 | 2026-08-05 |
| [Providencia 3 Dormitorios Remodelado Impecable](https://www.portalinmobiliario.com/MLC-2116481019-providencia-3-dormitorios-remodelado-impecable-_JM) | 4,990 | $203,815,502 | 85 | 58.71 | 80 |  | 0 | $110,000 | 2026-08-05 |
| [Venta Departamento 1er Piso 3d 2b Y Patio - I.suárez - Prov](https://www.portalinmobiliario.com/MLC-2114829595-venta-departamento-1er-piso-3d-2b-y-patio-isuarez-prov-_JM) | 5,264 | $215,006,975 | 85 | 61.93 | 85 | 3 | 0 | $0 | 2026-08-05 |
| [Excelente Dpto 3d / 2b En Av. Providencia (144751)](https://www.portalinmobiliario.com/MLC-2117563231-excelente-dpto-3d-2b-en-av-providencia-144751-_JM) | 4,407 | $180,000,000 | 66 | 66.77 | 98 | 3 | 0 | $90,000 | 2026-08-05 |
| [Vendo Hermoso Departamento Vintage 3d Y 2b Providencia](https://www.portalinmobiliario.com/MLC-2117553791-vendo-hermoso-departamento-vintage-3d-y-2b-providencia-_JM) | 5,740 | $234,449,095 | 82 | 70.00 | 94 | 3 | 0 | $60,000 | 2026-08-05 |
| [Departamento De 2 Dormitorios En Infante Y Eliodoro Yañez !](https://www.portalinmobiliario.com/MLC-4288408906-departamento-de-2-dormitorios-en-infante-y-eliodoro-yanez--_JM) | 4,600 | $187,886,034 | 64 | 71.88 | 98 | 2 | 1 | $0 | 2026-08-05 |
| [Venta Departamento 3hab 2ba Providencia](https://www.portalinmobiliario.com/MLC-4288254850-venta-departamento-3hab-2ba-providencia-_JM) | 6,800 | $277,744,572 | 93 | 73.12 | 85 | 3 | 1 | $200,000 | 2026-08-05 |
| [Oportunidad Única En Barrio Los Dominicos (174361)](https://www.portalinmobiliario.com/MLC-2117548881-oportunidad-unica-en-barrio-los-dominicos-174361-_JM) | 7,200 | $294,082,488 | 95 | 75.79 | 96 | 4 | 1 | $142,000 | 2026-08-05 |
| [Depto Cercano Al Colegio Verbo Divino (178089)](https://www.portalinmobiliario.com/MLC-4292455906-depto-cercano-al-colegio-verbo-divino-178089-_JM) | 6,500 | $265,491,135 | 85 | 76.47 | 95 | 3 | 0 | $100,000 | 2026-08-05 |
| [2d,2b,1bod - Metro Parque Bustamante](https://www.portalinmobiliario.com/MLC-2115961955-2d2b1bod-metro-parque-bustamante-_JM) | 6,900 | $281,829,051 | 90 | 76.67 | 73 | 2 | 0 | $100,000 | 2026-08-05 |
| [¡el Departamento Ideal Para Comenzar A Proyectar Tu Futuro!](https://www.portalinmobiliario.com/MLC-2114828303-el-departamento-ideal-para-comenzar-a-proyectar-tu-futuro-_JM) | 6,000 | $245,068,740 | 77 | 77.92 | 103 | 3 | 1 | $140,000 | 2026-08-05 |
| [Ubicación Privilegiada](https://www.portalinmobiliario.com/MLC-4292417168-ubicacion-privilegiada-_JM) | 7,500 | $306,335,925 | 96 | 78.12 | 148 | 3 | 1 | $130,000 | 2026-08-05 |
| [Moderno Seminuevo, Posible Tasación Tasa Fija 2.1%](https://www.portalinmobiliario.com/MLC-2116518335-moderno-seminuevo-posible-tasacion-tasa-fija-21-_JM) | 7,990 | $326,349,872 | 99 | 80.71 | 85 | 2 | 1 |  | 2026-08-05 |
| [Atencion Inversionista Departamento 3 Dormitorios Las Condes](https://www.portalinmobiliario.com/MLC-2117565135-atencion-inversionista-departamento-3-dormitorios-las-condes-_JM) | 7,490 | $305,927,477 | 90 | 83.22 | 102 | 3 | 1 | $160,000 | 2026-08-05 |
| [Oficina / Estudio De 12m² Con Luz Natural](https://www.portalinmobiliario.com/MLC-4292443466-oficina-estudio-de-12m-con-luz-natural-_JM) | 1,000 | $40,844,790 | 12 | 83.33 | 158 |  | 0 | $0 | 2026-08-05 |
| [Colón / Málaga, 3 Dormitorios ¡exclusivo! (168606)](https://www.portalinmobiliario.com/MLC-2117562109-colon-malaga-3-dormitorios-exclusivo-168606-_JM) | 7,900 | $322,673,841 | 94 | 84.04 | 95 | 3 | 2 | $180,000 | 2026-08-05 |
| [Moderno Depto En Venta, Gran Conectividad!](https://www.portalinmobiliario.com/MLC-4292443790-moderno-depto-en-venta-gran-conectividad-_JM) | 7,900 | $322,673,841 | 93 | 84.95 | 89 | 3 | 1 | $0 | 2026-08-05 |
| [Depto Venta. Av. Los Leones, Excelente Precio!!](https://www.portalinmobiliario.com/MLC-2115957771-depto-venta-av-los-leones-excelente-precio-_JM) | 7,390 | $301,842,998 | 86 | 85.93 | 85 | 3 | 1 | $217,000 | 2026-08-05 |
| [Bello Departamento Recien Remodelado, Insuperable](https://www.portalinmobiliario.com/MLC-4293422560-bello-departamento-recien-remodelado-insuperable-_JM) | 4,300 | $175,632,597 | 50 | 86.00 | 155 | 1 | 1 | $110,000 | 2026-08-05 |
| [Departamento Con Muy Buenos Espacios En El Golf/burgos](https://www.portalinmobiliario.com/MLC-4292443124-departamento-con-muy-buenos-espacios-en-el-golfburgos-_JM) | 8,450 | $345,138,476 | 97 | 87.11 | 95 | 4 | 1 | $150,000 | 2026-08-05 |
| [Metro Manquehue - Loft 1d,2b, Est Y Bod](https://www.portalinmobiliario.com/MLC-2115961981-metro-manquehue-loft-1d2b-est-y-bod-_JM) | 6,200 | $253,237,698 | 70 | 88.57 | 111 | 1 | 1 | $180,000 | 2026-08-05 |
| [Departamento En Venta De 3 Dormitorios En Las Condes](https://www.portalinmobiliario.com/MLC-2114834811-departamento-en-venta-de-3-dormitorios-en-las-condes-_JM) | 7,590 | $310,011,956 | 85 | 89.29 |  | 3 | 0 |  | 2026-08-05 |
| [Depto 2 Dorm + 1 Baño, Cocina Renovada Providencia](https://www.portalinmobiliario.com/MLC-4292453078-depto-2-dorm-1-bano-cocina-renovada-providencia-_JM) | 5,600 | $228,730,824 | 62 | 90.32 | 84 | 2 | 1 | $280,000 | 2026-08-05 |
| [Venta Depto. 1d-2b 1e Remodelado Providencia Metro M Montt](https://www.portalinmobiliario.com/MLC-2116519603-venta-depto-1d-2b-1e-remodelado-providencia-metro-m-montt-_JM) | 5,990 | $244,660,292 | 66 | 90.76 | 98 | 1 | 1 | $120,000 | 2026-08-05 |
| [3 Hab 3 B 1 Estacionamiento, Bodega Y Oficina Privada](https://www.portalinmobiliario.com/MLC-2117579979-3-hab-3-b-1-estacionamiento-bodega-y-oficina-privada-_JM) | 8,990 | $367,194,662 | 98 | 91.73 | 103 | 3 | 1 | $250,000 | 2026-08-05 |
| [Depto En Venta De 3d 3b, Oficina Tipo Staf. En Las Condes](https://www.portalinmobiliario.com/MLC-4288405688-depto-en-venta-de-3d-3b-oficina-tipo-staf-en-las-condes-_JM) | 9,000 | $367,603,110 | 98 | 91.84 | 102 | 3 | 1 | $0 | 2026-08-05 |
| [Remodelado En Barrio Las Lilas 3 Dorm 2 Baños Estac & Bodega](https://www.portalinmobiliario.com/MLC-4292444640-remodelado-en-barrio-las-lilas-3-dorm-2-banos-estac-bodega-_JM) | 8,200 | $334,927,278 | 89 | 92.13 | 95 | 3 | 1 | $290,000 | 2026-08-05 |
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
