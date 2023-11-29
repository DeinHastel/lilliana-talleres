import os

nombre = input("nombre del archvio")
with open(nombre,"w") as archivo:
    while True:
        texto = input("digite cosas para el archivo (o escriba 'para finalizar')")
        if texto.lower() == "salir":  break
        archivo.write(texto+"\n")