# Paso 1: Importa la biblioteca Pandas.
import pandas as pd

# Paso 2: Lee los datos del archivo 'winemag-data-130k-v2.csv'.
df = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

# Paso 3: Realizar el análisis y procesamiento de los datos según lo indicado en el problema.
# Por ejemplo, vamos a calcular el promedio del puntaje (points) de los vinos por país.
promedio_puntajes_por_pais = df.groupby('country')['points'].mean()

# Mostrar los primeros 10 resultados.
print("Promedio de puntajes por país:")
print(promedio_puntajes_por_pais.head(10))

# Paso 4: Guarda los resultados o realiza las operaciones adicionales necesarias.

