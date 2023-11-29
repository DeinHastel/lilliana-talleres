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

class Auditor(Persona):
    def __init__(self,nombre,edad,genero,departamento):
        super().__init__(nombre,edad,genero)
        self.departamento = departamento
    def auditar(self):
        return f"{self.nombre} audita {self.departamento} "
class Gerente(Persona):
    def __init__(self, nombre, edad, genero, equipo):
        super().__init__(nombre, edad, genero)
        self.equipo = equipo
    def dirigir_equipo(self):
        return f"{self.nombre} dirige a {self.equipo}"
    
persona1 = Persona("erick",18,"masculino")
auditor1 = Auditor("carlos",29,"masculino","fianzas")
gerente1 = Gerente("juana",18,"femenina",["mario","jenny"])

print(auditor1.trabajar())
print(gerente1.dirigir_equipo())
print(auditor1._dormir())
print(auditor1._Persona__estudiar())

