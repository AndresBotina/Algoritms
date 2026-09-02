cantidad_vehiculos = int(input("cuantos vehiculos va a registrar: "))

motos = 0
autos = 0
recaudado_motos = 0
recaudado_autos = 0
vehiculos_5_horas = 0
mayor_valor = 0

for i in range(cantidad_vehiculos):
    print("vehiculo", i + 1)
    placa = input("deme la placa: ")

    tipo = int(input("tipo (1 moto, 2 auto): "))
    while tipo != 1 and tipo != 2:
        print("tipo mal ingresado, solo 1 o 2")
        tipo = int(input("tipo (1 moto, 2 auto): "))

    horas = int(input("cuantas horas estuvo: "))
    while horas <= 0:
        print("horas invalidas, debe ser mayor a cero")
        horas = int(input("cuantas horas estuvo: "))

    total = 0

    if tipo == 1:
        if horas == 1:
            total = 2000
        else:
            total = 2000 + (horas - 1) * 1500
        motos = motos + 1
        recaudado_motos = recaudado_motos + total
    else:
        if horas == 1:
            total = 4000
        else:
            total = 4000 + (horas - 1) * 3000

        if horas >= 8 and total > 20000:
            total = 20000

        autos = autos + 1
        recaudado_autos = recaudado_autos + total

    if horas >= 5:
        vehiculos_5_horas = vehiculos_5_horas + 1

    if total > mayor_valor:
        mayor_valor = total

    print("placa:", placa)
    print("horas:", horas)
    print("total a pagar:", total)

total_general = recaudado_motos + recaudado_autos

if cantidad_vehiculos > 0:
    promedio = total_general / cantidad_vehiculos
else:
    promedio = 0

print("RESULTADOS DEL DIA")
print("total de vehiculos:", cantidad_vehiculos)
print("cuantas motos:", motos)
print("cuantos autos:", autos)
print("recaudado en motos:", recaudado_motos)
print("recaudado en autos:", recaudado_autos)
print("recaudado total:", total_general)
print("promedio por vehiculo:", promedio)
print("vehiculos con 5 horas o mas:", vehiculos_5_horas)
print("el pago mas alto:", mayor_valor)