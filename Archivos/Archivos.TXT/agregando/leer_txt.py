
with open("Archivos\\Archivos.TXT\\agregando\\archivo_creado(agregando).txt", encoding="UTF-8") as archivo :
    
    print("Este es el contenido del archivo txt: ")
    #usamos un bucle for para leer cada línea del archivo hasta que se terminen
    for linea in archivo :
        print(linea.strip()) #el método .strip() sirve para eliminar el salto de línea al final de cada línea


#el archivo se cierra automáticamente






