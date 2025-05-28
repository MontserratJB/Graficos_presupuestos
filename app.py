from dash import Dash, html, dcc
from graficos import generar_grafico

app = Dash(__name__)
figura = generar_grafico()

app.layout = html.Div([
    html.H1("Presupuesto Municipal 2023"),
    dcc.Graph(figure=figura)
])

if __name__ == "__main__":
    app.run_server(debug=True)
