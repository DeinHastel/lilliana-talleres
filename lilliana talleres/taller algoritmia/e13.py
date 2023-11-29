def contar_elementos_positivos(lista):
    positivos = []
    for elemento in lista:
        if elemento > 0:
            positivos.append(elemento)
    return positivos

# Ejemplo de uso:
mi_lista = [3, -2, 5, 0, -1, 7, -4]

nums_positivos = contar_elementos_positivos(mi_lista)
print(f"El número de elementos positivos en la lista es: {nums_positivos}")
