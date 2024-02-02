# app.py
from dash import Dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from layouts.principal_layouts import layout as principal
from layouts.precipitacion_layouts import layout as precipitacion_layouts
from callbacks.precipitacion_callbacks import display_page, update_precipitation_map_options

app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN], suppress_callback_exceptions=True)

# Diseño principal mejorado
app.layout = principal

# Callback para cambiar el contenido según la opción seleccionada
app.callback(
    Output('page-content', 'children'),
    [Input('page-selector', 'value')]
)(lambda selected_option: display_page(selected_option, app))

app.callback(
    [Output('precipitation-map', 'figure'),
     Output('time-selector', 'children')],
    [Input('time-selector', 'value')]
)(lambda selected_option: update_precipitation_map_options(selected_option, app))

if __name__ == '__main__':
    app.run_server(debug=True)
