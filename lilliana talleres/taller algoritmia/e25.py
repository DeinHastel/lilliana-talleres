def modificar_registro(archivo_secuencial, indice_registro, nuevo_registro):
    try:
        with open(archivo_secuencial, "r") as secuencial:
            registros = secuencial.readlines()
        
        if 0 <= indice_registro < len(registros):
            registros[indice_registro] = nuevo_registro + '\n'

            with open(archivo_secuencial, "w") as secuencial:
                secuencial.writelines(registros)
                print("Registro modificado con éxito.")
        else:
            print("Índice de registro fuera de rango.")
    except FileNotFoundError:
        print("El archivo de Agenda no existe.")

archivo_secuencial = "agenda.txt"

# Mostrar registros existentes
with open(archivo_secuencial, "r") as secuencial:
    registros = secuencial.readlines()
    for i, registro in enumerate(registros):
        print(f"Contacto {i}: {registro.strip()}")

indice = int(input("Ingrese el índice del registro que desea modificar: "))

if 0 <= indice < len(registros):
    nuevo_registro = input("Ingrese el nuevo contenido del registro: ")
    modificar_registro(archivo_secuencial, indice, nuevo_registro)
else:
    print("Índice de registro fuera de rango.")
