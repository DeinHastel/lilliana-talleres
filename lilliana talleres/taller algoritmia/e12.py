def es_fecha_valida(dia, mes, año):
    # lista de dias de los meses
    dias_maximos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_maximos[1] = 29

    # verificar si el mes esta bien y sus dias son correctos
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_maximos[mes - 1]:
        return False

    return True


try:
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    año = int(input("Ingresa el año: "))
    
    if es_fecha_valida(dia, mes, año):
        print("La fecha ingresada es válida.")
    else:
        print("La fecha ingresada no es válida.")
except ValueError:
    print("Error: Ingresa números enteros para el día, mes y año.")
