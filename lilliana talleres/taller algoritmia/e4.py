def num_mayor(n1,n2):
    
    if n1 < n2:
        return f"el numero mayor es {n2}"
    elif n1 > n2:
        return f"el numero mayor es {n1}"
    else:
        return f"los dos numeros son iguales"
    
    
n1 = int(input("digite el primer numero "))
n2 = int(input("digite el segundo numero "))

n = num_mayor(n1,n2)

print(n)