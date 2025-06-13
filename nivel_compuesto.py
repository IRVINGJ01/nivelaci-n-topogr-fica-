
import streamlit as st
import pandas as pd

st.title("📐 Nivelación Topográfica - Tabla de Puntos")

# Inicializar sesión
if "puntos" not in st.session_state:
    st.session_state.puntos = []
    st.session_state.cota_actual = None

# Entrada inicial: solo la primera vez
if st.session_state.cota_actual is None:
    cota_base = st.number_input("🔹 Cota base inicial (BM)", step=0.01)
    if st.button("✅ Usar como cota base"):
        st.session_state.cota_actual = cota_base

# Si ya hay cota activa, mostrar formulario de nuevos puntos
if st.session_state.cota_actual is not None:
    st.subheader("Agregar nuevo punto")

    vista_atras = st.number_input("🔹 Vista Atrás (si hay cambio de estación)", step=0.01, key="va")
    vista_adelante = st.number_input("🔹 Vista Adelante", step=0.01, key="va_de")

    if st.button("➕ Agregar punto"):
        hi = st.session_state.cota_actual + vista_atras
        nueva_cota = hi - vista_adelante

        punto = {
            "Cota Base": st.session_state.cota_actual,
            "Vista Atrás": vista_atras,
            "HI": hi,
            "Vista Adelante": vista_adelante,
            "Cota Nueva": nueva_cota
        }

        st.session_state.puntos.append(punto)
        st.session_state.cota_actual = nueva_cota  # actualizar para el siguiente punto

# Mostrar tabla
if st.session_state.puntos:
    st.subheader("📋 Registro de Puntos")
    df = pd.DataFrame(st.session_state.puntos)
    st.dataframe(df, use_container_width=True)

# Botón para descargar como CSV
if st.session_state.puntos:
    df = pd.DataFrame(st.session_state.puntos)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Descargar como CSV",
        data=csv,
        file_name="nivelacion_topografica.csv",
        mime="text/csv")
