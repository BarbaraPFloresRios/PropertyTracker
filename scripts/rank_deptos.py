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
MIN_M2_UTILES = 40                 # inclusivo (>=): Barbara lo cambio 2026-10-05 de ">40" a ">=40" porque
                                   # los 40m2 exactos seguian apareciendo uno a uno como excepcion manual
                                   # (Pio X, y MLC-4541838686 que quedo fuera del ranking del 5-oct por 0,0 m2)
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
    "2201193555", "4350409898", "2268778815",  # edificio 60 anos (2268778815 = republicacion 23-sep, mismas coords/piso/precio, mismo corredor Binexxos)
    "4445105284", "2217016181", "2217041959", "4437064058",  # Vecinal (visitada y descartada)
    "4191761666",                       # Tu Hogar Conectado = 4444272012, mismo corredor solo-telefono
    "4499467526", "2018312425",         # Precioso Dpto Remodelado 1D = Departamento Bucarest (misma unidad, piso5/48m2/UF~3660); edificio muy antiguo por fotos
    "4490288254",                       # Departamento Estudio En Barrio El Golf - Cbg: es studio (titulo lo dice)
    "4495764082",                       # El Golf Centro Financiero: 38 anos + GC 150k al tope + 0 estacionamiento
    "4510792888",                       # = 4495764082 republicado (mismas coords/piso/m2/precio/GC/antiguedad/0 est)
    "4502089232",                       # Av. Nueva Providencia/Los Leones: zona muy concurrida + edificio muy viejo (64 anos) -- NOTA 26-sep: Barbara dice que "avenida transitada" lo debe juzgar ELLA con fotos/calle exacta, no un filtro automatico. Este caso queda como esta (ya asumido hace dias) pero NO repetir el patron para nuevos candidatos -- ver 4513678986/4514087776 abajo, restaurados al ranking.
    "2275685999",                       # Hernando de Aguirre: descripcion dice "departamento estudio" (marcado 1D en dataset)
    "4513678986",                       # Torres Carlos Antunez, Av. Providencia: 57 anos, DESCARTADO por Barbara
                                         # 2026-09-27 -- edificio demasiado antiguo, teme problemas de canerias/estilo.
                                         # (Distinto del caso 4514087776: ese lo evalua ella con fotos, no se
                                         # descarto solo por la avenida; este lo descarto ella misma por la edad.)
    "4509220410",                       # Hdo De Aguirre - Eleodoro Yanez, Las Lilas: DESCARTADO por Barbara 2026-09-28.
    "4409958494",                       # Luis Thayer Ojeda 133, Providencia: DESCARTADO por Barbara 2026-09-28 (ya
                                         # fallaba los topes de precio/GC; ademas sin ascensor piso 6, estacionamiento
                                         # tandem compartido, arriendo vigente).
    "4523773982",                       # Las Condes Nor Poniente: es studio, DESCARTADO por Barbara 2026-09-29.
    "4420575658",                       # Departamento Inversion En Providencia: DESCARTADO por Barbara 2026-09-30
                                         # -- edificio se ve muy antiguo por fotos + sin estacionamiento.
    "2285739487",                       # Dpto Con Ubicacion Inmejorable (L. Thayer Ojeda 0127): DESCARTADO 2026-10-03
                                         # -- edificio confirmado 1977 (49 anos, SII), muy a la pasada, Barbara
                                         # desconfia de la liquidez de ese segmento de mercado.
    "4299060012",                       # Nueva De Lyon 170 Dp 1502 (Andres De Fuenzalida 166): DESCARTADO 2026-10-04
                                         # -- informe Propiedata/SII (rol 130-226) confirma superficie construida
                                         # real de 31m2, vs 39m2 utiles / 45m2 totales publicados (m2 inflados).
                                         # Pedido 4.600 UF; modelo Propiedata estima 2.842 UF (rango 2.295-3.194) y
                                         # la venta real mas comparable del mismo edificio (31m2 + estac., 2024-25)
                                         # fue 3.448-3.600 UF. Sobreprecio de 23% a 62% segun el benchmark.
    "2268753681",                       # Departamento En Venta De 2 Dorm. En Providencia: DESCARTADO 2026-10-04
                                         # -- Barbara: edificio se ve muy viejo. Tenia el mejor adj (68) de toda
                                         # la banda C, pero era justamente por la antiguedad (patron ya conocido).
    "2299440261",                       # Depart. Para Remodelar Providencia (Antonio Bellet 226): es la MISMA
                                         # unidad de 4444272012/4191761666 republicada 2026-10-05 -- 45m2 utiles,
                                         # piso 3, 2 estacionamientos + 1 bodega, UF 3.869 vs 3.868 del aviso
                                         # anterior, misma direccion. Descartada desde el 16/21-sep porque el
                                         # corredor solo acepta llamadas telefonicas (sin WhatsApp). Escapo al
                                         # dedup por coords porque lat/lng difieren en el 4to decimal (~80 m).
    "4543944984",                       # Areas Verdes-Condominio Consolidado (Pedro de Valdivia): DESCARTADO
                                         # 2026-10-05 por Barbara -- muy viejo (62 anos declarados, sobre su tope
                                         # de ~50). Tenia el mejor adj (56) de todo el set, otra vez el patron
                                         # "ganga por vieja"; ademas piso 1/4 y 0 estacionamiento.
    "4509177990",                       # Metro Los Leones 1D+1B+E / Vista Oriente (Av. Nueva Providencia):
                                         # DESCARTADO 2026-10-05 por Barbara -- "esta muy a la pasada".
                                         # Era el mejor de los 5 destapados por el filtro >=40 (15 anos, est 1,
                                         # terraza 10m2, adj 100, 11 min) pero la calle lo mata.
    "2099517567",                       # Bello Departamento 1D 1B Metro Los Leones (Av. Nueva Providencia 2170):
                                         # DESCARTADO 2026-10-05 por Barbara, YA VISITADO -- muy a la pasada,
                                         # mucho trafico en esa calle, y encima sin estacionamiento.
    "2176948049",                       # Depto 1 Cuadra Metro Los Leones (Av. Nueva Providencia / Ricardo Lyon):
                                         # = MISMA unidad que 4509177990 republicada por otro corredor (Cariola
                                         # Kroneberg). Coords IDENTICAS (-33.422666,-70.6100146, 0,0 m), mismos
                                         # 40m2 utiles / 50 totales / 10 terraza, est 1 + 0 bodega, edificio de
                                         # 17 pisos, UF 4.300 vs 4.290; solo difiere el piso (14 vs 15, dato mal
                                         # puesto en uno). Descartada 2026-10-05 por republicacion + la calle que
                                         # Barbara ya rechazo ("muy a la pasada"). Afloro al ranking solo porque
                                         # el dedup habia conservado 4509177990 (mejor adj por 0,25).
    "4542166828",                       # Venta Departamento 3d 2b Providencia (Marchant Pereira 10, Paseo
                                         # Providencia): DESCARTADO 2026-10-05 por Barbara -- "muy a la pasada y
                                         # sin estacionamiento". Tenia el mejor adj del set (66) y solo 10 anos
                                         # declarados; es ademas la misma unidad que 2256990123 (en CAIDOS: el
                                         # corredor dijo el 21-sep que no estaba disponible) -> al quedar en
                                         # DESCARTADOS, la huella de unidad ya excluye futuras republicaciones.
    "2245054365",                       # Remodelado 1 Dorm / Nueva Providencia (Av. Nueva Providencia):
                                         # DESCARTADO 2026-10-05 por Barbara -- "muy a la pasada y sin
                                         # estacionamiento". Cuarto aviso de esa avenida que descarta por lo
                                         # transitada; era el ultimo sobreviviente del grupo destapado por >=40
                                         # (45 anos, GC 120k, est 0, adj 108).
    "2274577949",                       # Oportunidad El Golf 1d1b Mut + Bodega Remodelado (Pdte. Riesco 2977):
                                         # DESCARTADO 2026-10-05 por Barbara, YA VISITADO -- edificio muy antiguo y
                                         # la "remodelacion" tiene un gusto muy particular -> habria que remodelar
                                         # de nuevo. Era el mas barato en UF del set (4.090) y tenia la antiguedad
                                         # SIN DATO: la visita confirmo que el descuento era por edad/estado,
                                         # mismo patron "ganga por vieja".
    "4542162062",                       # Excelente Dpto 3d/2b En Av. Providencia (144751): DESCARTADO 2026-10-05
                                         # por Barbara ("muy viejo, muy lejos") -- y es la MISMA unidad que
                                         # 2219776375, ya descartada el 16-sep por los mismos motivos ("edificio
                                         # viejisimo, dice 19 anos pero por fotos es el doble/triple; muy al paso
                                         # de la calle"). Coords identicas, mismo titulo, 66m2/3D/piso 21.
                                         # Paso el filtro porque EXCLUIR corre ANTES del dedup -> ver
                                         # fingerprints_excluidos() abajo, agregado para cerrar ese hueco.
    "4317263782",                       # Departamento Venta 1 Dorm / 1 Bano / Metro Pedro De Valdivia (Av. Pedro
                                         # de Valdivia con Providencia, justo en la salida del metro): DESCARTADO
                                         # 2026-10-06 por Barbara -- "esta muy bonito PERO el edificio esta muy a
                                         # la pasada y debe tener como 70 anos". El depto se ve bien en fotos; lo
                                         # matan la esquina (avenida) y la antiguedad del edificio.
                                         # Antiguedad CONFIRMADA por Barbara via Propiedata el mismo dia: ano de
                                         # construccion 1969 -> 57 anos. OJO: antiguedad_anos = 0 en el CSV (sin
                                         # dato) escondia justamente eso. Llevaba 53 dias en el dataset sin contactar.
                                         # Gemelo exacto MLC-3575613802 (coords 0,0 m, mismos 42m2/1D/UF 4.510,
                                         # mismo titulo) ya estaba delisted desde 2026-07-22; al quedar esta
                                         # unidad en DESCARTADOS la huella lo atrapa si se republica.
    "2280144321",                       # Arrendado Ideal Inversionistas En El Corazon De Providencia (Carlos
                                         # Antunez 1900-2000, Pedro de Valdivia): DESCARTADO 2026-10-06 por
                                         # Barbara -- "por lejos y sin estacionamiento y hay que remodelar".
                                         # 1D/40m2 utiles + 4m2 terraza, $165M (UF 4.014,8), adj 100, 21 min,
                                         # 28 anos, est 0, GC sin dato (campo en 0), piso 3/9.
                                         # Era el ULTIMO sobreviviente de los 5 candidatos que destapo el cambio
                                         # de filtro a >=40 -> los 5 terminaron descartados por Barbara.
                                         # AVISO RECICLADO: 5 republicaciones previas en coords IDENTICAS (0,0 m),
                                         # mismos 40m2/1D/piso 3, todas ya delisted -- 2160847419 (del. 26-ago),
                                         # 4401221990 (5-sep), 2219782739 (17-sep), 4487810882 (28-sep). El
                                         # precio en PESOS nunca se movio ($165M); la UF baja sola (4.037 -> 4.014)
                                         # porque sube el indicador, NO es una rebaja. O sea: llevaba >6 semanas
                                         # sin venderse, no los 7 dias que sugeria su first_seen.
    "4216694058",                       # Depto 2d+2b Con Terraza Y Estacionamiento (Carlos Antunez con Pedro de
                                         # Valdivia, Providencia): DESCARTADO 2026-10-06 por Barbara -- "esta muy
                                         # lejos y hay que remodelar". 2D/41m2 utiles + 10m2 terraza (51 totales),
                                         # UF 4.500 / $184,9M, adj 102, 20 min, 31 anos, GC 150k (AL TOPE), est 1,
                                         # sin bodega, piso 5/8. Llevaba 76 dias en el dataset (first_seen 22-jul),
                                         # el aviso mas anejo del ranking. Sin gemelos (chequeado por coords).
                                         # 3er descarte con "lejos" como motivo explicito en banda C -> ver nota
                                         # de criterio sobre el tope efectivo de distancia.
}
# NOTA 26-sep: NO tener boton WhatsApp visible (solo "Contactar") NO es motivo de descarte por
# si solo -- Barbara lo aclaro explicitamente. 4509167238 (Dario Urzua) vuelve al ranking.
# NOTA 26-sep: 4514087776=4510772796 (Av. Nueva Providencia, 57 anos, 0 est) NO se descarta
# automaticamente por "avenida transitada" -- Barbara evalua eso ella misma con fotos y la
# ubicacion exacta en la calle. Queda en el ranking (banda C) con flag.
# 🚫 caidos verificados (link muerto / redirectedFromVip / corredor dice no disponible)
CAIDOS = {
    "4450271144", "2228842067", "2187517135", "4427322334",
    "4499455338", "2256990123", "4451784562", "4403479822", "4486979384",
    "4394177382",                       # El Golf Centro Financiero: pausada sin ficha 2026-09-22, misma unidad = 4495764082 (esa sigue viva)
    "4510779996",                       # Quillay 2541 (Carmen Silva): corredora Kutt le dijo a Barbara 2026-10-04
                                         # que se vendio (ella habia pedido visita dias antes). El aviso en el
                                         # portal sigue activo (Portal no lo actualizo) -- excluir igual.
    "2214549601",                       # "Luminoso Y Amplio" (El Golf, San Sebastian 2700-3000): CAIDO
                                         # confirmado 2026-10-06 -- Barbara aviso que no lo veia publicado y el
                                         # navegador lo confirmo (la VIP redirige con #redirectedFromVip= al
                                         # listado de El Golf). CSV coherente: last_seen=2026-09-29,
                                         # delisted_date=2026-09-30. Estaba en KEEPALIVE desde un rescate por
                                         # falso positivo, pero esta vez la caida es REAL -> movido aca.
                                         # OJO: es la 2a vez que esta unidad se cae sin venderse (antes fue
                                         # MLC-4182777778, mismo edificio/m2/precio ~196M, caida 2026-08-05) y
                                         # la visita nunca se concreto en ninguno de los 2 ciclos -> si vuelve
                                         # a aparecer, es republicacion, no un aviso nuevo.
    "4545915510",                       # "Depto Para Remodelar 2 Dorm" (P. de Valdivia / Av. Nueva Providencia,
                                         # Orbis, 70 anos, est 0): CAIDO confirmado en navegador 2026-10-09
                                         # (#redirectedFromVip= -> aviso eliminado). Coherente con el CSV:
                                         # last_seen_date=2026-10-08, no aparecio en el scrape del 9-oct.
                                         # Solo estuvo 3 dias en el ranking (entro el 6-oct, adj 70).
}
# verificados VIVOS aunque el CSV los marque delisted (falso positivo) -> rescatar
KEEPALIVE = set()                   # (vacio) 2214549601 "Luminoso Y Amplio" estuvo aca por un falso
                                    # positivo del flag delisted, pero el 2026-10-06 se confirmo CAIDO de
                                    # verdad (ver CAIDOS) -> removido. Leccion: un rescate por KEEPALIVE hay
                                    # que re-verificarlo, no es permanente; mantiene vivo en el ranking un
                                    # aviso que puede haber muerto despues.
                                    # Coronel (4404154390) sacada 2026-09-22: pagina ahora sin ficha (posible vendida)
