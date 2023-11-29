def es_digito(caracter):
    if caracter.isdigit():
        if int(caracter) >= 0 and int(caracter)<=9:
            return caracter.isdigit()
        else:
            caracter = False
            return caracter
    else:
        caracter = False
        return caracter
        

caracter = '10'  

if es_digito(caracter):
    print(f"'{caracter}' es un dígito valido.")
else:
    print(f"'{caracter}' no es un dígito o no es valido.")
