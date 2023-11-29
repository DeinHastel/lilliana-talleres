def suma_diagonal(matriz):
    if len(matriz) != 4 or len(matriz[0]) != 4:
        return None  

    suma = 0
    for i in range(4):
        suma += matriz[i][i]
    
    return suma

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

resultado = suma_diagonal(matriz)
print("La suma de la diagonal principal es:", resultado)