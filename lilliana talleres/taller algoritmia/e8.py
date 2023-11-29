def salario(horas_trabajadas, tarifa_hora):
    if horas_trabajadas <= 40:
        salario = horas_trabajadas * tarifa_hora
    else:
        horas_normales = 40
        horas_extras = horas_trabajadas - 40
        salario = (horas_normales * tarifa_hora) + (horas_extras * 1.5 * tarifa_hora)
    
    return salario

# lo menciono una ultima vez, paso de poner inputs para optimizar tests de codigo, ya que es simple hacerlo:
horas_trabajadas = 45 
tarifa_hora = 10

salario_total = salario(horas_trabajadas, tarifa_hora)
print(f"El salario total es: ${salario_total}")