# ⭐ favoritas / visitadas y 👀 por visitar (solo para marcar el estado)
# 🏠 COMPRADA: oferta aceptada, en tramitacion. Se deja en el ranking a proposito -- Barbara quiere
# seguir mirando el mercado y esta fila es el BENCHMARK contra el que se compara el resto (UF 4.100,
# adj 95, 7 min). Ver memoria depto-compra-san-pio-x-2425.
COMPRADA = {"4541838686"}   # San Pio X 2425 Dp 303: oferto UF 4.100 el miercoles 2026-10-07 (el
                            # precio pedido, sin regatear) y el vendedor acepto; en tramitacion
FAV = {"4404154390", "2231564131", "4441100684",
       "2246908357",    # Carmencita 220 Dp 703: gano el analisis de sept pero NO se concreto; la
                        # negociacion (5.100/5.300) quedo abierta y hay que cerrarla con la corredora
       } | COMPRADA
POR_VISITAR = {
    "2267442371",    # Pio X (Mardoqueo Fernandez 171): visita agendada el miercoles 2026-10-07 18:00,
                     # el mismo dia en que Barbara oferto por San Pio X -> resultado nunca registrado,
                     # probablemente quedo sin desenlace por eso (no confirmado)
}
# excepciones de tamano confirmadas por Barbara caso a caso (para los que miden MENOS de 40m2;
# los de 40m2 exactos ya pasan solos desde que el filtro quedo inclusivo el 2026-10-05)
INCLUIR_AUNQUE_FALLE_M2 = {
    "2267442371",    # Los Leones / Pio X (Mardoqueo Fernandez): 40m2 utiles exactos, GC real 85k,
                     # WhatsApp, sin arriendo vigente, calle tranquila -- Barbara pidio incluirlo
                     # 2026-09-27. Ya redundante con el filtro >=40, se deja por trazabilidad.
}

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

