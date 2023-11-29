def contar_palabras_en_linea(linea):
    contador_a = linea.lower().count('a')
    contador_an = linea.lower().count('an')
    contador_and = linea.lower().count('and')
    return contador_a, contador_an, contador_and

def contar_palabras_en_texto(texto):
    lineas = texto.split('\n')
    total_a = 0
    total_an = 0
    total_and = 0

    for linea in lineas:
        contador_a, contador_an, contador_and = contar_palabras_en_linea(linea)
        total_a += contador_a
        total_an += contador_an
        total_and += contador_and

    return total_a, total_an, total_and

# Ejemplo de texto
texto = """
We are going to make the text for Professor
Lilian and we are going to count
how many a, an, and there are in the text
"""

# Contar las palabras en el texto
ocurrencias_a, ocurrencias_an, ocurrencias_and = contar_palabras_en_texto(texto)

print("Número de ocurrencias de 'a':", ocurrencias_a)
print("Número de ocurrencias de 'an':", ocurrencias_an)
print("Número de ocurrencias de 'and':", ocurrencias_and)
