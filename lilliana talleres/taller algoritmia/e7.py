#este codigo si fue la mayor parte de internet, ni idea de como hacer esas funciones
import math

def conversion_coordenadas(r, theta):
    # Convierte el ángulo de grados a radianes
    theta_radianes = math.radians(theta)

    # Calcula las coordenadas cartesianas
    x = r * math.cos(theta_radianes)
    y = r * math.sin(theta_radianes)

    return x, y

# Ejemplo de uso:
radio = 5  
angulo = 30

x, y = conversion_coordenadas(radio, angulo)

print(f"Coordenadas polares ({radio}, {angulo}°) se convierten en coordenadas cartesianas ({x}, {y})")