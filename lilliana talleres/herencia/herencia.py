class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print("estoy comiendo")
        
    def dormir(self):
        print("dormir we")
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    def ladrar(self):
        print(f"{self.nombre} esta haciendo woooof")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre,edad)
        self.color = color
    def ronronear(self):
        print("esta haciendo meeow")

perro1 = Perro("firulais",3,"yorkie")
perro1.ladrar()
perro2 = Perro("perseo",4,"pastor aleman")
perro2.comer()

gato1 = Gato("charlie",2,"persa")
gato1.ronronear()


