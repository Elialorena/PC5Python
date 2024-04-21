# Paso 1: Abrir Jupyter Notebook.
# Abrir Jupyter Notebook desde la terminal.

# Paso 2: Crear un nuevo notebook 
# Clic en "New" y seleccionar "Python 3" para crear un nuevo notebook.

# Paso 3: Importar la biblioteca Pandas.
import pandas as pd

# Paso 4: Lee los datos del archivo.
# Reemplaza 'nombre_del_archivo.csv' con el nombre y la ubicación del archivo CSV.
df = pd.read_csv('nombre_del_archivo.csv')

# Paso 5: Realizar el análisis según el problema planteado.
# Un ejemplo para mostrar las primeras filas de datos:
print("Primeras filas de datos:")
print(df.head())

# Se puede agregar codigo para seguir analizando los datos.

# Paso 6: Guarda los resultados 
