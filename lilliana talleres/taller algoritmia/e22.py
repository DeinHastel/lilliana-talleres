def agregar_contacto(archivo):
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    codigo_postal = input("Código Postal: ")
    telefono = input("Teléfono: ")
    edad = input("Edad: ")

    registro = f"{nombre}, {direccion}, {ciudad}, {codigo_postal}, {telefono}, {edad}\n"

    with open(archivo, "a") as agenda:
        agenda.write(registro)

def listar_contactos(archivo):
    with open(archivo, "r") as agenda:
        contactos = agenda.readlines()
        for i, contacto in enumerate(contactos, start=1):
            print(f"Contacto {i}: {contacto.strip()}")

# Nombre del archivo de la Agenda de Direcciones
archivo_agenda = "agenda.txt"

while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_contacto(archivo_agenda)
        print("Contacto agregado exitosamente.")
    elif opcion == "2":
        listar_contactos(archivo_agenda)
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
