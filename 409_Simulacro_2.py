'''
Ejercicio - 02. Control de consumo de agua en apartamentos

Una unidad residencial necesita analizar el consumo mensual de agua de sus apartamentos para
determinar el valor que debe pagar cada uno. Al iniciar, el programa debe solicitar la cantidad de
apartamentos que serán procesados.
Por cada registro se debe ingresar:
• Número del apartamento.
• Cantidad de metros cúbicos de agua consumidos durante el mes.
• Estrato: 1, 2, 3, 4, 5 o 6.
Consumo Valor por m3
Hasta 10 m3 $2.000
De 11 a 20 m3 $2.500
Más de 20 m3 $3.200
El servicio tiene un cargo fijo de $18.000. Para determinar el valor del consumo se debe utilizar la
tarifa correspondiente al rango en el que se encuentre el consumo total del apartamento.
• Los estratos 1 y 2 reciben un descuento del 15%.
• El estrato 3 recibe un descuento del 5%.
• Los estratos 4, 5 y 6 no reciben descuento.
• Para cada apartamento se debe mostrar su número, consumo, valor antes del descuento,
descuento y total a pagar.
Al finalizar, el programa debe:
• Clasificar el consumo general según el promedio obtenido: menor de 10 m3, Consumo bajo;
entre 10 y 20 m3, Consumo moderado; mayor de 20 m3, Consumo alto.
• Mostrar cuántos apartamentos tuvieron un consumo superior al promedio de todos los
apartamentos.

Determinar si existió por lo menos un apartamento que consumiera más de 40 m3. En caso
afirmativo, mostrar una alerta por consumo excesivo.
• Indicar el número del apartamento que registró el menor consumo de agua.
Validaciones: el consumo no puede ser negativo y el estrato solamente puede estar entre 1 y 6. Si
se encuentra un dato inválido, se debe informar el error y solicitar nuevamente los datos
correspondientes.
'''

nro_apartamentos = int(input("¿Cuántos apartamentos serán procesados? "))

consumos = []
nro_apartamento_menor = 0
menor_consumo = None
hay_exceso = False

for i in range(1, nro_apartamentos + 1):
    nro_apartamento = int(input("Ingrese el número del apartamento: "))

    print("""
        Hasta 10 m3 $2.000
        De 11 a 20 m3 $2.500
        Más de 20 m3 $3.200
        """)

    agua = float(input("Agua en metros cúbicos consumidos durante el mes: "))
    while agua < 0:
        print("Error: el consumo no puede ser negativo.")
        agua = float(input("Agua en metros cúbicos consumidos durante el mes: "))

    estrato = int(input("Ingrese el estrato (1 a 6): "))
    while estrato < 1 or estrato > 6:
        print("Error: el estrato debe estar entre 1 y 6.")
        estrato = int(input("Ingrese el estrato (1 a 6): "))

    if agua <= 10:
        valor_consumo = agua * 2000
    elif agua <= 20:
        valor_consumo = agua * 2500
    else:
        valor_consumo = agua * 3200

    cargo_fijo = 18000
    valor_antes_descuento = valor_consumo + cargo_fijo

    match estrato:
        case 1 | 2:
            descuento = valor_antes_descuento * 0.15
        case 3:
            descuento = valor_antes_descuento * 0.05
        case _:
            descuento = 0

    total_pagar = valor_antes_descuento - descuento

    print(f"\n---------- DATOS DEL APARTAMENTO N° [{nro_apartamento}] ----------")
    print(f"Consumo: {agua} m3")
    print(f"Valor antes del descuento: {valor_antes_descuento}")
    print(f"Descuento: {descuento}")
    print(f"Total a pagar: {total_pagar}")

    consumos.append(agua)

    if menor_consumo is None or agua < menor_consumo:
        menor_consumo = agua
        nro_apartamento_menor = nro_apartamento

    if agua > 40:
        hay_exceso = True

promedio = sum(consumos) / len(consumos)
print(f"\nPromedio de consumo: {promedio} m3")

if promedio < 10:
    print("Consumo general: Consumo bajo")
elif promedio <= 20:
    print("Consumo general: Consumo moderado")
else:
    print("Consumo general: Consumo alto")

superior = 0
for c in consumos:
    if c > promedio:
        superior += 1
print(f"Apartamentos con consumo superior al promedio: {superior}")

if hay_exceso:
    print("ALERTA: existe consumo excesivo (más de 40 m3).")

print(f"El apartamento con menor consumo es el N° {nro_apartamento_menor} con {menor_consumo} m3.")
