import pandas as pd
from envio_correo import enviar_correo
import pc4_api  # Suponiendo que ya has implementado la función para obtener el valor del dólar actual

def limpiar_columnas(df):
    # Renombrar columnas eliminando espacios, tildes y convirtiéndolas a minúsculas
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    # Eliminar columnas repetidas
    df = df.loc[:, ~df.columns.duplicated()]
    
    # Eliminar el carácter coma de la columna 'dispositivo_legal'
    df['dispositivo_legal'] = df['dispositivo_legal'].str.replace(',', '')

    return df

def dolarizar_valores(df):
    # Obtener el valor actual del dólar desde la API
    valor_dolar = pc4_api.obtener_valor_dolar()

    # Dolarizar los valores de montos de inversión y transferencia
    df['monto_inversion_usd'] = df['monto_inversion'] / valor_dolar
    df['monto_transferencia_usd'] = df['monto_transferencia'] / valor_dolar

    return df

def mapear_estado(estado):
    if estado == 'Actos Previos':
        return 1
    elif estado == 'Resuelto':
        return 0
    elif estado == 'Ejecucion':
        return 2
    elif estado == 'Concluido':
        return 3

def puntuar_estado(df):
    df['estado_puntuado'] = df['estado'].apply(mapear_estado)

    return df

def generar_reporte_ubigeos(df):
    # Eliminar duplicados de las columnas 'ubigeo', 'Region', 'Provincia', 'Distrito'
    ubigeos_sin_duplicados = df[['ubigeo', 'Region', 'Provincia', 'Distrito']].drop_duplicates()

    # Almacenar en una base de datos
    # ubigeos_sin_duplicados.to_sql('ubigeos', con=engine, if_exists='replace')

def generar_reporte_por_region(df):
    # Filtrar obras de tipo Urbano y estado 1, 2, 3
    df_filtrado = df[(df['tipo_obra'] == 'Urbano') & (df['estado_puntuado'].isin([1, 2, 3]))]

    # Agrupar por región y obtener el top 5 de costo de inversión
    for region, datos_region in df_filtrado.groupby('Region'):
        top5_costo_inversion = datos_region.nlargest(5, 'monto_inversion_usd')
        if not top5_costo_inversion.empty:
            top5_costo_inversion.to_excel(f'{region}_top5_costo_inversion.xlsx', index=False)

if __name__ == "__main__":
    # Leer el archivo 'reactiva.xlsx'
    df = pd.read_excel('reactiva.xlsx')

    # Realizar limpieza de columnas
    df = limpiar_columnas(df)

    # Dolarizar valores
    df = dolarizar_va
