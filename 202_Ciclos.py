#Cantidad de la fila
#A partir de la cantidad de usuarios en la fila
#calcular el IMC de cada usuario y mostrar el IMC en pantalla
#Informar si el usuario tiene bajo peso, peso normal, o sobrepeso.
longitud_fila = int(input("Ingresa la cantidad de personas en la fila: "))
if longitud_fila<=0:
    print("Ingrese un numero positivo")
else:
    for i in range(1,longitud_fila+1):
        print(f"Persona {i}")
        peso = int(input("Ingrese el peso de la persona en kg: "))
        altura = float(input("Ingrese la altura en metros: "))
        imc = peso/altura**2
        print("El imc de la persona",i, "es: ", imc)
