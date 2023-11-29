class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

    def calcular_salario_neto(self, impuestos, otros_descuentos):
        salario_neto = self.sueldo - impuestos - otros_descuentos
        return salario_neto

un_empleado = Empleado("Juan", "Pérez", 50000)
impuestos = 1000
otros_descuentos = 2000

salario_neto_empleado = un_empleado.calcular_salario_neto(impuestos, otros_descuentos)

print(f"Nombre: {un_empleado.nombre} {un_empleado.apellido}")
print(f"Sueldo bruto: {un_empleado.sueldo}")
print(f"Impuestos: {impuestos}")
print(f"Otros descuentos: {otros_descuentos}")
print(f"Salario neto: {salario_neto_empleado}")

class Gerente(Empleado):
    def __init__(self, nombre, apellido, sueldo, departamento):
        super().__init__(nombre, apellido, sueldo)
        self.departamento = departamento

    def calcular_salario_neto(self, impuestos, otros_descuentos, bono_gerente):
        salario_neto_gerente = super().calcular_salario_neto(impuestos, otros_descuentos)
        salario_neto_gerente += bono_gerente
        return salario_neto_gerente

un_gerente = Gerente("Ana", "Gómez", 70000, "Finanzas")
impuestos_gerente = 1500
otros_descuentos_gerente = 3000
bono_gerente = 5000

salario_neto_gerente = un_gerente.calcular_salario_neto(impuestos_gerente, otros_descuentos_gerente, bono_gerente)

print(f"Nombre: {un_gerente.nombre} {un_gerente.apellido}")
print(f"Sueldo bruto: {un_gerente.sueldo}")
print(f"Impuestos: {impuestos_gerente}")
print(f"Otros descuentos: {otros_descuentos_gerente}")
print(f"Bono de gerente: {bono_gerente}")
print(f"Salario neto: {salario_neto_gerente}")

class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje

    def calcular_salario_neto(self, impuestos, otros_descuentos, bono_experto):
        salario_neto_programador = super().calcular_salario_neto(impuestos, otros_descuentos)
        salario_neto_programador += bono_experto
        return salario_neto_programador

un_programador = Programador("Carlos", "González", 60000, "Python")
impuestos_programador = 1200
otros_descuentos_programador = 2500
bono_experto = 3000

salario_neto_programador = un_programador.calcular_salario_neto(impuestos_programador, otros_descuentos_programador, bono_experto)

print(f"Nombre: {un_programador.nombre} {un_programador.apellido}")
print(f"Sueldo bruto: {un_programador.sueldo}")
print(f"Impuestos: {impuestos_programador}")
print(f"Otros descuentos: {otros_descuentos_programador}")
print(f"Bono de experto en {un_programador.lenguaje}: {bono_experto}")
print(f"Salario neto: {salario_neto_programador}")