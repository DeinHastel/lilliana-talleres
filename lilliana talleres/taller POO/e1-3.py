class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_info(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año})"


mi_auto = Vehiculo("Toyota", "Corolla", 2022)
print(mi_auto.obtener_info())

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas

    def obtener_info(self):
        info_vehiculo = super().obtener_info()
        return f"{info_vehiculo}, Puertas: {self.numero_puertas}"

mi_auto = Automovil("Toyota", "Corolla", 2022, 4)
print(mi_auto.obtener_info())

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def obtener_info(self):
        info_vehiculo = super().obtener_info()
        return f"{info_vehiculo}, Capacidad de Carga: {self.capacidad_carga} kg"

mi_camioneta = Camioneta("Ford", "Ranger", 2022, 1000)
print(mi_camioneta.obtener_info())