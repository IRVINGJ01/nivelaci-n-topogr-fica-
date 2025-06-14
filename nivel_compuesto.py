
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nivelación Topográfica", layout="centered")
st.title("📐 Nivelación Topográfica - Tabla de Puntos")

# Inicializa variables de sesión
if "puntos" not in st.session_state:
    st.session_state.puntos = []

if "hi_actual" not in st.session_state:
    st.session_state.hi_actual = None

# Entradas del usuario
progresiva = st.text_input("📏 Progresiva")
vista_atras = st.number_input("👈 Vista Atrás (si hay cambio de estación)", step=0.01)
vista_adelante = st.number_input("👉 Vista Adelante", step=0.01)

if st.button("➕ Agregar punto"):

    # Si hay vista atrás, se cambia estación
    if vista_atras != 0:
        # Si ya hay puntos anteriores, se toma la última cota
        if st.session_state.puntos:
            cota_base = st.session_state.puntos[-1].get("Cota Nueva", 100)
        else:
            cota_base = 100  # Valor por defecto si es el primer punto

        hi = cota_base + vista_atras
        st.session_state.hi_actual = hi

    else:
        hi = st.session_state.hi_actual
        if st.session_state.puntos:
            cota_base = st.session_state.puntos[-1].get("Cota Nueva", 100)
        else:
            cota_base = 100

    cota_nueva = hi - vista_adelante

    st.session_state.puntos.append({
        "Progresiva": progresiva,
        "Vista Atrás": vista_atras,
        "HI": hi,
        "Vista Adelante": vista_adelante,
        "Cota Nueva": cota_nueva
    })

# Mostrar tabla
st.subheader("📋 Registro de Puntos")
df = pd.DataFrame(st.session_state.puntos)
st.dataframe(df, use_container_width=True)

# Botón para descargar
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇ Descargar como CSV", csv, "nivelacion_topografica.csv","text/csv")