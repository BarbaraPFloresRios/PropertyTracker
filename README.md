# PropertyTracker

Monitor de propiedades en [Portal Inmobiliario](https://www.portalinmobiliario.com), con la misma lógica de JobTrackerChile: cada corrida scrapea los resultados de búsqueda, los contrasta contra lo ya guardado y reporta los avisos realmente nuevos y los cambios de precio.

## Uso

```bash
python3 main.py
```

Cada corrida:

* Scrapea todas las páginas de resultados de las búsquedas configuradas
* Detecta avisos nuevos (`listing_id` no visto antes) y los imprime
* Detecta cambios de precio contra la corrida anterior y los imprime
* Mantiene `first_seen_date` / `last_seen_date` y `first_seen_price` por aviso
* Guarda el histórico en `data/raw/portalinmobiliario_listings.csv`
* Exporta los avisos de los últimos 7 días a `data/recent_listings.csv`

## Datos capturados

Por cada aviso: título, precio (UF o CLP), dormitorios, baños, m² útiles, **UF/m²** (calculado), ubicación, tipo (usada / proyecto), link, y fechas de primera y última vez visto.

La fecha exacta de publicación no es pública en el sitio, pero corriendo el tracker a diario, `first_seen_date` la aproxima con precisión de un día.

## Configuración

Las búsquedas se definen en `scrapers/portalinmobiliario.py` (`SEARCHES`). Para agregar arriendo u otra comuna:

```python
SEARCHES = [
    {"operation": "venta", "property_type": "departamento", "location": "providencia-metropolitana"},
    {"operation": "arriendo", "property_type": "departamento", "location": "providencia-metropolitana"},
]
```

El slug de `location` es el que aparece en la URL del sitio al buscar la comuna.

## Notas

* No usa browser: el sitio devuelve el HTML con un JSON embebido (`_n.ctx.r=`) que contiene todos los datos de las tarjetas ya estructurados.
* Los avisos con `is_pad` (publicidad pagada) se excluyen porque suelen ser de otras comunas y duplican los orgánicos.
* En proyectos (edificios nuevos) los m² vienen como rango, por lo que `uf_per_m2` solo se calcula para propiedades con m² único.
* Una corrida diaria con pausa de 1s entre páginas (~70 requests) es un volumen respetuoso con el sitio.
