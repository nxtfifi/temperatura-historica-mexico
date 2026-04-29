"""
preprocessing.py — Script de extracción y limpieza de datos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Proyecto: ¿Cuándo dejó de ser normal el calor?
Curso: Visualización Gráfica para IA — IBERO León 2025

Fuentes:
  - NASA GISS Surface Temperature Analysis (GISTEMP v4)
    · Global Annual: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv
    · Zonal Annual:  https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv
  Fecha de descarga: 2025-04-28
  Formato: CSV | Licencia: Dominio público (datos gubernamentales EE.UU.)

Uso:
  python preprocessing.py

Salida (en data/processed/):
  · global_annual.csv   — anomalías anuales globales con medias móviles
  · global_monthly_heatmap.csv — tabla pivote meses×años para mapa de calor
  · zonal_annual.csv    — anomalías por zona geográfica con medias móviles
"""

import os
import io
import requests
import pandas as pd
import numpy as np

# ─── Configuración ────────────────────────────────────────────────────────────
RAW_DIR  = "data/raw"
PROC_DIR = "data/processed"

URLS = {
    "global": "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
    "zonal":  "https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv",
}

MONTHS_EN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_ES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]


_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def download_raw(name: str, url: str) -> str:
    """Descarga un CSV y lo guarda en data/raw/. Devuelve el texto del CSV."""
    print(f"  Descargando {name}...")
    resp = requests.get(url, timeout=30, headers=_HEADERS)
    resp.raise_for_status()
    local_path = os.path.join(RAW_DIR, f"{name}.csv")
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print(f"  ✅ Guardado en {local_path} ({len(resp.text)//1024} KB)")
    return resp.text


