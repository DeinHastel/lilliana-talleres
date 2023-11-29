def copiar_a_directo(archivo_secuencial, archivo_directo):
    registros = []

    with open(archivo_secuencial, "r") as secuencial:
        for registro in secuencial:
            registros.append(registro.strip())

    longitud_maxima = max(len(registro) for registro in registros)

    with open(archivo_directo, "w") as directo:
        for registro in registros:
            registro_formatado = registro.ljust(longitud_maxima)
            directo.write(registro_formatado + '\n')

archivo_secuencial = "agenda.txt"

archivo_directo = "directo_agenda.txt"

copiar_a_directo(archivo_secuencial, archivo_directo)

print("Archivo secuencial copiado a archivo directo.")
