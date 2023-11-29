#Diseñar la función FACTORIAL que calcule la factorial de un número entero
#entre el rango 100 a 1.000.000.

def factorial(x):
    sum = 0
    if x >= 100 and x <= 1000000:
        for i in range(x,2,-1):
            fact = x * (i-1)
            x = fact + sum
        return x
    else:
        error = "valor ingresado incorrecto"
        return error
    print(x)

y = int(input("digite un numero entero del entre 100 y 1000000 para un factorial \n"))
fact = factorial(y)
print(fact)