import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('datos_presupuesto.csv')

st.title("Presupuesto Municipal 2023")

fig = px.bar(df, x='Programa', y='Presupuesto', color='Ejecución')
st.plotly_chart(fig)
