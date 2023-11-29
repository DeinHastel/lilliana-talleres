class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


persona = Persona("Juan", "Pérez", 30)
print(f"Nombre completo: {persona.obtener_nombre_completo()}")
print(f"Edad: {persona.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()} ({self.carrera})"

un_estudiante = Estudiante("Ana", "Gómez", 22, "Ingeniería Informática")
print(f"Nombre completo y carrera: {un_estudiante.obtener_nombre_completo()}")
print(f"Edad: {un_estudiante.edad} años")

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia = materia

    def obtener_nombre_completo(self):
        return f"{super().obtener_nombre_completo()} - Materia: {self.materia}"

un_profesor = Profesor("Dr. Rodríguez", "Martínez", 40, "Matemáticas")
print(f"Nombre completo y materia: {un_profesor.obtener_nombre_completo()}")
print(f"Edad: {un_profesor.edad} años")