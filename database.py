from psycopg2 import sql
import pandas as pd
from config import db_config as db # Asegúrate de importar las configuraciones correctamente
from sqlalchemy import create_engine, Table, Column, MetaData, Float, Integer

def obtener_datos_precipitaciones():
    print("Intentando establecer conexión a la base de datos...")
    try:
        # Crear la conexión de SQLAlchemy
        engine = create_engine(f"postgresql+psycopg2://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['dbname']}")

        # Consulta SQL
        query = "SELECT * FROM proyecto.precipitaciones;"

        # Leer datos en un DataFrame de pandas
        df = pd.read_sql_query(query, engine)

        print("Conexión exitosa a la base de datos.")
        return df

    except Exception as e:
        print(f"Error durante la conexión a la base de datos: {e}")
        return None

# Verificar si se obtienen datos
df_precipitaciones = obtener_datos_precipitaciones()
#print(df_precipitaciones)
