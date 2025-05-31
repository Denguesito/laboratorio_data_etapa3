import os
from database.conexion import DataSaver
from domain.csv_model import CSVDataset
from domain.excel_model import ExcelDataset


def cargar_csv_y_excel():
    csv_path = os.path.join(os.path.dirname(__file__), 'files', 'datos_clientes.csv')
    excel_path = os.path.join(os.path.dirname(__file__), 'files', 'datos_compras.xlsx')

    csv_dataset = CSVDataset(csv_path)
    csv_dataset.cargar()
    csv_dataset.resumen()

    excel_dataset = ExcelDataset(excel_path)
    excel_dataset.cargar()
    excel_dataset.resumen()

    saver = DataSaver()
    saver.guardar(csv_dataset.datos, 'clientes_csv')
    saver.guardar(excel_dataset.datos, 'compras_excel')


if __name__ == "__main__":
    cargar_csv_y_excel()