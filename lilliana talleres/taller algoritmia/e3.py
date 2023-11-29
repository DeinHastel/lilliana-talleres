def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros(a, b, c, d):
    resultado = mcd(a, b)
    
    resultado = mcd(resultado, c)
    
    resultado = mcd(resultado, d)
    
    return resultado

n1 = 12
n2 = 18
n3 = 24
n4 = 36

resultado_mcd = mcd_cuatro_numeros(n1, n2, n3, n4)
print(f"El MCD de {n1}, {n2}, {n3} y {n4} es {resultado_mcd}")