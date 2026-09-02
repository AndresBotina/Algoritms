cantidad_viviendas = int(input("cuantas viviendas va a procesar: "))

total_m3 = 0
viviendas_altas = 0
total_facturado = 0
mayor_consumo = 0

for i in range(cantidad_viviendas):
    print("vivienda", i + 1)
    nombre = input("nombre del responsable: ")

    lectura_anterior = int(input("lectura anterior: "))
    lectura_actual = int(input("lectura actual: "))

    while lectura_actual < lectura_anterior:
        print("datos incorrectos, la lectura actual no puede ser menor a la anterior")
        lectura_anterior = int(input("lectura anterior: "))
        lectura_actual = int(input("lectura actual: "))

    consumo = lectura_actual - lectura_anterior

    if consumo <= 15:
        costo_consumo = consumo * 2000
    else:
        if consumo <= 30:
            costo_consumo = consumo * 2500
        else:
            costo_consumo = consumo * 3000

    total_factura = costo_consumo + 12000

    print("consumo:", consumo)
    print("total factura:", total_factura)

    if consumo > 40:
        print("Consumo elevado: se recomienda revisar el uso del agua.")
        viviendas_altas = viviendas_altas + 1

    total_m3 = total_m3 + consumo
    total_facturado = total_facturado + total_factura

    if consumo > mayor_consumo:
        mayor_consumo = consumo

if cantidad_viviendas > 0:
    promedio_consumo = total_m3 / cantidad_viviendas
else:
    promedio_consumo = 0

print("RESULTADOS FINAL")
print("total de viviendas:", cantidad_viviendas)
print("total m3 consumidos:", total_m3)
print("promedio de consumo:", promedio_consumo)
print("viviendas con mas de 40 m3:", viviendas_altas)
print("total dinero facturado:", total_facturado)
print("mayor consumo:", mayor_consumo)