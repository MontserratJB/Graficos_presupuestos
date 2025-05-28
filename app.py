import dash
from dash import html

# Crear la app Dash
app = dash.Dash(__name__)

# Layout simple para prueba
app.layout = html.Div("Hola desde Dash")

# Este bloque permite correr localmente
if __name__ == "__main__":
    app.run_server(debug=True)
