import pandas as pd
import streamlit as st
import plotly.express as px

# Area and shot type mappings
area_codes = {"A1": "Zona 1", "A2": "Zona 2", "A3": "Zona 3", "A4": "Zona 4"}
shot_type_codes = {1: "Tiro libre", 2: "Tiro de campo", 3: "Tiro de 3 puntos", 4: "Bandeja"}

# Function to load and process data for a given match
def load_match_data(sheet_name):
    data = pd.read_excel("Datos_Basketball_patido_NBA.xlsx", sheet_name=sheet_name, usecols="A:D")
    data["Área"] = data["Área"].map(area_codes)
    data["Tipo de Tiro"] = data["Tipo de Tiro"].map(shot_type_codes)
    return data

# Streamlit app
st.title("Dashboard de Análisis de Tiros")

# Match selection dropdown
match_options = ["Partido 1", "Partido 2", "Partido 3", "Partido 4", "Partido 5"]
selected_match = st.selectbox("Seleccionar Partido", match_options)

# Load and process data for the selected match
data = load_match_data(selected_match)

# Display area and shot type codifications
st.sidebar.header("Codificación")
st.sidebar.write("Áreas:", area_codes)
st.sidebar.write("Tipos de Tiro:", shot_type_codes)

# Main table with scroll functionality
st.header("Datos de Tiros")
st.dataframe(data)

# Label for shot data
st.header("Datos de Tiros")

# Display shot areas reference graph
st.image("Área de tiro.png")

# Interactive visualizations
st.header("Visualizaciones")

# Combine data from all matches for overall visualizations
all_matches_data = pd.concat([load_match_data(sheet) for sheet in match_options])

# Chance of scoring by shot number
fig5 = px.line(
    all_matches_data,
    x="Número de Tiro",
    y="Encestó",
    title="Probabilidad de Encestar por Número de Tiro (Todos los Partidos)",
)
st.plotly_chart(fig5)

# Shots made vs missed by area
fig1 = px.histogram(
    all_matches_data,
    x="Área",
    color="Encestó",
    barmode="group",
    title="Tiros Encestados vs Fallados por Área (Todos los Partidos)",
)
st.plotly_chart(fig1)

# Shots made vs missed by shot type
fig2 = px.histogram(
    all_matches_data,
    x="Tipo de Tiro",
    color="Encestó",
    barmode="group",
    title="Tiros Encestados vs Fallados por Tipo de Tiro (Todos los Partidos)",
)
st.plotly_chart(fig2)

# Shot success rate by area
shot_counts = all_matches_data.groupby("Área")["Encestó"].value_counts(normalize=True).unstack()
fig3 = px.bar(shot_counts, title="Porcentaje de Tiros Encestados por Área (Todos los Partidos)")
st.plotly_chart(fig3)

# Shot success rate by shot type
shot_counts = all_matches_data.groupby("Tipo de Tiro")["Encestó"].value_counts(normalize=True).unstack()
fig4 = px.bar(shot_counts, title="Porcentaje de Tiros Encestados por Tipo de Tiro (Todos los Partidos)")
st.plotly_chart(fig4)
