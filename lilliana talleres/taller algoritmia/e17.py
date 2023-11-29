def calificacion_media(calificaciones):
    if len(calificaciones) == 0:
        return None  # Si no hay calificaciones, devolvemos None
    suma = sum(calificaciones)
    media = suma / len(calificaciones)
    return media

def diferencia_media(calificaciones, media):
    diferencias = []
    for calificacion in calificaciones:
        diferencia = calificacion - media
        diferencias.append(diferencia)
    return diferencias

def imprimir_calificaciones_y_diferencias(estudiantes, calificaciones, diferencias):
    for i in range(len(estudiantes)):
        print(f"Estudiante: {estudiantes[i]}, Calificación: {calificaciones[i]}, Diferencia con la Media: {diferencias[i]}")

# Ejemplo de estudiantes y calificaciones
estudiantes = ["Estudiante A", "Estudiante B", "Estudiante C", "Estudiante D"]
calificaciones = [85, 90, 78, 92]

# Calcular la calificación media
media = calificacion_media(calificaciones)

if media is not None:
    print("Calificación Media:", media)

    # Calcular las diferencias con la media
    diferencias = diferencia_media(calificaciones, media)

    # Imprimir las calificaciones y diferencias
    imprimir_calificaciones_y_diferencias(estudiantes, calificaciones, diferencias)
else: 
    print("No hay calificaciones para calcular la media.")
