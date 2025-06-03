from domain.base_model import DatasetBase
import pandas as pd


class CSVDataset(DatasetBase):
    @classmethod
    def leer_archivo(cls, ruta):
        df = pd.read_csv(ruta)
        return cls(df)

    def validar(self):
        if self._datos is None:
            raise Exception("No hay datos cargados")
        if self._datos.isnull().any().any():
            print("Advertencia: Hay valores nulos en los datos.")
        if self._datos.duplicated().any():
            print("Advertencia: Hay filas duplicadas.")
        print("Validación completada.")
        return True

    @classmethod
    def nombre_tabla(cls):
        return "csv_data"
    
    def cargar(self):
        print("Cargando datos CSV...")
        self._datos = pd.read_csv(self._fuente)
        print("Datos cargados.")
        self.limpiar()
        self.validar()
    
    def mostrar_resumen(self):
        print("Mostrando resumen de datos:")
        self.resumen()