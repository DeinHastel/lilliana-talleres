"""factorial es de 5*4*3*2*1
"""

def factorial(n, tot = 0):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
resultado = factorial(5)
print(f"resultado factorial: {resultado}")