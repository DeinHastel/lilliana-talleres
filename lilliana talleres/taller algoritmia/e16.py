def buscar_maximo(lista):
    maximo = lista[0]  

    for elemento in lista:
        if elemento > maximo:
            maximo = elemento  

    return maximo

lista = [5, 12, 8, 25, 10, 15]

maximo_valor = buscar_maximo(lista)

print("El valor máximo en la lista es:", maximo_valor)

