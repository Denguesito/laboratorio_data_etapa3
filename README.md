Este proyecto es una aplicación modular en Python para cargar, validar y almacenar datos desde archivos (.csv, .xlsx, .json, etc.) en una base de datos relacional usando SQLAlchemy.


## Ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

## Características
- Carga automática de archivos desde `/files/`
- Validación de tipos, campos obligatorios, duplicados y nulos
- Persistencia en base de datos relacional (una tabla por archivo)
- Modularidad y uso de POO (abstracción, herencia, polimorfismo, encapsulamiento)

## Dependencias principales
- pandas
- SQLAlchemy
- pymsql
- python-decouple
- openpyxl


## Notas
- Puedes agregar más modelos en `/domain/` para soportar otros formatos.
- Los archivos de datos deben estar en `/files/`.