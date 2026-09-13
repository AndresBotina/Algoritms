"""Area y perimetro de un triangulo
Descripcion: 
Realizar una aplicacion que permita mediante un menu
deopciones determinar el area o el perimetro de un triángulo."""

while True:
    print("""
    *** MENÚ ***
    1. Determinar el área de un triángulo
    2. Determinar el perímetro de un triángulo
    3. Salir
    """)

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: debe ingresar un número.")
        continue

    if opcion == 1:
        try:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area}")
        except ValueError:
            print("Error: debe ingresar valores numéricos.")
    elif opcion == 2:
        try:
            lado = float(input("Ingrese el lado del triángulo: "))
            perimetro = lado * 3
            print(f"El perímetro del triángulo es: {perimetro}")
        except ValueError:
            print("Error: debe ingresar un valor numérico.")
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("Opción no válida")
