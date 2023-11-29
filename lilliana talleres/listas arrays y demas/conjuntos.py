conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

resultaado = conjunto1.union(conjunto2)
print(f"union : {resultaado}")

resultaado2 = conjunto1.intersection(conjunto2)
print(f"interseccion : {resultaado2}")

resultaado3 = conjunto1.difference(conjunto2)
print(f"diferencia : {resultaado3}")

resultaado4 = conjunto1.symmetric_difference(conjunto2)
print(f"symetric diference: {resultaado4}")
