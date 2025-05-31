from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from decouple import config


class DataSaver:
    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)

    def guardar(self, df, tabla):
        if df is None or not isinstance(df, pd.DataFrame):
            print(f"No se puede guardar: datos vacíos o tipo incorrecto para {tabla}")
            return
        try:
            df.to_sql(tabla, con=self.engine, if_exists='replace', index=False)
            print(f"Datos guardados en la tabla: {tabla}")
        except SQLAlchemyError as e:
            print(f"Error al guardar en la base de datos: {e}")