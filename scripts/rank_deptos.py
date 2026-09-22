#!/usr/bin/env python3
"""
Ranking de departamentos caminables al Costanera Center para Barbara.

Uso:
    cd ~/Desktop/projects/PropertyTracker && git pull && python3 scripts/rank_deptos.py

Fuente: data/raw/portalinmobiliario_listings.csv (set completo, NO recent_listings.csv).
Criterios y listas de exclusion viven en la memoria de Claude
(depto-search-criteria.md). Este script es la version ejecutable de esos criterios;
cuando Barbara descarta/confirma algo nuevo, actualizar los sets DESCARTADOS/CAIDOS/
KEEPALIVE/FAV/POR_VISITAR de abajo (o pedirle a Claude que lo haga).

NOTA: la vigencia real de cada link (Portal elimina avisos sin aviso) NO se puede
verificar aca -> Claude la confirma en el navegador solo para los finalistas.
"""
import pandas as pd, numpy as np, re, math, os

CSV = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "portalinmobiliario_listings.csv")

# ------------------------------------------------------------------ criterios
COSTANERA = (-33.4178, -70.6060)   # Av. Andres Bello
MAX_DIST_M = 1500                  # ~25 min a pie (tope de Barbara, "muy border")
MIN_M2_UTILES = 40
CAP_POR_COMUNA = {"las-condes-metropolitana": 230e6}  # resto -> 190e6
CAP_DEFAULT = 190e6
GC_TOPE = 150_000                  # aplica solo a GC con dato real
PARKING_UF = 300                   # estacionamiento valorizado en UF 300
WALK_FACTOR = 1.35                 # linea recta -> caminata real
WALK_KMH = 5

# ------------------------------------------- listas (sincronizar con memoria)
# ❌ descartados por Barbara (studios, edificios viejos, contacto imposible, etc.)
DESCARTADOS = {
    "4444442422", "2215990417", "2219776375", "4444272012", "2039845269",
    "2181858637", "4421808944", "4233323866", "4173826972", "4361692300",
    "4404451594",                       # studio confirmado
    "2201193555", "4350409898",         # edificio 60 anos
    "4445105284", "2217016181", "2217041959", "4437064058",  # Vecinal (visitada y descartada)
    "4191761666",                       # Tu Hogar Conectado = 4444272012, mismo corredor solo-telefono
    "4499467526", "2018312425",         # Precioso Dpto Remodelado 1D = Departamento Bucarest (misma unidad, piso5/48m2/UF~3660); edificio muy antiguo por fotos
}
# 🚫 caidos verificados (link muerto / redirectedFromVip / corredor dice no disponible)
CAIDOS = {
    "4450271144", "2228842067", "2187517135", "4427322334",
    "4499455338", "2256990123", "4451784562", "4403479822", "4486979384",
    "4394177382",                       # El Golf Centro Financiero: pausada sin ficha 2026-09-22, misma unidad = 4495764082 (esa sigue viva)
}
# verificados VIVOS aunque el CSV los marque delisted (falso positivo) -> rescatar
KEEPALIVE = set()                   # Coronel (4404154390) sacada 2026-09-22: pagina ahora sin ficha (posible vendida)
# ⭐ favoritas / visitadas y 👀 por visitar (solo para marcar el estado)
FAV = {"4404154390", "2231564131", "4441100684", "2246908357"}
POR_VISITAR = {"4495764082"}

EXCLUIR = DESCARTADOS | CAIDOS

# ------------------------------------------------------------------ helpers
def haversine_m(lat, lng):
    if pd.isna(lat) or pd.isna(lng):
        return np.nan
    R = 6_371_000
    p1, p2 = math.radians(lat), math.radians(COSTANERA[0])
    dphi = math.radians(COSTANERA[0] - lat)
    dl = math.radians(COSTANERA[1] - lng)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def norm_id(x):
    return re.sub(r"\D", "", str(x))

def calle(loc):
    return "" if pd.isna(loc) else re.split(r"\d", str(loc).lower())[0].strip()

def banda(d):
    return "A" if d <= 700 else ("B" if d <= 1200 else "C")