def _huellas(df, ids):
    """Huellas de UNIDAD para los listing_id dados: (exactas por coords, aproximadas)."""
    sub = df[df["id"].isin(ids)]
    exactas, aprox = set(), []
    for _, r in sub.iterrows():
        if pd.isna(r["lat"]) or pd.isna(r["lng"]) or pd.isna(r["m2_utiles"]):
            continue
        exactas.add((round(r["lat"], 5), round(r["lng"], 5), r["m2_utiles"], r["bedrooms_n"]))
        aprox.append((r["lat"], r["lng"], r["m2_utiles"], r["bedrooms_n"],
                      r["piso_unidad"], r["price_uf"], r["listing_id"]))
    return exactas, aprox

def misma_unidad_que(r, exactas, aprox, metros=150, tol_precio=0.03):
    """True si r es la misma unidad que alguna de las huellas.

    Dos criterios, porque las republicaciones evaden de dos formas:
      - coords@5dp + m2 utiles + dormitorios -> coords identicas (caso tipico)
      - a <150 m con mismos m2, dormitorios y piso y precio dentro de 3% -> coords con
        ruido de geocodificacion (Antonio Bellet 226 difirio en el 4to decimal, ~80 m)
    NO se usa el nombre de la calle como huella: "Callao, Barrio El Golf" o "Avenida Nueva
    Providencia" matchean edificios distintos y producen falsos positivos (se probo
    2026-10-05 y saco del ranking a Vive El Confort, que Barbara visito y le gusto).
    """
    if pd.isna(r["lat"]) or pd.isna(r["lng"]) or pd.isna(r["m2_utiles"]):
        return None
    if (round(r["lat"], 5), round(r["lng"], 5), r["m2_utiles"], r["bedrooms_n"]) in exactas:
        return next((h[6] for h in aprox
                     if round(h[0], 5) == round(r["lat"], 5)
                     and round(h[1], 5) == round(r["lng"], 5)
                     and h[2] == r["m2_utiles"] and h[3] == r["bedrooms_n"]), "?")
    for lat, lng, m2, dorm, piso, uf, lid in aprox:
        if m2 != r["m2_utiles"] or dorm != r["bedrooms_n"]:
            continue
        if pd.isna(piso) or pd.isna(r["piso_unidad"]) or piso != r["piso_unidad"]:
            continue
        if pd.isna(uf) or pd.isna(r["price_uf"]) or abs(r["price_uf"] / uf - 1) > tol_precio:
            continue
        if (((lat - r["lat"]) * 111_000) ** 2 + ((lng - r["lng"]) * 92_000) ** 2) ** 0.5 <= metros:
            return lid
    return None

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
    f = f[(f["m2_utiles"] >= MIN_M2_UTILES) | f["id"].isin(INCLUIR_AUNQUE_FALLE_M2)]
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

    # EXCLUIR es por listing_id y corre ANTES del dedup: cuando una unidad descartada se
    # republica bajo otro ID, el ID viejo se va por EXCLUIR y el nuevo queda sin nada contra
    # lo que deduplicar, asi que vuelve al ranking como "nuevo". Paso 3 veces (Antonio Bellet
    # 226; Vista Oriente/2176948049; y 4542162062 que era 2219776375, descartada el 16-sep y
    # re-descartada el 5-oct por los mismos motivos). Se cierra por huella de unidad.
    # OJO: solo DESCARTADOS, nunca CAIDOS -- un caido es un link muerto, su republicacion es
    # justo lo que queremos ver; mezclarlos saco del ranking a Vive El Confort (visitada y
    # querida) y a Marchant Pereira.
    d_ex, d_ap = _huellas(df, DESCARTADOS)
    rep = f.apply(lambda r: misma_unidad_que(r, d_ex, d_ap), axis=1)
    if rep.notna().any():
        print("\n[republicacion de DESCARTADO -> excluido del ranking]")
        for lid, orig in zip(f["listing_id"][rep.notna()], rep[rep.notna()]):
            print(f"  {lid} = misma unidad que {orig} (ya descartada)")
    f = f[rep.isna()]

    # Los caidos NO se excluyen, pero si una unidad caida reaparece bajo otro ID conviene
    # saberlo: puede ser que volvio al mercado de verdad, o que el aviso es bait.
    c_ex, c_ap = _huellas(df, CAIDOS)
    revive = f.apply(lambda r: misma_unidad_que(r, c_ex, c_ap), axis=1)
    if revive.notna().any():
        print("\n[⚠️ republicacion de un aviso CAIDO -- sigue en el ranking, pero verificar]")
        for lid, orig in zip(f["listing_id"][revive.notna()], revive[revive.notna()]):
            print(f"  {lid} = misma unidad que {orig} (caida). Confirmar disponibilidad real.")

    f["pk"] = f["parking"].fillna(0)
    f["adj"] = (f["price_uf"] - PARKING_UF * f["pk"]) / f["m2_utiles"]

    # dedup: 1) por coords+m2+dorm (caza republicaciones multi-corredor), 2) backstop calle+precio+dorm
    f["la5"] = f["lat"].round(5); f["ln5"] = f["lng"].round(5)
    f = f.sort_values("adj").drop_duplicates(["la5", "ln5", "m2_utiles", "bedrooms_n"], keep="first")
    f["calle"] = f["location"].apply(calle)
    f = f.sort_values("adj").drop_duplicates(["calle", "price_uf", "bedrooms_n"], keep="first")
    f = f.sort_values("adj").reset_index(drop=True)

    def estado(i):
        if i in COMPRADA:
            return "COMPRADA"
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
