class Forma:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

una_forma = Forma(5, 8)
area = una_forma.calcular_area()
print(f"Área de la forma: {area}")

class Rectangulo(Forma):
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

mi_rectangulo = Rectangulo(5, 8)
area_rectangulo = mi_rectangulo.calcular_area()
perimetro_rectangulo = mi_rectangulo.calcular_perimetro()

print(f"Área del rectángulo: {area_rectangulo}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")

class Circulo(Forma):
    def calcular_circunferencia(self):
        radio = self.ancho / 2  
        return 2 * math.pi * radio

mi_circulo = Circulo(10, 0)  # El segundo parámetro (alto) no se usa en este caso
area_circulo = mi_circulo.calcular_area()
circunferencia_circulo = mi_circulo.calcular_circunferencia()

print(f"Área del círculo: {area_circulo}")
print(f"Circunferencia del círculo: {circunferencia_circulo}")