def process_global(raw_text: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Procesa los datos globales de GISTEMP.

    Limpieza aplicada:
    - Omisión de línea de encabezado de metadatos (skiprows=1)
    - Valores faltantes codificados como '***' o '****' → NaN
    - Filtro de filas donde Year no es numérico (GISTEMP incluye sub-headers)
    - Conversión de tipos: year→int, anomaly→float
    - Eliminación de filas con anomalía faltante en J-D (media anual)
    - Cálculo de medias móviles centradas de 5 y 10 años
    - Derivación de columna 'decade' para agrupaciones decenales

    Transformaciones para mapa de calor:
    - Selección de columnas mensuales (Jan–Dec)
    - Renombrado a español (Ene–Dic)
    - Pivot: meses como índice (filas), años como columnas
    """
    raw = pd.read_csv(
        io.StringIO(raw_text),
        skiprows=1,
        na_values=["***", "****", "*****"],
    )

    # Filtrar filas no numéricas en Year (sub-headers que GISTEMP inserta)
    raw = raw[pd.to_numeric(raw["Year"], errors="coerce").notna()].copy()
    raw["Year"] = raw["Year"].astype(int)

    # ── Serie anual (J-D = media Enero–Diciembre) ────────────────────────
    annual = raw[["Year", "J-D"]].copy()
    annual.columns = ["year", "anomaly"]
    annual["anomaly"] = pd.to_numeric(annual["anomaly"], errors="coerce")
    annual = annual.dropna(subset=["anomaly"]).copy()
    annual["roll5"]  = annual["anomaly"].rolling(5,  center=True).mean()
    annual["roll10"] = annual["anomaly"].rolling(10, center=True).mean()
    annual["decade"] = (annual["year"] // 10) * 10

    print(f"  → Serie anual: {len(annual)} filas ({annual['year'].min()}–{annual['year'].max()})")

    # Estadísticas descriptivas por décad (diagnóstico de calidad)
    decade_stats = annual.groupby("decade")["anomaly"].agg(["mean", "std", "count"])
    print("  → Anomalía promedio por década:")
    for dec, row in decade_stats.iterrows():
        bar = "█" * int(abs(row["mean"]) * 15)
        sign = "+" if row["mean"] > 0 else ""
        print(f"     {dec}s: {sign}{row['mean']:.3f}°C  {bar}")

    # ── Datos mensuales → mapa de calor ──────────────────────────────────
    monthly_cols = ["Year"] + MONTHS_EN
    monthly = raw[monthly_cols].copy()
    monthly.columns = ["year"] + MONTHS_ES
    for m in MONTHS_ES:
        monthly[m] = pd.to_numeric(monthly[m], errors="coerce")
    monthly = monthly.dropna(subset=["year"])
    monthly["year"] = monthly["year"].astype(int)

    heatmap = monthly.set_index("year")[MONTHS_ES].T.astype(float)
    # Porcentaje de datos faltantes
    missing_pct = heatmap.isna().sum().sum() / heatmap.size * 100
    print(f"  → Heatmap: {heatmap.shape[1]} años × 12 meses | faltantes: {missing_pct:.1f}%")

    return annual, heatmap


def process_zonal(raw_text: str) -> pd.DataFrame:
    """
    Procesa los datos zonales de GISTEMP.

    Limpieza aplicada:
    - Mismo skiprows y na_values que el global
    - Selección de columnas relevantes: Glob, NHem, 24N-44N, EQU-24N
    - Conversión de tipos
    - Medias móviles de 10 años por zona (suaviza variabilidad interanual)

    Nota geográfica:
    - '24N-44N' cubre norte y centro de México
    - 'EQU-24N' cubre sur de México y Centroamérica
    """
    # Detectar automáticamente cuántas filas saltar (buscar la que tiene "Year")
    lines = raw_text.splitlines()
    header_row = next(
        (i for i, line in enumerate(lines) if "Year" in line.split(",")[0]),
        1
    )

    raw = pd.read_csv(
        io.StringIO(raw_text),
        skiprows=header_row,
        na_values=["***", "****", "*****"],
    )

    # Limpiar nombres de columnas (espacios, caracteres raros)
    raw.columns = raw.columns.str.strip()

    # Buscar la columna Year de forma flexible
    year_col = next((c for c in raw.columns if c.strip().lower() == "year"), None)
    if year_col is None:
        raise KeyError(f"No se encontró columna 'Year'. Columnas disponibles: {list(raw.columns)}")
    if year_col != "Year":
        raw = raw.rename(columns={year_col: "Year"})

    raw = raw[pd.to_numeric(raw["Year"], errors="coerce").notna()].copy()
    raw["Year"] = raw["Year"].astype(int)

    target_cols = {
        "Year":    "year",
        "Glob":    "global",
        "NHem":    "n_hem",
        "SHem":    "s_hem",
        "24N-44N": "mex_norte",
        "EQU-24N": "mex_sur",
    }
    available = {k: v for k, v in target_cols.items() if k in raw.columns}
    zonal = raw[list(available.keys())].rename(columns=available).copy()

    zonal["year"] = pd.to_numeric(zonal["year"], errors="coerce")
    zonal = zonal.dropna(subset=["year"])
    zonal["year"] = zonal["year"].astype(int)

    for col in ["global", "n_hem", "s_hem", "mex_norte", "mex_sur"]:
        if col in zonal.columns:
            zonal[col] = pd.to_numeric(zonal[col], errors="coerce")
            zonal[f"{col}_r10"] = zonal[col].rolling(10, center=True).mean()

    print(f"  → Datos zonales: {len(zonal)} filas | columnas: {list(zonal.columns)}")

    # Diagnóstico: calentamiento relativo México vs Global en período reciente
    if "mex_norte" in zonal.columns and "global" in zonal.columns:
        recent = zonal[zonal["year"] >= 2000].copy()
        mx_mean  = recent["mex_norte"].mean()
        glb_mean = recent["global"].mean()
        if not (np.isnan(mx_mean) or np.isnan(glb_mean)):
            ratio = mx_mean / glb_mean if glb_mean != 0 else 1.0
            print(f"  → Media 2000–present: México norte={mx_mean:.3f}°C | Global={glb_mean:.3f}°C | ratio={ratio:.2f}x")

    return zonal


def main():
    print("\n════════════════════════════════════════════════════")
    print("  Pipeline de datos — Temperatura histórica GISTEMP v4")
    print("════════════════════════════════════════════════════\n")

    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROC_DIR, exist_ok=True)

    # ── 1. Descarga ──────────────────────────────────────────────────────
    print("[ 1/3 ] Descarga de datos crudos")
    global_raw = download_raw("global", URLS["global"])
    zonal_raw  = download_raw("zonal",  URLS["zonal"])

    # ── 2. Procesamiento ─────────────────────────────────────────────────
    print("\n[ 2/3 ] Limpieza y transformación")
    print("  · Datos globales:")
    df_annual, df_heatmap = process_global(global_raw)
    print("  · Datos zonales:")
    df_zonal = process_zonal(zonal_raw)

    # ── 3. Guardado ──────────────────────────────────────────────────────
    print("\n[ 3/3 ] Guardado de archivos procesados")
    df_annual.to_csv(os.path.join(PROC_DIR, "global_annual.csv"), index=False)
    df_heatmap.to_csv(os.path.join(PROC_DIR, "global_monthly_heatmap.csv"))
    df_zonal.to_csv(os.path.join(PROC_DIR, "zonal_annual.csv"), index=False)
    print(f"  ✅ global_annual.csv          ({len(df_annual)} filas)")
    print(f"  ✅ global_monthly_heatmap.csv ({df_heatmap.shape[0]}×{df_heatmap.shape[1]})")
    print(f"  ✅ zonal_annual.csv           ({len(df_zonal)} filas)")

    print("\n✔ Pipeline completado exitosamente.")
    print(f"  Archivos en: {os.path.abspath(PROC_DIR)}\n")


if __name__ == "__main__":
    main()
