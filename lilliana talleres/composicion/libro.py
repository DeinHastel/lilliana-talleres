class Autor:
    def __init__(self,nombre,nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros=[] # aca se relaciona
    def agregar_libro(self,titulo, anio):
        libro = Libro(titulo,anio)
        self.libros.append(libro)
    def __str__(self):
        return f"autor : {self.nombre} nacionalidad : {self.nacionalidad}"
class Libro:
    def __init__(self,titulo,anio):
        self.titulo = titulo
        self.anio = anio
#__str__(set)
    def __str__(self):
        return f" el libro es {self.titulo} del año {self.anio}"

autor1 = Autor("k.k","britanico")
autor1.agregar_libro("harry popotter",1900)
autor1.agregar_libro("piedra filososfal",1910)

print(autor1)
for libro in autor1.libros:
    print(f"libro {libro}")