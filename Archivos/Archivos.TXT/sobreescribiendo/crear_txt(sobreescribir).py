#Forma ÓPTIMA de trabajar con archivos .TXT

#en este caso lo abriremos para escritura de datos, por ende ponemos la "w" de write
with open("Archivos\\Archivos.TXT\\sobreescribiendo\\archivo_creado(sobreescribiendo).txt","w", encoding="UTF-8") as archivo :
    #pedimos al usuario la cantidad de renglones para saber cuando se terminará el ingreso de datos
    cant_renglones = int(input("Ingrese la cantidad de renglones que tendrá el archivo.txt creado: "))
    for i in range(cant_renglones) :
        #el usuario va ingresando los renglones
        renglon = input(f"Renglón {i+1}: ")
        #escribimos el renglón ingresado en el archivo.txt y luego un salto de líneas
        archivo.write(renglon)
        archivo.write("\n")

#el archivo se cierra automáticamente



