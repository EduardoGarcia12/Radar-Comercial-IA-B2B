import pandas as pd
import re
import pandas as pd
import re
from pathlib import Path



# =====================================
# RUTAS
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

ARCHIVO_ENTRADA = BASE_DIR / "datos" / "prospectos.csv"
ARCHIVO_SALIDA = BASE_DIR / "procesados" / "prospectos_scoring.csv"

print(f"Leyendo archivo: {ARCHIVO_ENTRADA}")

# =====================================
# CARGA DE DATOS
# =====================================

df = pd.read_csv(
    ARCHIVO_ENTRADA,
    encoding="utf-8"
)

# Elimina espacios accidentales en encabezados

df.columns = df.columns.str.strip()

print("\nColumnas detectadas:")
print(df.columns.tolist())

# =====================================
# FUNCIONES AUXILIARES
# =====================================

def obtener_dias(texto):
    """
    Convierte:
    'Hace 12 días' -> 12
    """

    match = re.search(r"(\d+)", str(texto))

    if match:
        return int(match.group(1))

    return 999


# =====================================
# FIT ICP (20)
# =====================================

def score_fit_icp(row):

    score = 0

    # Tamaño empresa

    if row["Tamaño estimado"] == "Grande":
        score += 20

    elif row["Tamaño estimado"] == "Mediana":
        score += 15

    elif row["Tamaño estimado"] == "PyME":
        score += 10

    else:
        score += 5

    return score


# =====================================
# NECESIDAD (15)
# =====================================

def score_necesidad(necesidad):

    necesidad = str(necesidad).lower()

    palabras_clave = [
        "automatizar",
        "dashboard",
        "crm",
        "reportes",
        "pipeline",
        "ia",
        "ventas",
        "cotización",
        "cotizaciones"
    ]

    if any(p in necesidad for p in palabras_clave):
        return 15

    return 10


# =====================================
# PRESUPUESTO (15)
# =====================================

def score_presupuesto(presupuesto):

    presupuesto = str(presupuesto)

    if "400k+" in presupuesto:
        return 15

    if "300k+" in presupuesto:
        return 15

    if "250k" in presupuesto:
        return 12

    if "180k" in presupuesto:
        return 12

    if "150k" in presupuesto:
        return 12

    if "$100k" in presupuesto:
        return 8

    if "70k" in presupuesto:
        return 6

    if "50k" in presupuesto:
        return 4

    if "30k" in presupuesto:
        return 2

    if "No definido" in presupuesto:
        return 2

    return 2


# =====================================
# URGENCIA (15)
# =====================================

def score_urgencia(urgencia):

    mapa = {
        "Alta": 15,
        "Media": 10,
        "Baja": 5
    }

    return mapa.get(urgencia, 0)


# =====================================
# INTERÉS (10)
# =====================================

def score_interes(interes):

    mapa = {
        "Alto": 10,
        "Medio": 6,
        "Bajo": 2
    }

    return mapa.get(interes, 0)


# =====================================
# APROBACIÓN / DECISOR (10)
# =====================================

def score_decisor(objecion):

    objecion = str(objecion).lower()

    if "dirección no ha aprobado" in objecion:
        return 5

    if "falta dueño de proyecto" in objecion:
        return 2

    return 10


# =====================================
# RIESGO DE ENFRIAMIENTO (10)
# =====================================

def score_enfriamiento(contacto):

    dias = obtener_dias(contacto)

    if dias <= 7:
        return 10

    elif dias <= 15:
        return 7

    elif dias <= 25:
        return 4

    else:
        return 1


# =====================================
# OBJECIÓN (5)
# =====================================

def score_objecion(objecion):

    objecion = str(objecion).lower()

    faciles = [
        "roi",
        "caso de éxito",
        "implementación"
    ]

    medias = [
        "datos",
        "aprobado"
    ]

    if any(x in objecion for x in faciles):
        return 5

    if any(x in objecion for x in medias):
        return 3

    return 1


# =====================================
# SCORE TOTAL
# =====================================

def calcular_score(row):

    return (

        score_fit_icp(row)

        + score_necesidad(row["Necesidad detectada"])

        + score_presupuesto(row["Presupuesto estimado"])

        + score_urgencia(row["Urgencia"])

        + score_interes(row["Interés"])

        + score_decisor(row["Objeción"])

        + score_enfriamiento(row["Último contacto"])

        + score_objecion(row["Objeción"])
    )


# =====================================
# CLASIFICACIÓN
# =====================================

def clasificar(score):

    if score >= 80:
        return "A"

    elif score >= 60:
        return "B"

    elif score >= 40:
        return "C"

    return "D"


# =====================================
# RIESGO EN TEXTO
# =====================================

def riesgo_texto(contacto):

    dias = obtener_dias(contacto)

    if dias <= 7:
        return "Bajo"

    elif dias <= 15:
        return "Medio"

    return "Alto"


# =====================================
# EJECUTAR
# =====================================

df["Score"] = df.apply(calcular_score, axis=1)

df["Categoría"] = df["Score"].apply(clasificar)

df["Riesgo"] = df["Último contacto"].apply(riesgo_texto)

# Ordenar de mayor score a menor

df = df.sort_values(
    by="Score",
    ascending=False
)

# Mostrar resultado

print(
    df[
        [
            "Prospecto",
            "Empresa",
            "Score",
            "Categoría",
            "Riesgo"
        ]
    ]
)

# =====================================
# EXPORTAR RESULTADO
# =====================================

# Crear carpeta procesados si no existe

ARCHIVO_SALIDA.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    ARCHIVO_SALIDA,
    index=False,
    encoding="utf-8-sig"
)

print("\nArchivo generado correctamente:")
print(ARCHIVO_SALIDA)