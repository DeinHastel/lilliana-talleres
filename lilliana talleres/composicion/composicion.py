class Motor:
    def __init__(self,tipo):
        self.tipo = tipo
    def arrancar(self):
        print(f"el motor es tipo {self.tipo}")

class Auto:
    def __init__(self,marca,modelo,motor):
        self.marca = marca
        self.modelo = modelo
        # creacion de un motor dentro de la clase auto
        self.motor = Motor(motor)
    def conducir(self):
        print(f"conduciendo el {self.marca} del {self.modelo}")
        self.motor.arrancar()
class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def conducir_auto(self,auto):
        print(f"{self.nombre} esta conduciendo {auto.marca}")
        auto.conducir()

auto = Auto("toyota","2021","hibrido")
persona = Persona("Ramces")

persona.conducir_auto(auto)