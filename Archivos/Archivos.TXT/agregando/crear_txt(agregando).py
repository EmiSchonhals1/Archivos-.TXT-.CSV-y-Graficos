#Forma ÓPTIMA de trabajar con archivos.CSV

#en este caso lo abriremos para agregar datos, por ende ponemos la "a" de append
with open("Archivos\\Archivos.TXT\\agregando\\archivo_creado(agregando).txt", "a", encoding="UTF-8") as archivo :
    #No borra los datos anteriores del archivo.txt, sino que agrega lo que ingresemos al archivo
    #podemos usar las mismas operaciones que usábamos en el "w", con la diferencia de que al poner la "a" nos lo agregará sin eliminar todos los datos anteriores del archivo.txt

    #archivo.write("\n") si queremos que nos dé un salto de línea si hay algo antes de lo agregado
    
    cant_renglones = int(input("Ingrese la cantidad de renglones que se agregarán al archivo.txt: "))
    for i in range(cant_renglones) :
        #el usuario va ingresando los renglones
        renglon = input(f"Renglón {i+1}: ")
        #escribimos el renglón ingresado en el archivo.txt y luego un salto de líneas
        archivo.write(renglon)
        archivo.write("\n")

#el archivo se cierra automáticamente









