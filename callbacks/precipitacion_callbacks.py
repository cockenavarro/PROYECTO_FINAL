import datetime
from dash.dependencies import Input, Output, State
from database import obtener_datos_precipitaciones
from dash.exceptions import PreventUpdate
from layouts.precipitacion_layouts import layout as precipitacion_layout
from layouts.temperatura_layouts import layout as temperatura_layout
from layouts.principal_layouts import layout as principal
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def display_page(selected_option, app):
    # Lógica para cambiar el contenido según la opción seleccionada
    if selected_option == '/precipitation':
        return precipitacion_layout
    elif selected_option == '/temperature':
        return temperatura_layout
    else:
        return 'Seleccione una opción'
    
def generate_precipitation_map(df_filtered):
    # Asegúrate de que las columnas 'latitud', 'longitud' y 'precipitacion' existan en tu DataFrame
    if 'latitud' not in df_filtered.columns or 'longitud' not in df_filtered.columns or 'precipitacion' not in df_filtered.columns:
        raise ValueError("El DataFrame no tiene las columnas necesarias para generar el mapa de precipitaciones.")

    # Configuración de la figura utilizando Scattermapbox
    fig = go.Figure()

    # Añade trazos al mapa para cada punto de latitud y longitud
    fig.add_trace(
        go.Scattermapbox(
            lat=df_filtered['latitud'],
            lon=df_filtered['longitud'],
            mode='markers',
            marker=dict(
                size=5,
                color=df_filtered['precipitacion'],
                colorscale='rainbow',
                colorbar=dict(title='Pr')
            ),
            text=df_filtered['precipitacion'],  # Texto que se muestra al pasar el ratón sobre un punto
        )
    )

    # Configuración del diseño del mapa
    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            center=dict(lat=df_filtered['latitud'].mean(), lon=df_filtered['longitud'].mean()),  # Centra el mapa en el promedio de las coordenadas
            zoom=2,  # Ajusta el nivel de zoom
        )
    )

    return fig
    
def update_precipitation_map_options(selected_date, app):
    try:
        # Obtén los datos desde la base de datos
        df_precipitaciones = obtener_datos_precipitaciones()

        # Filtra los datos para la fecha seleccionada
        df_selected_date = df_precipitaciones[df_precipitaciones['fecha'] == selected_date]

        # Actualiza el mapa con los datos filtrados
        map_figure = generate_precipitation_map(df_selected_date)

        # Obtiene el rango de fechas disponible
        date_range = df_precipitaciones['fecha'].unique()

        # Convierte las fechas a un formato adecuado para el Dropdown
        date_options = [{'label': datetime.strptime(str(date), '%Y-%m-%d').strftime('%b %d, %Y'), 'value': str(date)} for date in date_range]

         # Imprime el contenido de date_options
        print("date_options:", date_options)

        return map_figure, date_options

    except Exception as e:
        print(f"Error en la actualización del mapa: {str(e)}")
        return {}, []