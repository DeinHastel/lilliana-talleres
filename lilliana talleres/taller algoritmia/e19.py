def arabigo_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""

    i = 0
    while numero > 0:
        while numero >= valores[i]:
            resultado += romanos[i]
            numero -= valores[i]
        i += 1

    return resultado

def romano_a_arabigo(romano):
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    prev_valor = 0

    for letra in romano:
        valor = valores_romanos.get(letra, 0)
        if valor > prev_valor:
            resultado += valor - 2 * prev_valor  
        else:
            resultado += valor
        prev_valor = valor

    return resultado

numero_arabigo = 1987
numero_romano = "MMCMXCIV"

romano_generado = arabigo_a_romano(numero_arabigo)
print(f"{numero_arabigo} en números romanos es {romano_generado}")

arabigo_generado = romano_a_arabigo(numero_romano)
print(f"{numero_romano} en números arábigos es {arabigo_generado}")
