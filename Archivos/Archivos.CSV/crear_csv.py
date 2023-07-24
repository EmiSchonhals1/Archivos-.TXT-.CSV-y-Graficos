# Forma óptima de crear un CSV

#importamos pandas y le damos un alias
import pandas as pd

#creamos los datos que deseamos almacenar en el CSV en forma de diccionario o lista de listas
datos = {
    'Nombre': ['Emi', 'Nico', 'Carlos', 'Germán'],
    'Edad' : ['20', '21', '26', '34'],
    'Altura' : ['1.85', '1.77', '1.68', '1.92'],
    'Peso' : ['84', '75', '93.3', '99.2']
}

#creamos un dataframe (df), que son estructuras de datos bidimensionales parecidos a una hoja de cálculo, por ende tienen sólo dos valores: Filas y Columnas
df = pd.DataFrame(datos)

#le damos un nombre al archivo csv y luego mandamos el df al mismo usando el método .to_csv()
nombre_archivo = "Archivos\\Archivos.CSV\\archivo_creado.csv"
df.to_csv(nombre_archivo, index=False)
#El argumento index=False es importante ya que evita que se guarde la columna de índices en el archivo CSV




