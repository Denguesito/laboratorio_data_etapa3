import pandas as pd
from domain.base_model import DatasetBase

class ExcelDataset(DatasetBase):
    def cargar(self):
        print("Cargando datos de Excel...")
        self._datos = pd.read_excel(self._fuente)
        print("Datos cargados.")
        self.limpiar()
        self.validar()

    def validar(self):
        if self._datos is None:
            raise Exception("No hay datos cargados")
        if self._datos.isnull().any().any():
            print("Advertencia: Hay valores nulos en los datos.")
        if self._datos.duplicated().any():
            print("Advertencia: Hay filas duplicadas.")
        print("Validación completada.")
        return True

    def mostrar_resumen(self):
        print("Mostrando resumen de datos:")
        self.resumen()
