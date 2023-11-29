class Estudiante:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre
    def agregar_estudiante(self,estudiante):
        self.estudiantes= [] 
        self.estudiantes.append(estudiante)
    
    def enlistar_estudiantes(self):
        return f"estudiantes {self.estudiantes}"
#objetos estudiantes
estudiante1 = Estudiante("jason",29)
estudiante2 = Estudiante("carla",29)
estudiante3 = Estudiante("carlaasd",29)
mi_universidad = Universidad("sena")

mi_universidad.agregar_estudiante(estudiante1)
mi_universidad.agregar_estudiante(estudiante2)
mi_universidad.agregar_estudiante(estudiante3)

for estudiantesU in mi_universidad.estudiantes:
    print(f"{estudiantesU.nombre} edad : {estudiantesU.edad}")