# ------------------------------------------------------------------ pipeline
def main():
    df = pd.read_csv(CSV)
    df["id"] = df["listing_id"].apply(norm_id)
    df["dist"] = df.apply(lambda r: haversine_m(r["lat"], r["lng"]), axis=1)
    df["walk"] = df["dist"] * WALK_FACTOR / (WALK_KMH * 1000) * 60

    data_date = pd.to_datetime(df["last_seen_date"], errors="coerce").max()
    data_date = None if pd.isna(data_date) else data_date.date().isoformat()

    f = df[df["property_type"].astype(str).str.lower().eq("departamento")].copy()
    f = f[~f["title"].astype(str).str.lower().str.contains("oficina", na=False)]
    f = f[f["bedrooms_n"] >= 1]
    f = f[f["m2_utiles"] > MIN_M2_UTILES]
    f = f[f["dist"] <= MAX_DIST_M]
    activo = f["delisted_date"].isna() & f["finished_date"].isna()
    f = f[activo | f["id"].isin(KEEPALIVE)]
    f = f[f["comuna"].isin(["providencia-metropolitana", "las-condes-metropolitana"])]
    f = f[f["price_clp"].notna() &
          (f["price_clp"] <= f["comuna"].apply(lambda c: CAP_POR_COMUNA.get(c, CAP_DEFAULT)))]
    gc = f["gastos_comunes_clp"]
    # GC del dataset es poco confiable -> <= tope (incluye los "al borde" como El Golf 150k)
    f = f[(gc.isna() | (gc <= 1)) | (gc <= GC_TOPE)]
    f = f[~f["id"].isin(EXCLUIR)]

    f["pk"] = f["parking"].fillna(0)
    f["adj"] = (f["price_uf"] - PARKING_UF * f["pk"]) / f["m2_utiles"]

    # dedup: 1) por coords+m2+dorm (caza republicaciones multi-corredor), 2) backstop calle+precio+dorm
    f["la5"] = f["lat"].round(5); f["ln5"] = f["lng"].round(5)
    f = f.sort_values("adj").drop_duplicates(["la5", "ln5", "m2_utiles", "bedrooms_n"], keep="first")
    f["calle"] = f["location"].apply(calle)
    f = f.sort_values("adj").drop_duplicates(["calle", "price_uf", "bedrooms_n"], keep="first")
    f = f.sort_values("adj").reset_index(drop=True)

    def estado(i):
        return "*fav" if i in FAV else ("o vis" if i in POR_VISITAR else "")

    def fmt(r):
        g = r["gastos_comunes_clp"]
        gs = "s/d" if (pd.isna(g) or g <= 1) else f"{int(g/1000)}k"
        new = "NEW" if (data_date and r["first_seen_date"] == data_date) else ""
        return (f"  adj{r['adj']:>3.0f} | {r['walk']:>2.0f}min | {int(r['bedrooms_n'])}D/{int(r['m2_utiles'])} | "
                f"{r['price_clp']/1e6:>3.0f}M | GC{gs:>4} | est{int(r['pk'])} | "
                f"{r['comuna'].replace('-metropolitana','')[:4]} | {estado(r['id']):<5} {new:<3} | "
                f"MLC-{r['id']}\n      {r['url']}")

    print(f"Data: {data_date} | pasan filtros (<= {MAX_DIST_M} m): {len(f)}\n")
    if data_date:
        nuevos = f[f["first_seen_date"] == data_date]
        print(f"NUEVOS hoy (first_seen == {data_date}): {len(nuevos)}")
        for _, r in nuevos.iterrows():
            print(fmt(r))
        print()
    for b, lbl in [("A", "A  <=700m (<=10 min)  SWEET SPOT"),
                   ("B", "B  700-1200m (10-20 min)"),
                   ("C", "C  1200-1500m (20-25 min)  border")]:
        sub = f[f["dist"].apply(banda) == b]
        print(f"== {lbl}  ({len(sub)}) ==")
        for _, r in sub.iterrows():
            print(fmt(r))
        print()
    print("RECORDAR: antiguedad y GC del dataset NO son confiables; estado real solo por "
          "fotos/visita; verificar vigencia de links en navegador (Portal elimina avisos sin marcar).")

if __name__ == "__main__":
    main()
