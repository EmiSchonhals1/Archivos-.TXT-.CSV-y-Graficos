import pandas as pd  #pd es la sigla universal con la que se conoce a la librería pandas

#usamos la función .read_csv para leer el archivo.CSV
df = pd.read_csv("Archivos\\Archivos.CSV\\archivo_creado.csv")

#df (DATA FRAME) son estructuras de datos bidimensionales parecidos a una hoja de cálculo, por ende tiene sólo dos valores: Filas y Columnas

#Mostrar todo el CSV utilizando el slicing
print("Lectura del CSV completo: \n")
print (df[:])

print("----------------------------------------------------------------")

#mostrar sólo la columna nombre
print("Columna 'nombre': \n")
print (df["Nombre"])

print("----------------------------------------------------------------")

#ordenar por altura DESCENDENTE
df_ordenado_descendente = df.sort_values("Altura", ascending=False)
print("df ordenado por altura DESCENDENTE: \n")
print(df_ordenado_descendente)

print("----------------------------------------------------------------")

#ordenar por peso ASCENDENTE
df_ordenado_ascendente = df.sort_values("Peso")
print("df ordenado por peso ASCENDENTE: \n")
print(df_ordenado_ascendente)

