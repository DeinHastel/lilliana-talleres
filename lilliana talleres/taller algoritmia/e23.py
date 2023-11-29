def imprimir_agenda(archivo):
    try:
        with open(archivo, "r") as agenda:
            contactos = agenda.readlines()
            if contactos:
                print("Registros en la Agenda:")
                for i, contacto in enumerate(contactos, start=1):
                    print(f"Contacto {i}: {contacto.strip()}")
            else:
                print("La Agenda está vacía.")
    except FileNotFoundError:
        print("El archivo de Agenda no existe.")

archivo_agenda = "agenda.txt"

imprimir_agenda(archivo_agenda)
