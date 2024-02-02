# app/layouts/precipitacion_layouts.py
from dash import html
from dash import dcc

# Layout mejorado
layout = html.Div([
    html.H1("Visualización Precipitaciones 1979-2019", style={'text-align': 'center', 'color': '#FFFFFF'}),

    html.Div([
        html.Div(id='output-filename', style={'margin-bottom': '10px'}),
        html.Label("Seleccionar Fecha", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='time-selector',
            multi=False
        ),
    ], style={'background-color': '#f2f2f2', 'padding': '20px', 'border-radius': '10px'}),

    # Mapa interactivo
    dcc.Graph(
        id='precipitation-map',
        style={'height': '80vh'}
        
    ),
    # Agrega un componente oculto para time-selector
    html.Div(id='time-selector-container', style={'display': 'none'}),
], style={'width': '80%', 'margin': 'auto'})

