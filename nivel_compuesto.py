
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nivelación Topográfica", layout="centered")

st.title("📐 Nivelación Topográfica - Tabla de Puntos")

# Inicializa sesión para guardar puntos y la HI
if "puntos" not in st.session_state:
    st.session_state.puntos = []
if "hi_actual" not in st.session_state:
    st.session_state.hi_actual = None

# Entradas
cota_base = st.number_input("• Cota base inicial (BM)", step=0.01)

usar_como_base = st.checkbox("Usar como cota base", value=True)
progresiva = st.text_input("📏 Progresiva")

vista_atras = st.number_input("• Vista Atrás (si hay cambio de estación)", step=0.01)
vista_adelante = st.number_input("• Vista Adelante", step=0.01)

# Botón para agregar punto
if st.button("➕ Agregar punto"):
    if len(st.session_state.puntos) == 0 and usar_como_base:
        hi = cota_base + vista_atras
        cota_nueva = hi - vista_adelante
        st.session_state.hi_actual = hi
        st.session_state.puntos.append({
            "Progresiva": progresiva,
            "Vista Atrás": vista_atras,
            "HI": hi,
            "Vista Adelante": vista_adelante,
            "Cota": cota_nueva
        })
    else:
        # Si hay nueva vista atrás, se cambia de estación
        if vista_atras != 0:
            cota_base = st.session_state.puntos[-1]["Cota Nueva"]
            hi = cota_base + vista_atras
            st.session_state.hi_actual = hi
        else:
            hi = st.session_state.hi_actual

        if st.session_state.puntos:
            cota_base = st.session_state.puntos[-1]["Cota Nueva"]
        else:
            cota_base = 100

        else:
            cota_base = st.session_state.cota_base  # Ya viene del input
        cota_nueva = hi - vista_adelante
        st.session_state.puntos.append({
            "Progresiva": progresiva,
            "Vista Atrás": vista_atras,
            "HI": hi,
            "Vista Adelante": vista_adelante,
            "Cota": cota_nueva
        })

# Mostrar tabla
st.subheader("📋 Registro de Puntos")
df = pd.DataFrame(st.session_state.puntos)
st.dataframe(df, use_container_width=True)

# Opción para descargar como CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Descargar como CSV",
    data=csv,
    file_name="nivelacion_topografica.csv",
    mime="text/csv")