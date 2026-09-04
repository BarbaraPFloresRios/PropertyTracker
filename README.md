# PropertyTracker

A real estate listing monitor built in Python. PropertyTracker scrapes apartment listings from [Portal Inmobiliario](https://www.portalinmobiliario.com) (Chile's largest real estate marketplace, owned by MercadoLibre), maintains a historical dataset of listings and prices, and detects newly published properties and price changes over time.

The long-term goal is to use this growing dataset to **detect personal real estate investment opportunities**: undervalued listings, price drops, and neighborhoods trending above or below their historical price per m².

## Interactive map

**[🗺️ Open the interactive map](https://barbarapfloresrios.github.io/PropertyTracker/map.html)** — recent listings colored by UF/m², with price, size and a link to each listing on hover/click. Regenerated on every pipeline run from `docs/map.html`.

## Latest listings

<!-- RECENT_LISTINGS:START -->
_Top 30 by UF/m² among listings first seen in the last 14 days (under 100 m², published within the last 30 days). Updated automatically from `data/recent_listings.csv`._

| Listing | UF | CLP | m² | UF/m² | Zona UF/m² | Beds | Parking | Common exp. | First Seen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Departamento Estudio En Excelente Ubicación](https://www.portalinmobiliario.com/MLC-2210033553-departamento-estudio-en-excelente-ubicacion-_JM) | 1,223 | $50,000,000 | 55 | 22.24 | 54 | 1 | 0 | $50 | 2026-09-01 |
| [Depto. Primer Piso, Tres Dormitorios, Estac. Compartido](https://www.portalinmobiliario.com/MLC-4417709810-depto-primer-piso-tres-dormitorios-estac-compartido-_JM) | 2,030 | $83,000,000 | 87 | 23.34 | 51 | 3 | 1 |  | 2026-08-28 |
| [Departamento/3d1b/usach/estacion Central/planetario](https://www.portalinmobiliario.com/MLC-2212103597-departamento3d1busachestacion-centralplanetario-_JM) | 1,712 | $70,000,000 | 73 | 23.46 | 48 | 3 | 0 |  | 2026-09-02 |
| [Departamento Antiguo (176985)](https://www.portalinmobiliario.com/MLC-4418552946-departamento-antiguo-176985-_JM) | 1,100 | $44,964,051 | 44 | 25.00 | 73 | 1 | 0 | $50,000 | 2026-08-28 |
| [Departamento Grande Pedro Lagos San Diego  (177976)](https://www.portalinmobiliario.com/MLC-4447964648-departamento-grande-pedro-lagos-san-diego-177976-_JM) | 1,800 | $73,577,538 | 70 | 25.71 | 54 | 2 | 0 | $40,000 | 2026-09-04 |
| [Acogedor Depto. En Condomiino Residencial](https://www.portalinmobiliario.com/MLC-4437185782-acogedor-depto-en-condomiino-residencial-_JM) | 1,290 | $52,730,569 | 49 | 26.33 | 68 | 1 | 0 | $55,000 | 2026-09-01 |
| [Acogedor Departamento, Piso Doce Incluye Bodega](https://www.portalinmobiliario.com/MLC-4417963028-acogedor-departamento-piso-doce-incluye-bodega-_JM) | 1,761 | $72,000,000 | 65 | 27.10 | 53 | 1 | 0 | $95,000 | 2026-08-28 |
| [Departamento Completamente Remodelado (144421)](https://www.portalinmobiliario.com/MLC-4445106614-departamento-completamente-remodelado-144421-_JM) | 1,650 | $67,446,076 | 60 | 27.50 | 54 | 2 | 0 | $15,000 | 2026-09-03 |
| [Vendo Dpto. Estudio Excelente Ubicación Con Bodega](https://www.portalinmobiliario.com/MLC-2210033561-vendo-dpto-estudio-excelente-ubicacion-con-bodega-_JM) | 1,297 | $53,000,000 | 45 | 28.81 | 74 | 1 | 0 | $50,000 | 2026-09-01 |
| [Departamento San Francisco Id: 137511](https://www.portalinmobiliario.com/MLC-4423667560-departamento-san-francisco-id-137511-_JM) | 1,590 | $65,000,000 | 55 | 28.91 | 61 | 2 | 0 | $5,000 | 2026-08-29 |
| [Departamento En Santiago Argomedo Remate 24 Septiembre 2026](https://www.portalinmobiliario.com/MLC-4421196724-departamento-en-santiago-argomedo-remate-24-septiembre-2026-_JM) | 905 | $37,006,145 | 31 | 29.20 | 82 | 1 | 0 |  | 2026-08-28 |
| [Cumming/ Balmaceda 2d 2b Terraza  (82859)](https://www.portalinmobiliario.com/MLC-2183115821-cumming-balmaceda-2d-2b-terraza-82859-_JM) | 2,000 | $81,752,820 | 68 | 29.41 | 47 | 2 | 0 | $90,000 | 2026-08-22 |
| [Dúplex 87 M², 5 Terrazas, 2d, 2b, Metro O'higgins](https://www.portalinmobiliario.com/MLC-4397551728-duplex-87-m-5-terrazas-2d-2b-metro-ohiggins-_JM) | 2,569 | $105,000,000 | 87 | 29.53 | 55 | 2 | 0 |  | 2026-08-25 |
| [Departamento 1 Dormitorio - 1 Baño ( Santa Ana - Santiago )](https://www.portalinmobiliario.com/MLC-4443916618-departamento-1-dormitorio-1-bano-santa-ana-santiago--_JM) | 1,600 | $65,402,256 | 54 | 29.63 |  | 1 | 0 |  | 2026-09-03 |
| [Venta Departamento 2hab 1ba Cercano A Estación De Metro](https://www.portalinmobiliario.com/MLC-4433068006-venta-departamento-2hab-1ba-cercano-a-estacion-de-metro-_JM) | 1,835 | $75,000,000 | 60 | 30.58 | 65 | 2 | 0 | $70,000 | 2026-08-31 |
| [Inersion ,comercial O Habutacional 2d/1b Maciver (180206)](https://www.portalinmobiliario.com/MLC-4397559286-inersion-comercial-o-habutacional-2d1b-maciver-180206-_JM) | 1,908 | $78,000,000 | 61 | 31.28 | 53 | 2 | 0 | $75,000 | 2026-08-25 |
| [Vendemos Departamento En Barrio Yungay,piso 17](https://www.portalinmobiliario.com/MLC-4410909834-vendemos-departamento-en-barrio-yungaypiso-17-_JM) | 1,346 | $55,000,000 | 43 | 31.29 | 66 | 1 | 0 | $50,000 | 2026-08-27 |
| [Oportunidad Para Remodelar Y Rentabilizar](https://www.portalinmobiliario.com/MLC-2213117975-oportunidad-para-remodelar-y-rentabilizar-_JM) | 1,880 | $76,847,651 | 60 | 31.33 | 53 | 2 | 0 | $80,000 | 2026-09-02 |
| [Departamento De Dos Dormitorios En Condominio Cerrado](https://www.portalinmobiliario.com/MLC-4449886610-departamento-de-dos-dormitorios-en-condominio-cerrado-_JM) | 2,200 | $89,928,102 | 70 | 31.43 | 48 | 2 | 0 | $75,000 | 2026-09-04 |
| [Luminoso Y Amplio Departamento Santiago](https://www.portalinmobiliario.com/MLC-2195804749-luminoso-y-amplio-departamento-santiago-_JM) | 3,060 | $125,081,815 | 94 | 32.55 | 56 | 3 | 1 | $0 | 2026-08-26 |
| [Oferta (174950)](https://www.portalinmobiliario.com/MLC-2217017499-oferta-174950-_JM) | 1,957 | $80,000,000 | 60 | 32.62 | 48 | 2 | 0 | $93,000 | 2026-09-04 |
| [Departamento San Antonio Id: 150326](https://www.portalinmobiliario.com/MLC-4441938264-departamento-san-antonio-id-150326-_JM) | 1,957 | $80,000,000 | 60 | 32.62 | 53 | 1 | 0 | $0 | 2026-09-02 |
| [Departamento En Venta De 3 Dorm. En Santiago](https://www.portalinmobiliario.com/MLC-4441913752-departamento-en-venta-de-3-dorm-en-santiago-_JM) | 1,600 | $65,402,256 | 49 | 32.65 | 72 | 3 | 1 | $80,000 | 2026-09-02 |
| [Departamento 2 Dormitorios En Condominio Cerrado. Santiago](https://www.portalinmobiliario.com/MLC-4428241946-departamento-2-dormitorios-en-condominio-cerrado-santiago-_JM) | 1,800 | $73,577,538 | 55 | 32.73 | 47 | 2 | 0 | $55,000 | 2026-08-30 |
| [Venta Depa 2 Dorm 1 Baño Zenteno, Santiago](https://www.portalinmobiliario.com/MLC-4430068580-venta-depa-2-dorm-1-bano-zenteno-santiago-_JM) | 1,490 | $60,905,851 | 45 | 33.11 | 72 | 2 | 0 | $0 | 2026-08-30 |
| [Toesca, Bascuñan Con Terraza](https://www.portalinmobiliario.com/MLC-2193319145-toesca-bascunan-con-terraza-_JM) | 2,028 | $82,900,000 | 61 | 33.25 | 48 | 3 | 0 | $160,000 | 2026-08-26 |
| [Venta Departamento 2d Y 2b Frente A Parque Los Reyes](https://www.portalinmobiliario.com/MLC-2194370419-venta-departamento-2d-y-2b-frente-a-parque-los-reyes-_JM) | 1,775 | $72,555,628 | 53 | 33.49 | 47 | 2 | 0 | $0 | 2026-08-26 |
| [Único 3 Dormitorios + Bodega Metro Rondizzoni (166664)](https://www.portalinmobiliario.com/MLC-4419209280-unico-3-dormitorios-bodega-metro-rondizzoni-166664-_JM) | 1,450 | $59,270,795 | 43 | 33.72 | 72 | 3 | 0 | $80,000 | 2026-08-28 |
| [Oportunidad  En El Corazón De Santiago Venta O Arriendo](https://www.portalinmobiliario.com/MLC-4419782700-oportunidad-en-el-corazon-de-santiago-venta-o-arriendo-_JM) | 2,030 | $83,000,000 | 60 | 33.84 | 48 | 2 | 0 | $70,000 | 2026-08-28 |
| [Acogedor Departamento 2d Con Vista Despejada En Santiago](https://www.portalinmobiliario.com/MLC-2211365947-acogedor-departamento-2d-con-vista-despejada-en-santiago-_JM) | 1,664 | $68,000,000 | 49 | 33.95 | 74 | 2 | 0 | $61,000 | 2026-09-01 |
<!-- RECENT_LISTINGS:END -->

## How it works

Each run:

* Scrapes all search result pages for the configured searches (no browser needed — the site embeds structured JSON in its HTML)
* Compares against the stored dataset by listing ID
* Reports **truly new listings** and **price changes** since the last run
* Tracks `first_seen_date`, `last_seen_date` and `first_seen_price` per listing
* Stores the full history in `data/raw/portalinmobiliario_listings.csv`
* Exports listings discovered in the last 14 days (under 100 m², sorted by UF/m²) to `data/recent_listings.csv`

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
