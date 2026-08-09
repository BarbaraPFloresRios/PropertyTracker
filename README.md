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
| [Departamento En Venta De 2 Dorm. En Las Condes](https://www.portalinmobiliario.com/MLC-2109940269-departamento-en-venta-de-2-dorm-en-las-condes-_JM) | 3,305 | $135,000,000 | 60 | 55.09 | 84 | 2 | 0 | $17,000 | 2026-08-03 |
| [Primer Piso Con Patio !!!](https://www.portalinmobiliario.com/MLC-2116719077-primer-piso-con-patio--_JM) | 4,290 | $175,224,149 | 75 | 57.20 |  | 3 | 0 |  | 2026-08-05 |
| [En La Mejor Ubicación De Providencia (178133)](https://www.portalinmobiliario.com/MLC-4293357458-en-la-mejor-ubicacion-de-providencia-178133-_JM) | 4,040 | $165,000,000 | 70 | 57.71 | 98 | 3 | 0 | $120,000 | 2026-08-05 |
| [Providencia 3 Dormitorios Remodelado Impecable](https://www.portalinmobiliario.com/MLC-2116481019-providencia-3-dormitorios-remodelado-impecable-_JM) | 4,990 | $203,815,502 | 85 | 58.71 | 80 |  | 0 | $110,000 | 2026-08-05 |
| [La Mejor Ubicacion En Providencia](https://www.portalinmobiliario.com/MLC-2112558505-la-mejor-ubicacion-en-providencia-_JM) | 5,141 | $210,000,000 | 84 | 61.21 | 94 | 4 | 0 | $60,000 | 2026-08-04 |
| [Venta Departamento 1er Piso 3d 2b Y Patio - I.suárez - Prov](https://www.portalinmobiliario.com/MLC-2114829595-venta-departamento-1er-piso-3d-2b-y-patio-isuarez-prov-_JM) | 5,264 | $215,006,975 | 85 | 61.93 | 85 | 3 | 0 | $0 | 2026-08-05 |
| [Moderno Depto En Corazón De Las Condes (173909)](https://www.portalinmobiliario.com/MLC-4282528264-moderno-depto-en-corazon-de-las-condes-173909-_JM) | 5,600 | $228,730,824 | 90 | 62.22 | 89 | 3 | 1 | $80,000 | 2026-08-03 |
| [Oportunidad Inversionistas!!!](https://www.portalinmobiliario.com/MLC-4282527870-oportunidad-inversionistas-_JM) | 1,910 | $78,000,000 | 30 | 63.66 | 82 | 1 | 0 | $70,000 | 2026-08-03 |
| [Venta Departamento Remodelar 3d 2b - Las Condes](https://www.portalinmobiliario.com/MLC-2111608055-venta-departamento-remodelar-3d-2b-las-condes-_JM) | 4,897 | $200,000,000 | 75 | 65.29 | 107 | 3 | 1 | $110 | 2026-08-04 |
| [Excelente Dpto 3d / 2b En Av. Providencia (144751)](https://www.portalinmobiliario.com/MLC-2117563231-excelente-dpto-3d-2b-en-av-providencia-144751-_JM) | 4,407 | $180,000,000 | 66 | 66.77 | 98 | 3 | 0 | $90,000 | 2026-08-05 |
| [Excelente Dpto Antiguo Tres Dormitorios, Dos Mas Servicio.](https://www.portalinmobiliario.com/MLC-4286779538-excelente-dpto-antiguo-tres-dormitorios-dos-mas-servicio-_JM) | 4,407 | $180,000,000 | 65 | 67.80 | 103 | 3 | 1 | $50 | 2026-08-04 |
| [Vendo Hermoso Departamento Vintage 3d Y 2b Providencia](https://www.portalinmobiliario.com/MLC-2117553791-vendo-hermoso-departamento-vintage-3d-y-2b-providencia-_JM) | 5,740 | $234,449,095 | 82 | 70.00 | 94 | 3 | 0 | $60,000 | 2026-08-05 |
| [Espectacular Loft En Venta Providencia Parque Ines De Suarez](https://www.portalinmobiliario.com/MLC-2112167761-espectacular-loft-en-venta-providencia-parque-ines-de-suarez-_JM) | 4,250 | $173,590,358 | 60 | 70.83 | 84 | 1 | 0 | $140,000 | 2026-08-04 |
| [Departamento En Venta De 3 Dorm. En Las Condes](https://www.portalinmobiliario.com/MLC-2111012337-departamento-en-venta-de-3-dorm-en-las-condes-_JM) | 6,000 | $245,068,740 | 84 | 71.43 | 96 | 3 | 1 | $120,000 | 2026-08-04 |
| [Venta Departamento Remodelar 3d 2b - Las Condes](https://www.portalinmobiliario.com/MLC-2111011567-venta-departamento-remodelar-3d-2b-las-condes-_JM) | 5,386 | $220,000,000 | 75 | 71.82 | 107 | 3 | 1 | $110 | 2026-08-04 |
| [Departamento De 2 Dormitorios En Infante Y Eliodoro Yañez !](https://www.portalinmobiliario.com/MLC-4288408906-departamento-de-2-dormitorios-en-infante-y-eliodoro-yanez--_JM) | 4,600 | $187,886,034 | 64 | 71.88 | 98 | 2 | 1 | $0 | 2026-08-05 |
| [Amplio 4 Dorm + 3 Baños + Est + Bod (174263)](https://www.portalinmobiliario.com/MLC-4287837846-amplio-4-dorm-3-banos-est-bod-174263-_JM) | 5,990 | $244,660,292 | 83 | 72.17 | 93 | 4 | 1 | $120,000 | 2026-08-04 |
| [Venta Departamento 3hab 2ba Providencia](https://www.portalinmobiliario.com/MLC-4288254850-venta-departamento-3hab-2ba-providencia-_JM) | 6,800 | $277,744,572 | 93 | 73.12 | 85 | 3 | 1 | $200,000 | 2026-08-05 |
| [Rebajada ! Oportunidad Av Pocuro / Metro Inés De Suarez](https://www.portalinmobiliario.com/MLC-2114826863-rebajada-oportunidad-av-pocuro-metro-ines-de-suarez-_JM) | 6,800 | $277,744,572 | 93 | 73.12 | 85 | 3 | 1 | $200,000 | 2026-08-04 |
| [Oportunidad De 3 Dormitorios En Metro El Golf](https://www.portalinmobiliario.com/MLC-2112620379-oportunidad-de-3-dormitorios-en-metro-el-golf-_JM) | 7,250 | $296,124,728 | 98 | 73.98 | 100 | 3 | 1 | $250,000 | 2026-08-04 |
| [Venta Departamento Cerca Metro Ines De Suarez](https://www.portalinmobiliario.com/MLC-4288251070-venta-departamento-cerca-metro-ines-de-suarez-_JM) | 5,100 | $208,308,429 | 68 | 75.00 | 103 | 3 | 50 | $80,000 | 2026-08-04 |
| [Oportunidad Única En Barrio Los Dominicos (174361)](https://www.portalinmobiliario.com/MLC-2117548881-oportunidad-unica-en-barrio-los-dominicos-174361-_JM) | 7,200 | $294,082,488 | 95 | 75.79 | 96 | 4 | 1 | $142,000 | 2026-08-05 |
| [Departamento En ¡ Venta ! Providencia](https://www.portalinmobiliario.com/MLC-4286578120-departamento-en-venta-providencia-_JM) | 3,650 | $149,083,484 | 48 | 76.04 | 81 | 2 | 0 |  | 2026-08-04 |
| [Cómodo Y Cálido Departamento Ubicado En Excelente ...](https://www.portalinmobiliario.com/MLC-4286171616-comodo-y-calido-departamento-ubicado-en-excelente--_JM) | 5,500 | $224,646,345 | 72 | 76.39 | 84 | 2 | 0 | $105,000 | 2026-08-04 |
| [Depto Cercano Al Colegio Verbo Divino (178089)](https://www.portalinmobiliario.com/MLC-4292455906-depto-cercano-al-colegio-verbo-divino-178089-_JM) | 6,500 | $265,491,135 | 85 | 76.47 | 95 | 3 | 0 | $100,000 | 2026-08-05 |
| [2d,2b,1bod - Metro Parque Bustamante](https://www.portalinmobiliario.com/MLC-2115961955-2d2b1bod-metro-parque-bustamante-_JM) | 6,900 | $281,829,051 | 90 | 76.67 | 73 | 2 | 0 | $100,000 | 2026-08-05 |
| [¡el Departamento Ideal Para Comenzar A Proyectar Tu Futuro!](https://www.portalinmobiliario.com/MLC-2114828303-el-departamento-ideal-para-comenzar-a-proyectar-tu-futuro-_JM) | 6,000 | $245,068,740 | 77 | 77.92 | 103 | 3 | 1 | $140,000 | 2026-08-05 |
| [Venta Departamento 1er Piso 2d 2b Oficina Y Patio - I.suáre](https://www.portalinmobiliario.com/MLC-2112239807-venta-departamento-1er-piso-2d-2b-oficina-y-patio-isuare-_JM) | 5,390 | $220,153,418 | 69 | 78.12 | 84 | 3 | 0 | $80,000 | 2026-08-04 |
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
