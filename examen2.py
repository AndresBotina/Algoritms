"""Una familia desea llevar un control digital del consumo diario de agua en su hogar. Para ello, se requiere desarrollar un
programa en Python que permita registrar los litros consumidos cada día y, al finalizar el registro, generar un resumen que
facilite analizar el comportamiento del consumo.
Requisitos del sistema: El programa deberá permitir registrar el consumo de agua de varios días. Para cada día se debe:
1. El programa comenzará solicitando el consumo correspondiente al día 1 y continuará con los días siguientes
mientras se registren consumos válidos.
2. Se considerará un consumo válido cualquier valor numérico mayor que 0.
3. Cuando se registre un consumo válido, este será procesado y el programa continuará con el siguiente día.
4. Si se ingresa 0 o un valor negativo, el dato se considerará inválido y deberá solicitarse nuevamente sin avanzar al
siguiente día.
5. El valor -1 será la única excepción a la regla anterior y se utilizará exclusivamente para indicar que se desea finalizar
el registro. Por lo tanto, -1 no representa un consumo, no debe incluirse en ningún cálculo y no debe contabilizarse
como un día registrado. Sino finaliza la ejecución de la aplicación.
6. Por cada consumo válido, el programa deberá clasificar el nivel de consumo de acuerdo con los siguientes rangos:
• Menor de 300 litros Bajo
• Entre 300 y 600 litros Moderado
• Mayor de 600 litros Alto
7. Después de cada registro, mostrar:
a. Número del día.
b. Litros consumidos.
c. Clasificación del consumo.
8. Resumen del consumo: Cuando el usuario ingrese -1, el programa deberá finalizar el registro y mostrar:
a. Total de litros consumidos durante el período.
b. Promedio diario de consumo.
c. Mayor y menor consumo registrado.
d. Cantidad de días con consumo bajo.
e. Cantidad de días con consumo moderado.
f. Cantidad de días con consumo alto.
9. Si el usuario ingresa -1 antes de registrar algún consumo, el programa deberá mostrar: "No se registraron consumos
de agua."
Conceptos que se deben evidenciar en la solución: Declaración y uso de variables y tipos de datos, Entradas y salidas
por teclado, Uso de condicionales y Uso de Ciclos. Adicionalmente uso de contadores y acumuladores."""

consumo_total = 0.0
contador_dias = 0
dias_bajo = 0
dias_moderado = 0
dias_alto = 0
mayor_consumo = 0.0
menor_consumo = 0.0

dia = 1

while True:
    try:
        consumo = float(input(f"Ingrese el consumo del día {dia} (litros): "))
    except ValueError:
        print("Valor inválido. Ingrese un valor numérico.")
        continue

    if consumo == -1:
        break

    if consumo <= 0:
        print("Consumo inválido. Debe ser mayor que 0.")
        continue

    if consumo < 300:
        clasificacion = "Bajo"
        dias_bajo += 1
    elif consumo <= 600:
        clasificacion = "Moderado"
        dias_moderado += 1
    else:
        clasificacion = "Alto"
        dias_alto += 1

    consumo_total += consumo
    contador_dias += 1

    if contador_dias == 1:
        mayor_consumo = consumo
        menor_consumo = consumo
    else:
        if consumo > mayor_consumo:
            mayor_consumo = consumo
        if consumo < menor_consumo:
            menor_consumo = consumo

    print(f"Día: {dia}")
    print(f"Litros consumidos: {consumo}")
    print(f"Clasificación del consumo: {clasificacion}")

    dia += 1

print()

if contador_dias == 0:
    print("No se registraron consumos de agua.")
else:
    promedio = consumo_total / contador_dias
    print("--- Resumen del consumo ---")
    print(f"Total de litros consumidos: {consumo_total}")
    print(f"Promedio diario de consumo: {round(promedio, 2)}")
    print(f"Mayor consumo registrado: {mayor_consumo}")
    print(f"Menor consumo registrado: {menor_consumo}")
    print(f"Días con consumo bajo: {dias_bajo}")
    print(f"Días con consumo moderado: {dias_moderado}")
    print(f"Días con consumo alto: {dias_alto}")
