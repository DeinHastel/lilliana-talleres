def fecha(dia, mes, año):
    dia_str = str(dia)
    mes_str = str(mes)
    año_str = str(año)

    if dia < 10:
        dia_str = '0' + dia_str
    if mes < 10:
        mes_str = '0' + mes_str

    año_str = año_str[-2:]

    fecha_formateada = f"fecha: {dia_str}/{mes_str}/{año_str}"

    print(fecha_formateada)

dia = 19  
mes = 9
año = 1987

fecha(dia, mes, año)