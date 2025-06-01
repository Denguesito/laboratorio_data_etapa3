from abc import ABC, abstractmethod

class DatasetBase(ABC):
    def __init__(self, fuente):
        self._fuente = fuente
        self._datos = None

    @property
    def datos(self):
        return self._datos

    @abstractmethod
    def cargar(self):
        pass

    def limpiar(self):
        if self._datos is not None:
            self._datos = self._datos.drop_duplicates().dropna()
            print("Datos limpiados.")

    def transformar(self):
        if self._datos is not None:
            self._datos.columns = self._datos.columns.str.lower().str.replace(' ', '_')
            for col in self._datos.select_dtypes(include='object').columns:
                self._datos[col] = self._datos[col].astype(str).str.strip()
            print("Transformación confirmada.")
        else:
            print("No hay datos para transformar.")

    def validar(self):
        try:
            if self._datos is None:
                raise Exception("No hay datos cargados")
            if self._datos.isnull().any().any():
                print("Advertencia: Hay valores nulos en los datos.")
            if self._datos.duplicated().any():
                print("Advertencia: Hay filas duplicadas.")
            print("Validación completada.")
            return True
        except Exception as e:
            print(f"Error en validación: {e}")
            return False

    def resumen(self):
        try:
            if self._datos is not None:
                print("Mostrando resumen de datos:")
                print(self._datos.describe(include='all'))
            else:
                print("No hay datos para mostrar resumen.")
        except Exception as e:
            print(f"Error al mostrar resumen: {e}")