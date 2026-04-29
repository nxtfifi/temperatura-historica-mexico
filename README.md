# ¿Cuándo dejó de ser normal el calor?
### El año en que México y el mundo cruzaron el punto de inflexión climático

**Autor:** Felix Garcia
**Matrícula:** 194223-7  
**Curso:** Visualización Gráfica para IA
**Docente:** Dra. Dora Alvarado  
**Herramienta:** Marimo · **Tema:** Temperatura histórica global y en México  

---

## Descripción del proyecto

Data story interactiva construida con [Marimo](https://marimo.io) que explora 144 años de
mediciones de temperatura (NASA GISTEMP v4, 1880–2024) para responder una pregunta central:
¿cuándo exactamente dejó el calor extremo de ser la excepción climática y se convirtió en la
nueva normalidad? El recorrido va de lo global a lo local, con especial énfasis en las zonas
geográficas que cubren México.

### Pregunta de investigación

> **¿Cuándo dejó de ser normal el calor?**  
> El año en que cada región cruzó el punto de inflexión climático.

### Sub-preguntas narrativas

1. ¿Cuánto ha aumentado la temperatura global desde que existen registros instrumentales?
2. ¿Se está calentando México más rápido que el promedio mundial?
3. ¿En qué mes y año el rojo tomó control permanente del calendario climático?

### Visualizaciones

| # | Título | Tipo | Interactividad |
|---|--------|------|----------------|
| 1 | La línea que no para | Gráfica de barras divergentes + línea de tendencia | Selector de suavizado (Marimo reactivo), zoom/pan, rangeslider |
| 2 | México bajo la lupa | Gráfica de líneas múltiples por zona | Multiselect reactivo de series (Marimo), hover unificado |
| 3 | El calendario del calentamiento | Mapa de calor mensual (1880–2024) | Hover con valor exacto, zoom, herramientas Plotly |

---

## Fuentes de datos

| Dataset | URL | Fecha descarga | Formato | Licencia |
|---------|-----|----------------|---------|----------|
| NASA GISTEMP v4 — Global Annual Mean | `https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv` | 2025-04-28 | CSV | Dominio público (EE.UU.) |
| NASA GISTEMP v4 — Zonal Annual Means | `https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv` | 2025-04-28 | CSV | Dominio público (EE.UU.) |

Las anomalías están expresadas en °C respecto a la media del período base **1951–1980**.

---

## Estructura del repositorio

```
proyecto-final/
├── app.py                    # Aplicación Marimo principal (data story completa)
├── preprocessing.py          # Script standalone de extracción y limpieza
├── requirements.txt
├── README.md           
└── data/                     #Estas carpetas las crea presprocessing.py
    ├── raw/                  # CSVs originales descargados (generados por preprocessing.py)
    │   ├── global.csv
    │   └── zonal.csv
    └── processed/            # Datos limpios y transformados
        ├── global_annual.csv
        ├── global_monthly_heatmap.csv
        └── zonal_annual.csv
```

---

## Instrucciones para ejecutar localmente

### Requisitos
- Python 3.10 o superior
- pip

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/nxtfifi/temperatura-historica-mexico.git


# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate      # Linux/macOS
# venv\Scripts\activate       # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

### Ejecución

```bash
# Opción A: Pre-descargar y procesar datos (recomendado para la primera vez)
python preprocessing.py

# Opción B: Correr la app directamente (descarga automática al cargar)
marimo run app.py

# Para desarrollo (modo edición con hot-reload):
marimo edit app.py
```

La aplicación abre automáticamente en `http://localhost:2718`.

### Notas
- Si `preprocessing.py` se ejecutó previamente, la app carga desde `data/processed/` sin conexión a internet.
- Si no se ejecutó, la app descarga los datos de NASA GISTEMP al iniciar (requiere internet, ~5 segundos).

---

## Aplicación desplegada

🔗 **[Ver app en línea](https://molab.marimo.io/notebooks/nb_Go5dw9rHs9A2eS7VzA9seQ/app)**

> Plataforma de despliegue: Marimo Cloud (molab.marimo.io)

---

## Decisiones de diseño

| Visualización | Tipo elegido | Justificación |
|---------------|-------------|---------------|
| Anomalía global | Barras divergentes | El canal visual de posición codifica dirección (positivo/negativo) y magnitud simultáneamente; el color refuerza warm/cold semánticamente |
| Comparación zonal | Líneas múltiples | Permite comparar trayectorias temporales y pendientes entre series; la media móvil 10a elimina ruido sin perder forma |
| Mapa de calor mensual | Heatmap | Codifica dos variables categóricas (mes/año) y una continua (anomalía) en una sola vista; revela patrones estacionales invisibles en series anuales |
