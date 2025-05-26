import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('Electric Vehicle Population Data.csv')

# Título
st.header('Panel de Vehículos Eléctricos en WA')

# Botón para histograma
if st.button('Mostrar histograma del rango eléctrico'):
    st.write('Distribución del rango eléctrico (Electric Range)')
    fig = px.histogram(df, x='Electric Range')
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Rango eléctrico por año del modelo')
    fig2 = px.scatter(df, x='Model Year', y='Electric Range')
    st.plotly_chart(fig2)

