import os
#para escribir con la w
archivo = open("carpeta/texto.txt","w")
archivo.write("nuevo texto")

#para leer con r
archivo = open("carpeta/texto.txt","r")
print(archivo.read())
archivo.close()