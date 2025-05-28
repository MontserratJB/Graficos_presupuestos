import pandas as pd
import plotly.express as px

def generar_grafico():
    # Cargar los datos desde el CSV
    df = pd.read_csv("datos_presupuesto.csv")

    # Asegurar que los valores sean numéricos
    df['Presupuesto'] = pd.to_numeric(df['Presupuesto'], errors='coerce')
    df['Ejecutado'] = pd.to_numeric(df['Ejecutado'], errors='coerce')

    # Calcular el porcentaje de ejecución
    df['% Ejecución'] = (df['Ejecutado'] / df['Presupuesto']) * 100

    # Crear gráfico de barras con Plotly
    fig = px.bar(
        df,
        x='Programa',
        y=['Presupuesto', 'Ejecutado'],
        barmode='group',
        labels={'value': 'Colones', 'variable': 'Categoría'},
        title='Comparativo de Presupuesto y Ejecución por Programa'
    )

    fig.update_layout(
        xaxis_title="Programa",
        yaxis_title="Monto (₡)",
        legend_title="",
        template="plotly_white"
    )

    return fig
