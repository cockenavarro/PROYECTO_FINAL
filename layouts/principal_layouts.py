from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H1("Explora el Clima", className="display-4 text-center", style={'color': '#FFFFFF'}),
                        html.P(
                            "Descubre patrones y tendencias en los datos climáticos.",
                            className="lead text-center text-white"
                        ),
                        html.Div(
                            [
                                dcc.Dropdown(
                                    id='page-selector',
                                    options=[
                                        {'label': 'Precipitación', 'value': '/precipitation'},
                                        {'label': 'Temperatura', 'value': '/temperature'},
                                    ],
                                    value=None,
                                    placeholder="Selecciona una opción",
                                    style={'width': '100%'}
                                ),
                            ],
                            className="text-center mt-3"
                        ),
                        html.P("¡Explora y disfruta de la visualización de datos climáticos!",
                               className="text-center mt-3 text-white"),
                    ],
                    className="jumbotron jumbotron-fluid",
                    style={'background-color': '#2C3E50', 'border-radius': '15px', 'padding': '20px',
                           'box-shadow': '0px 0px 20px 0px #FF4D00'}
                ),
                className="mb-4"
            ),
            justify="center"
        ),
        html.Div(id='page-content')
    ],
    fluid=True,
    style={'background-color': '#3498DB', 'height': '100vh', 'padding': '20px', 'transition': 'background-color 0.5s'}
)