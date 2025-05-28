
import pandas as pd
import plotly.express as px

def generar_grafico():
    # Cargar los datos desde el CSV con codificación 'latin1' y separador ';'
    df = pd.read_csv("datos_presupuesto.csv", encoding='latin1', sep=';')

    # Asegurar que los valores sean numéricos
    df['TOTAL GENERAL'] = pd.to_numeric(df['TOTAL GENERAL'], errors='coerce')

    # Crear gráfico de barras apiladas con Plotly
    fig = px.bar(
        df,
        x='CATEGORIA',
        y='TOTAL GENERAL',
        color='SUBCATEGORIA',
        labels={'TOTAL GENERAL': 'Monto Total (₡)', 'CATEGORIA': 'Categoría', 'SUBCATEGORIA': 'Subcategoría'},
        title='Comparativo de Presupuesto por Categoría y Subcategoría'
    )

    fig.update_layout(
        xaxis_title="Categoría",
        yaxis_title="Monto Total (₡)",
        legend_title="Subcategoría",
        template="plotly_white"
    )

    return fig

# Generar el gráfico
figura = generar_grafico()

# Mostrar el gráfico
figura.show()

