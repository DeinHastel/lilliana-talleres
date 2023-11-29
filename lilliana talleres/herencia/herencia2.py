class Persona:
    """
paramettesr:
Persona(nombre:str, edad:int, genero:str)\n
example:
Persona("erick",18,"masculino")
"""
    def __init__(self,nombre, edad, genero):
        self.nombre = nombre #atributo publico
        self.edad = edad #atributo protegido
        self.genero = genero #atributo privado
    def trabajar(self):#publico
        return f"{self.nombre} esta trabajando"
    def _dormir(self):#protegido
        return f"{self.nombre} se duerme"
    def __estudiar(self): #privado
        return f"{self.nombre} estudia"

persona1 = Persona("juan",34,"masculino")
trabajo = persona1.trabajar()
dormir = persona1._dormir()
estudio = persona1._Persona__estudiar()

print(trabajo)
print(dormir)
print(estudio)
