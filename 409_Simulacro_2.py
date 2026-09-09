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

total_agua_consumida = 0
agua_mtrs_cubicos = 0
nro_apartacho = 0
estrato = 0
descuento = 0
con_descuento = 0
nro_apartamentos = int(input("¿Cuantos apartamentos serán procesados? "))
for i in range(1,nro_apartamentos +1):
    nro_apartacho = int(input("Ingrese el numero del apartamento: "))
    print("")
    print("""
        Hasta 10 m3 $2.000
        De 11 a 20 m3 $2.500
        Más de 20 m3 $3.200
        """)
    agua_mtrs_cubicos = float(input("Agua en metros cubicos consuimdos durante el mes: "))

   

    print("""
        • Los estratos 1 y 2 reciben un descuento del 15%.
        • El estrato 3 recibe un descuento del 5%.
        • Los estratos 4, 5 y 6 no reciben descuento.
        """)
    estrato = int(input("Ingresa tu estrato: "))
    print("")

    match estrato:
        case 1|2:
            print("Estrato 1")
            descuento = agua_mtrs_cubicos*0.15
            if agua_mtrs_cubicos >= 1 and agua_mtrs_cubicos <=10:
                total_agua_consumida = agua_mtrs_cubicos * 2000
            
            elif agua_mtrs_cubicos <= 20:
                total_agua_consumida = agua_mtrs_cubicos*2500
            elif total_agua_consumida >= 21:
                total_agua_consumida =agua_mtrs_cubicos*3200
        case 3:
            print("Este estrato recibe descuento del 5%")
            descuento = agua_mtrs_cubicos*0.05
            if agua_mtrs_cubicos >= 1 and agua_mtrs_cubicos <=10:
                total_agua_consumida = agua_mtrs_cubicos * 2000
            
            elif agua_mtrs_cubicos <= 20:
                total_agua_consumida = agua_mtrs_cubicos*2500
            elif total_agua_consumida >= 21:
                total_agua_consumida =agua_mtrs_cubicos*3200
        case 4|5|6:
            print("Estos estratos NO reciben descuento")
            if agua_mtrs_cubicos >= 1 and agua_mtrs_cubicos <=10:
                total_agua_consumida = agua_mtrs_cubicos * 2000
            
            elif agua_mtrs_cubicos <= 20:
                total_agua_consumida = agua_mtrs_cubicos*2500
            elif total_agua_consumida >= 21:
                total_agua_consumida =agua_mtrs_cubicos*3200
        case _:
            print("Ingresaste un numero o dato invalido")
    con_descuento = total_agua_consumida - descuento
    print("")
    print(f"---------- DATOS DEL APARTAMENTO N° [{nro_apartacho}] -----------")
    print("")
    print(f"Total del agua consumida de [{nro_apartacho}] es {total_agua_consumida}")
    print(f"El total del agua consumida con descuento es de: [{con_descuento}]")




