"""Calificaciones Académicas
Descripción: Un docente necesita registrar N calificaciones,
calcular su promedio y determinar si un estudiante aprueba o reprueba.
Si el promedioes 3.0 o superior, el estudiante aprueba; si es menor, reprueba.
Restriciones: 
- Solicitar al usuario la cantidad de calificaciones a ingresar.
- Valida que cada calificaciones este entre 0.0 y 5.0 
- Usar try-except para envitar errores en la entrada de datos
- Calcular el promedio y mostrar si aprueba o reprueba
- Las calificaciones deben ser almacenadas en una lista"""

try:
    cantidad = int(input("¿Cuántas calificaciones va a registrar?: "))
except ValueError:
    print("Error: debe ingresar un número entero.")
else:
    calificaciones = []

    for i in range(cantidad):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {i + 1}: "))
            except ValueError:
                print("Error: debe ingresar un valor numérico.")
            else:
                if nota < 0.0 or nota > 5.0:
                    print("Error: la calificación debe estar entre 0.0 y 5.0")
                else:
                    calificaciones.append(nota)
                    break

    print("Calificaciones registradas:", calificaciones)

    if len(calificaciones) > 0:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio es: {promedio}")

        if promedio >= 3.0:
            print("El estudiante aprueba")
        else:
            print("El estudiante reprueba")
    else:
        print("No se registraron calificaciones")
