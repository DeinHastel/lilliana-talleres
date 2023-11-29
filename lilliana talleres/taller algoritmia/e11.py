def division_entera_y_resto(dividendo, divisor):
    cociente = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        cociente += 1

    return cociente, resto

# Ejemplo de uso:
dividendo = 23  # Cambia estos valores por el dividendo y divisor deseados
divisor = 4

cociente, resto = division_entera_y_resto(dividendo, divisor)
print(f"División entera de {dividendo} entre {divisor}: Cociente = {cociente}, Resto = {resto}")