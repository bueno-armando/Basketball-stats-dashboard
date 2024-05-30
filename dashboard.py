import pandas as pd
import streamlit as st
import plotly.express as px

# Read data from the spreadsheet (replace with your actual file)
data = pd.read_excel("Datos_Basketball_patido_NBA.xlsx", sheet_name="Partido1", usecols="A:D")

# Define area and shot type codifications
area_codes = {"A1": "Zona 1", "A2": "Zona 2", "A3": "Zona 3", "A4": "Zona 4"}
shot_type_codes = {1: "Tiro libre", 2: "Tiro de campo", 3: "Tiro de 3 puntos", 4: "Bandeja"}

# Apply codifications to the data
data["Área"] = data["Área"].map(area_codes)
data["Tipo de Tiro"] = data["Tipo de Tiro"].map(shot_type_codes)

# Create Streamlit app
st.title("Dashboard de Análisis de Tiros")

# Display area and shot type codifications
st.sidebar.header("Codificación")
st.sidebar.write("Áreas:", area_codes)
st.sidebar.write("Tipos de Tiro:", shot_type_codes)

# Main table with scroll functionality
st.header("Datos de Tiros")
st.dataframe(data)

# Interactive visualizations
st.header("Visualizaciones")

# Shots made vs missed by area
fig1 = px.histogram(data, x="Área", color="Encestó", barmode="group",
                   title="Tiros Encestados vs Fallados por Área")
st.plotly_chart(fig1)

# Shots made vs missed by shot type
fig2 = px.histogram(data, x="Tipo de Tiro", color="Encestó", barmode="group",
                   title="Tiros Encestados vs Fallados por Tipo de Tiro")
st.plotly_chart(fig2)

# Shot success rate by area
shot_counts = data.groupby("Área")["Encestó"].value_counts(normalize=True).unstack()
fig3 = px.bar(shot_counts, title="Porcentaje de Tiros Encestados por Área")
st.plotly_chart(fig3)

# Shot success rate by shot type
shot_counts = data.groupby("Tipo de Tiro")["Encestó"].value_counts(normalize=True).unstack()
fig4 = px.bar(shot_counts, title="Porcentaje de Tiros Encestados por Tipo de Tiro")
st.plotly_chart(fig4)