#así se lee un archivo txt

with open ("Archivos\\Archivos.TXT\\sobreescribiendo\\archivo_creado(sobreescribiendo).txt", encoding="utf-8") as archivo :
   
    print("Contenido del archivo txt: ")
    #usamos un bucle for para leer cada línea del archivo hasta que se terminen
    for linea in archivo :
        print(linea.strip()) #el método .strip() sirve para eliminar el salto de línea al final de cada línea
        
        
#el archivo se cierra automáticamente