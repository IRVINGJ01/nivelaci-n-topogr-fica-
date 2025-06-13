
import streamlit as st

st.title("📐 Calculadora de Nivel Fijo")

# Entrada de datos
nrf = st.number_input("Altura del Nivel de Referencia Fijo (NRF)", step=0.01)
lectura = st.number_input("Lectura del punto con la mira", step=0.01)

# Cálculo
nivel = nrf - lectura

# Resultado
st.success(f"Nivel del punto medido: {nivel:.2f} m")