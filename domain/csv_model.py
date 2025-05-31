from domain.base_model import DatasetBase
import pandas as pd


class CSVDataset(DatasetBase):
    @classmethod
    def leer_archivo(cls, ruta):
        df = pd.read_csv(ruta)
        return cls(df)

    def validar(self):
        # Ejemplo: validar que no haya nulos y tipos básicos
        if self._datos is None:
            raise Exception("No hay datos cargados")
        if self._datos.isnull().any().any():
            print("Advertencia: Hay valores nulos en los datos.")
        if self._datos.duplicated().any():
            print("Advertencia: Hay filas duplicadas.")
        return True

    @classmethod
    def nombre_tabla(cls):
        return "csv_data"
    
    def cargar(self):
        self._datos = pd.read_csv(self._fuente)
        self.limpiar()
        self.validar()
        
    def mostrar_resumen(self):
        self.resumen()