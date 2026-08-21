
tabla = int(input("Ingrese el número de la tabla: "))

while tabla< 0:
    print("Elige un numero positivo o mayor a cero")
    tabla = int(input("Ingrese el número de la tabla: "))


for i in range(1, 11):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")
        






