Euro = 0.86
PesosCO = 3117.11
Yenes = 153.89

while True:

    print("""
    CASA DE CAMBIO SENA
    Opcion 1: Dólares a Euros
    Opción 2: Dólares a Pesos COl
    Opción 3: Dólares a Yenes
    Opción 4: Salir.
    """)

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            dolares = float(input("Ingrese la cantidad de dólares: "))
            cambio  = dolares * Euro
            print(f"{dolares} dólares son {cambio} Euros")
        case 2:
            dolares = float(input("Ingrese la cantidad de dolares: "))
            cambio = dolares*PesosCO
            print(f"{dolares} dólares son {cambio} pesos colombianos")
        case 3:
            dolares = float(input("Ingrese la cantidad de dolares: "))
            cambio = dolares*Yenes
            print(f"{dolares} son {cambio} yenes")
        case 4:
            print("Hasta pronto mardito!")
            break

        case _:
            print("Dato inválido")

