"""Area y perimetro de un triangulo
Descripcion: 
Realizar una aplicacion que permita mediante un menu
deopciones determinar el area o el perimetro de un triángulo."""




base = float(input("Ingrese el lado del triángulo: "))
altura = float(input("Ingrese la altura: "))
lado = float(input("Ingrese el lado del triángulo"))
area = (base*altura) /2
perimetro = lado*3
print(""" 
     *** MENÚ ***
     1. Determinar el Area un de triángulo
     2. Determinar el perímetro de un triángulo
     3. Salir
""")
opcion = int(input("Ingrese una opción: "))
match opcion:
    case 1:
        print(f"El área del triangulo es: {area}")
    case 2:
        print(f"El perímetro del triángulo es: {perimetro}")
    case 3:
        print("Saliendo...")
    case _:
        print("Opción no válida")