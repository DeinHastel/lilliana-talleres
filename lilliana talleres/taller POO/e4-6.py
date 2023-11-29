class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_ruido(self):
        return "hago ruido"

mi_animal = Animal("perico", 3)
print(f"Nombre: {mi_animal.nombre}")
print(f"Edad: {mi_animal.edad} años")
print(mi_animal.hacer_ruido())

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_ruido(self):
        return "¡Guau, guau!"

mi_perro = Perro("Fido", 2, "Labrador")
print(f"Nombre: {mi_perro.nombre}")
print(f"Edad: {mi_perro.edad} años")
print(f"Raza: {mi_perro.raza}")
print(mi_perro.hacer_ruido())

class Gato(Animal):
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje = pelaje

    def hacer_ruido(self):
        return "¡Miau, miau!"

mi_gato = Gato("Whiskers", 1, "Negro")
print(f"Nombre: {mi_gato.nombre}")
print(f"Edad: {mi_gato.edad} años")
print(f"Pelaje: {mi_gato.pelaje}")
print(mi_gato.hacer_ruido())