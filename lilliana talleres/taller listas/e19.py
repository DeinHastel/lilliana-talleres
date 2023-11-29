personas = {
    "Juan": 25,
    "María": 30,
    "Pedro": 17,
    "Luisa": 12,
    "Ana": 18
}
mayores = [nombre for nombre, edad in personas.items() if edad >= 18]

print(mayores)