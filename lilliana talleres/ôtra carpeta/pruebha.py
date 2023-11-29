import os
#obtener la ruta absoluta del archivo
ruta = os.path.abspath("carpeta/pruba2.txt")
#abriendolo, la r ni idea para que sirve
txt = open(ruta,"r")
#leer
contenido = txt.read()
#cerrar archvio
txt.close()
#imprimiendo
print(contenido)