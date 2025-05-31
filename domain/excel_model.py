import pandas as pd
from domain.base_model import DatasetBase

class ExcelDataset(DatasetBase):
    def cargar(self):
        self._datos = pd.read_excel(self._fuente)
        self.limpiar()
        self.validar()
        
    def mostrar_resumen(self):
        self.resumen()
        
    def validar(self):
        if self._datos is None:
            raise Exception("No hay datos cargados")
        if self._datos.isnull().any().any():
            print("Advertencia: Hay valores nulos en los datos.")
        if self._datos.duplicated().any():
            print("Advertencia: Hay filas duplicadas.")
        return True
