import marimo

__generated_with = "0.23.4"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    import requests, io, os, warnings
    warnings.filterwarnings("ignore")

    FALLBACK = {
        1880:-0.16,1881:-0.08,1882:-0.11,1883:-0.17,1884:-0.28,
        1885:-0.33,1886:-0.31,1887:-0.36,1888:-0.27,1889:-0.17,
        1890:-0.35,1891:-0.22,1892:-0.27,1893:-0.31,1894:-0.32,
        1895:-0.23,1896:-0.11,1897:-0.11,1898:-0.27,1899:-0.17,
        1900:-0.08,1901:-0.15,1902:-0.28,1903:-0.37,1904:-0.47,
        1905:-0.26,1906:-0.22,1907:-0.39,1908:-0.43,1909:-0.48,
        1910:-0.43,1911:-0.44,1912:-0.36,1913:-0.35,1914:-0.15,
        1915:-0.14,1916:-0.36,1917:-0.46,1918:-0.30,1919:-0.27,
        1920:-0.27,1921:-0.19,1922:-0.28,1923:-0.26,1924:-0.27,
        1925:-0.22,1926:-0.06,1927:-0.15,1928:-0.20,1929:-0.36,
        1930:-0.09,1931:-0.07,1932:-0.11,1933:-0.27,1934:-0.13,
        1935:-0.19,1936:-0.14,1937:-0.02,1938:-0.00,1939:-0.02,
        1940: 0.09,1941: 0.20,1942: 0.07,1943: 0.09,1944: 0.20,
        1945: 0.09,1946:-0.07,1947:-0.03,1948:-0.05,1949:-0.08,
        1950:-0.16,1951: 0.01,1952: 0.02,1953: 0.08,1954:-0.13,
        1955:-0.14,1956:-0.15,1957: 0.05,1958: 0.06,1959: 0.03,
        1960:-0.03,1961: 0.06,1962: 0.03,1963: 0.05,1964:-0.20,
        1965:-0.11,1966:-0.06,1967:-0.02,1968:-0.07,1969: 0.08,
        1970: 0.03,1971:-0.08,1972: 0.01,1973: 0.16,1974:-0.07,
        1975:-0.01,1976:-0.10,1977: 0.18,1978: 0.07,1979: 0.16,
        1980: 0.26,1981: 0.32,1982: 0.14,1983: 0.31,1984: 0.16,
        1985: 0.12,1986: 0.18,1987: 0.33,1988: 0.40,1989: 0.29,
        1990: 0.45,1991: 0.41,1992: 0.23,1993: 0.24,1994: 0.31,
        1995: 0.45,1996: 0.35,1997: 0.46,1998: 0.63,1999: 0.40,
        2000: 0.42,2001: 0.54,2002: 0.63,2003: 0.62,2004: 0.54,
        2005: 0.68,2006: 0.61,2007: 0.66,2008: 0.54,2009: 0.64,
        2010: 0.72,2011: 0.61,2012: 0.64,2013: 0.68,2014: 0.75,
        2015: 0.87,2016: 1.01,2017: 0.92,2018: 0.83,2019: 0.98,
        2020: 1.02,2021: 0.85,2022: 0.89,2023: 1.17,2024: 1.29,
    }
    return FALLBACK, go, io, mo, os, pd, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    <div style="background:linear-gradient(160deg,#0d1117 0%,#161b22 60%,#1a2332 100%);
            padding:60px 52px;border-radius:14px;border:1px solid #30363d;margin-bottom:8px;">
      <p style="color:#7d8590;font-size:0.8em;letter-spacing:3px;text-transform:uppercase;margin:0 0 18px 0;">
    Visualización Gráfica para IA · IBERO León · 2026
      </p>
      <h1 style="color:#e6edf3;font-size:2.9em;font-family:Georgia,serif;margin:0 0 14px 0;line-height:1.2;">
    ¿Cuándo dejó de ser<br>normal el calor?
      </h1>
      <h2 style="color:#ff7b72;font-size:1.2em;font-weight:400;font-family:Georgia,serif;margin:0 0 30px 0;">
    El año en que México y el mundo cruzaron el punto de inflexión climático
      </h2>
      <div style="height:3px;background:linear-gradient(90deg,#ff7b72,#ffa657 40%,transparent);border-radius:2px;margin-bottom:30px;"></div>
      <p style="color:#7d8590;font-size:0.82em;margin:0;line-height:1.8;">
    📊 <b style="color:#8b949e">Fuente:</b> NASA GISS GISTEMP v4 &nbsp;·&nbsp;
    🗓 <b style="color:#8b949e">Período:</b> 1880–2024 &nbsp;·&nbsp;
    🌡 <b style="color:#8b949e">Referencia:</b> Media 1951–1980
      </p>
    </div>

    Durante siglos, las personas aprendieron a leer el clima de su región con sorprendente precisión.
    Los agricultores de Guanajuato sabían cuándo sembrar el maíz; los pescadores del Golfo sabían
    cuándo zarpar. Ese conocimiento tenía un fundamento estadístico concreto: la temperatura del planeta
    oscilaba dentro de rangos conocidos y predecibles.

    **Algo cambió. La pregunta que guía esta historia es: ¿cuándo exactamente?**

    A través de 144 años de mediciones exploraremos tres preguntas que van de lo global a lo local:
    ¿cuánto ha escalado la temperatura? ¿Se está calentando México más rápido? ¿Y en qué momento
    el calor extremo dejó de ser la excepción y se convirtió en la nueva normalidad?
    """)
    return


@app.cell(hide_code=True)
def _(FALLBACK, io, os, pd, requests):
    _URL = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    _P1, _P2 = "data/processed/global_annual.csv", "data/processed/global_monthly_heatmap.csv"
    _MEN = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    _MES = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
    try:
        if os.path.exists(_P1) and os.path.exists(_P2):
            df_annual = pd.read_csv(_P1)
            df_heatmap = pd.read_csv(_P2, index_col=0)
        else:
            _h = {"User-Agent": "Mozilla/5.0 (compatible; academic/1.0)"}
            _r = requests.get(_URL, timeout=25, headers=_h); _r.raise_for_status()
            _raw = pd.read_csv(io.StringIO(_r.text), skiprows=1, na_values=["***","****","*****"])
            _raw.columns = _raw.columns.str.strip()
            _raw = _raw[pd.to_numeric(_raw["Year"], errors="coerce").notna()].copy()
            _raw["Year"] = _raw["Year"].astype(int)
            df_annual = _raw[["Year","J-D"]].rename(columns={"Year":"year","J-D":"anomaly"}).copy()
            df_annual["anomaly"] = pd.to_numeric(df_annual["anomaly"], errors="coerce")
            df_annual = df_annual.dropna()
            df_annual["roll5"]  = df_annual["anomaly"].rolling(5,  center=True).mean()
            df_annual["roll10"] = df_annual["anomaly"].rolling(10, center=True).mean()
            _am = [c for c in ["Year"]+_MEN if c in _raw.columns]
            _mo = _raw[_am].copy(); _mo.columns = ["year"]+_MES[:len(_am)-1]
            for _m in _MES[:len(_am)-1]: _mo[_m] = pd.to_numeric(_mo[_m], errors="coerce")
            df_heatmap = _mo.set_index("year")[_MES[:len(_am)-1]].T.astype(float)
            os.makedirs("data/processed", exist_ok=True)
            df_annual.to_csv(_P1, index=False); df_heatmap.to_csv(_P2)
    except Exception as _e:
        print(f"Fallback: {_e}")
        _fb = pd.DataFrame({"year":list(FALLBACK.keys()),"anomaly":list(FALLBACK.values())})
        _fb["roll5"]  = _fb["anomaly"].rolling(5, center=True).mean()
        _fb["roll10"] = _fb["anomaly"].rolling(10, center=True).mean()
        df_annual = _fb; df_heatmap = pd.DataFrame()
    return df_annual, df_heatmap


@app.cell(hide_code=True)
def _(io, os, pd, requests):
    _URL2 = "https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv"
    _P3 = "data/processed/zonal_annual.csv"
    try:
        if os.path.exists(_P3):
            df_zonal = pd.read_csv(_P3)
        else:
            _h = {"User-Agent": "Mozilla/5.0 (compatible; academic/1.0)"}
            _r = requests.get(_URL2, timeout=25, headers=_h); _r.raise_for_status()
            _lines = _r.text.splitlines()
            _hrow = next((i for i,l in enumerate(_lines) if "Year" in l.split(",")[0]), 1)
            _raw = pd.read_csv(io.StringIO(_r.text), skiprows=_hrow, na_values=["***","****","*****"])
            _raw.columns = _raw.columns.str.strip()
            _map = {"Year":"year","Glob":"global","NHem":"n_hem","24N-44N":"mex_norte","EQU-24N":"mex_sur"}
            _av = {k:v for k,v in _map.items() if k in _raw.columns}
            df_zonal = _raw[list(_av.keys())].rename(columns=_av).copy()
            df_zonal["year"] = pd.to_numeric(df_zonal["year"], errors="coerce")
            df_zonal = df_zonal.dropna(subset=["year"]); df_zonal["year"] = df_zonal["year"].astype(int)
            for _c in ["global","n_hem","mex_norte","mex_sur"]:
                if _c in df_zonal.columns:
                    df_zonal[_c] = pd.to_numeric(df_zonal[_c], errors="coerce")
                    df_zonal[f"{_c}_r10"] = df_zonal[_c].rolling(10, center=True).mean()
            os.makedirs("data/processed", exist_ok=True); df_zonal.to_csv(_P3, index=False)
    except Exception as _e:
        print(f"Fallback zonal: {_e}"); df_zonal = pd.DataFrame()
    return (df_zonal,)


@app.cell(hide_code=True)
def _(mo):
    smooth_option = mo.ui.dropdown(
        options={"Sin suavizado":"none","Media móvil 5 años":"roll5","Media móvil 10 años":"roll10"},
        value="Media móvil 10 años", label="Línea de tendencia:",
    )
    return (smooth_option,)


@app.cell(hide_code=True)
def _(df_annual, go, mo, smooth_option):
    _texto1 = mo.md("""
    ---
    ## 1 · La línea que no para

    Cada barra representa la desviación de temperatura de un año respecto al período base 1951–1980.
    Las barras **azules** corresponden a años más fríos que ese promedio; las **rojas**, a años más cálidos.

    Hasta los años 70, el azul y el rojo se alternaban sin orden aparente — el clima oscilaba dentro
    de su variabilidad natural conocida. A partir de 1980 el rojo comenzó a dominar sin pausa.
    Los diez años más cálidos jamás registrados son, todos, los diez más recientes.

    > 🔍 **Interactivo:** cambia el suavizado con el selector. Arrastra el eje X para hacer zoom.
    """)
    _s = smooth_option.value
    _fig1 = go.Figure()
    if not df_annual.empty:
        _pos = df_annual[df_annual["anomaly"] >= 0]
        _neg = df_annual[df_annual["anomaly"] < 0]
        _fig1.add_trace(go.Bar(x=_pos["year"], y=_pos["anomaly"],
            marker=dict(color="#ff4444", opacity=0.85), name="Años más cálidos",
            hovertemplate="<b>%{x}</b><br>+%{y:.2f} °C<extra></extra>"))
        _fig1.add_trace(go.Bar(x=_neg["year"], y=_neg["anomaly"],
            marker=dict(color="#4488cc", opacity=0.85), name="Años más fríos",
            hovertemplate="<b>%{x}</b><br>%{y:.2f} °C<extra></extra>"))
        if _s != "none" and _s in df_annual.columns:
            _fig1.add_trace(go.Scatter(x=df_annual["year"], y=df_annual[_s], mode="lines",
                name={"roll5":"Media 5 años","roll10":"Media 10 años"}.get(_s,_s),
                line=dict(color="#ffa657", width=2.5, shape="spline"),
                hovertemplate="<b>%{x}</b><br>Tendencia: %{y:.2f} °C<extra></extra>"))
        _fig1.add_hline(y=0, line_color="#444c56", line_width=1.2)
        _fig1.add_vline(x=1975, line_color="#ffd700", line_width=1.2, line_dash="dot",
            annotation_text="Inflexión ~1975", annotation_font=dict(color="#ffd700", size=10),
            annotation_position="top left")
    _fig1.update_layout(height=440, plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font=dict(color="#c9d1d9"), title=dict(
            text="Anomalía anual de temperatura superficial global — NASA GISTEMP v4 (1880–2024)",
            font=dict(size=14, color="#e6edf3"), x=0.01),
        xaxis=dict(title="Año", gridcolor="#21262d", linecolor="#30363d",
                   rangeslider=dict(visible=True, thickness=0.04)),
        yaxis=dict(title="Anomalía (°C)", gridcolor="#21262d", linecolor="#30363d", zeroline=False),
        legend=dict(bgcolor="rgba(13,17,23,0.85)", bordercolor="#30363d", borderwidth=1,
                    font=dict(size=12), x=0.01, y=0.99),
        barmode="relative", bargap=0.06, hovermode="x unified",
        margin=dict(l=65, r=30, t=55, b=70))
    mo.vstack([_texto1, smooth_option, mo.ui.plotly(_fig1)])
    return


@app.cell(hide_code=True)
def _(mo):
    series_sel = mo.ui.multiselect(
        options=["Global","Hemisferio Norte","México — zona norte (24°N–44°N)","México — zona sur (0°–24°N)"],
        value=["Global","México — zona norte (24°N–44°N)","México — zona sur (0°–24°N)"],
        label="Zonas a comparar (media móvil 10 años):",
    )
    return (series_sel,)


@app.cell(hide_code=True)
def _(df_zonal, go, mo, series_sel):
    _texto2 = mo.md("""
    ---
    ## 2 · México bajo la lupa

    Las curvas representan distintas zonas del planeta con media móvil de 10 años. La línea gris
    es el promedio global. Las líneas dorada y roja pertenecen a las zonas que cubren México:
    norte (24°N–44°N) y sur (0°–24°N).

    **La zona norte de México se ha calentado consistentemente más rápido que el promedio global**
    desde la década de 1990. Esto tiene consecuencias directas: sequías más largas, olas de calor
    más frecuentes, y mayor presión sobre sistemas hídricos que ya operan al límite.

    > 🔍 **Interactivo:** activa o desactiva zonas con el selector para comparar trayectorias.
    """)
    _CFG = {
        "Global":                          ("global_r10",   "#aaaaaa", 2.0, "dash"),
        "Hemisferio Norte":                ("n_hem_r10",    "#4ecdc4", 1.8, "dot"),
        "México — zona norte (24°N–44°N)": ("mex_norte_r10","#ffd700", 2.8, "solid"),
        "México — zona sur (0°–24°N)":     ("mex_sur_r10",  "#ff7b72", 2.8, "solid"),
    }
    _fig2 = go.Figure()
    if not df_zonal.empty:
        for _n, (_c, _col, _w, _d) in _CFG.items():
            if _n in series_sel.value and _c in df_zonal.columns:
                _fig2.add_trace(go.Scatter(x=df_zonal["year"], y=df_zonal[_c], mode="lines",
                    name=_n, line=dict(color=_col, width=_w, dash=_d, shape="spline"),
                    hovertemplate=f"<b>%{{x}}</b> · {_n}<br><b>%{{y:.2f}} °C</b><extra></extra>"))
        _fig2.add_hline(y=0, line_color="#444c56", line_width=1.2)
        _fig2.add_vrect(x0=1990, x1=2024, line_width=0, fillcolor="#ff7b72", opacity=0.05,
            annotation_text="Aceleración post-1990", annotation_position="top right",
            annotation_font=dict(color="#ff7b72", size=10))
    else:
        _fig2.add_annotation(text="⚠ Datos no disponibles", showarrow=False,
            font=dict(color="white", size=18), xref="paper", yref="paper", x=0.5, y=0.5)
    _fig2.update_layout(height=480, plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font=dict(color="#c9d1d9"), title=dict(
            text="Anomalía por zona — comparación con México (media móvil 10 años)",
            font=dict(size=14, color="#e6edf3"), x=0.01),
        xaxis=dict(title="Año", gridcolor="#21262d", linecolor="#30363d"),
        yaxis=dict(title="Anomalía (°C)", gridcolor="#21262d", linecolor="#30363d", zeroline=False),
        legend=dict(bgcolor="rgba(13,17,23,0.85)", bordercolor="#30363d", borderwidth=1, font=dict(size=12)),
        hovermode="x unified", margin=dict(l=65, r=30, t=55, b=60))
    mo.vstack([_texto2, series_sel, mo.ui.plotly(_fig2)])
    return


@app.cell(hide_code=True)
def _(df_heatmap, go, mo):
    _texto3 = mo.md("""
    ---
    ## 3 · El calendario del calentamiento

    Cada celda muestra la anomalía de ese mes específico: **azul** = más frío que el promedio histórico;
    **rojo** = más cálido. Lo que hace poderosa esta visualización es ver **cuándo exactamente el rojo
    tomó control del calendario**. A partir de los años 80, el rojo colonizó el mapa de forma sistemática.
    Para 2010 en adelante, encontrar un mes azul es la excepción, no la regla.

    > 🔍 **Interactivo:** pasa el cursor sobre cualquier celda para ver el año, mes y anomalía exacta.
    """)
    _fig3 = go.Figure()
    if not df_heatmap.empty:
        _cs = [[0,"#08306b"],[0.15,"#2171b5"],[0.35,"#6baed6"],[0.47,"#deebf7"],
               [0.50,"#f7f7f7"],[0.53,"#fee0d2"],[0.65,"#fc8d59"],[0.85,"#d73027"],[1,"#67000d"]]
        _fig3.add_trace(go.Heatmap(
            z=df_heatmap.values.tolist(), x=[int(c) for c in df_heatmap.columns],
            y=df_heatmap.index.tolist(), colorscale=_cs, zmid=0, zmin=-1.8, zmax=1.8,
            colorbar=dict(title=dict(text="Anomalía<br>(°C)", font=dict(color="#c9d1d9", size=12)),
                          tickfont=dict(color="#c9d1d9"), outlinewidth=0, thickness=14, len=0.85),
            hovertemplate="<b>%{x} · %{y}</b><br>Anomalía: <b>%{z:.2f} °C</b><extra></extra>",
            xgap=0.3, ygap=0.3))
        _fig3.add_vline(x=1988, line_color="#ffa657", line_width=1.5, line_dash="dot",
            annotation_text="1988", annotation_font=dict(color="#ffa657", size=10),
            annotation_position="top")
    else:
        _fig3.add_annotation(text="⚠ Datos no disponibles", showarrow=False,
            font=dict(color="white", size=18), xref="paper", yref="paper", x=0.5, y=0.5)
    _fig3.update_layout(height=380, plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font=dict(color="#c9d1d9"), title=dict(
            text="Mapa de calor mensual: anomalía de temperatura global (1880–2024)",
            font=dict(size=14, color="#e6edf3"), x=0.01),
        xaxis=dict(title="Año", gridcolor="#21262d", linecolor="#30363d", dtick=20),
        yaxis=dict(title="", gridcolor="#21262d", linecolor="#30363d",
                   categoryorder="array",
                   categoryarray=["Dic","Nov","Oct","Sep","Ago","Jul","Jun","May","Abr","Mar","Feb","Ene"]),
        margin=dict(l=60, r=30, t=55, b=55))
    mo.vstack([_texto3, mo.ui.plotly(_fig3)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Conclusiones

    La pregunta con la que comenzamos tiene una respuesta que los datos hacen difícil de ignorar.

    **El cambio fue gradual y luego repentino.** Desde 1880 hasta circa 1975, las oscilaciones anuales
    dominaban sobre cualquier tendencia. A partir de ese punto la curva comenzó a inclinarse. El punto
    de no retorno llegó alrededor de **1988**, cuando la serie de récords de calor se volvió
    estadísticamente imposible de atribuir a la variabilidad natural.

    **México no es espectador.** La zona norte —Monterrey, Chihuahua, Hermosillo— se ha calentado
    consistentemente **por encima del promedio global** desde los noventa. Sequías más largas, olas de
    calor más frecuentes, mayor presión sobre sistemas hídricos que ya operan al límite.

    **El mapa de calor cuenta la historia más honesta**: el calendario ya no es azul con manchas rojas.
    Es rojo, con escasas memorias de azul. Lo que era extremo en 1950 es, hoy, un mes promedio.

    ---

    <div style="background:#f0f4f8;border-radius:8px;padding:20px 24px;">
    <p style="color:#1a1a2e;font-size:0.85em;line-height:2;margin:0;">
    <strong>📂 Fuentes de datos</strong><br>
    · NASA GISS Surface Temperature Analysis (GISTEMP v4) — Global Annual Mean<br>
    &nbsp;&nbsp;https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv — descargado 2026-04-23<br>
    · NASA GISTEMP v4 — Zonal Annual Means<br>
    &nbsp;&nbsp;https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv — descargado 2026-04-23<br>
    · Licencia: dominio público (gobierno de EE.UU.) · Anomalías en °C respecto a media 1951–1980
    </p>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
