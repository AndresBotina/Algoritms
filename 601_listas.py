"""Ejercicio: Control de Velocidades

Un fotorradar registra velocidades (km/h) hasta que se ingresa 0.

Ingreso y Guardado
- Pide la velocidad de cada vehículo y guárdala en una única lista.

Reglas de Multa
- Hasta 60 km/h: $0
- 61 a 80 km/h: $150.000
- Más de 80 km/h: $300.000

Salida Final (Usando la Lista)
- Lista de infractores: Mostrar una nueva lista solo con las velocidades > 60.
- Total recaudado: Suma del dinero por multas.
- Velocidad máxima: El valor más alto registrado.

Validación
- La velocidad no puede ser negativa (< 0). Si es inválida, pedirla de nuevo.
"""

velocidades = []

while True:
    velocidad = int(input("Ingrese la velocidad del vehículo (0 para terminar): "))
    if velocidad == 0:
        break
    if velocidad < 0:
        print("La velocidad no puede ser negativa. Intente de nuevo.")
        continue
    velocidades.append(velocidad)

infractores = [v for v in velocidades if v > 60]

total_recaudado = 0
for v in velocidades:
    if v <= 60:
        total_recaudado += 0
    elif v <= 80:
        total_recaudado += 150000
    else:
        total_recaudado += 300000

velocidad_maxima = max(velocidades) if velocidades else 0

print("Lista de infractores:", infractores)
print(f"Total recaudado: ${total_recaudado}")
print(f"Velocidad máxima: {velocidad_maxima} km/h")