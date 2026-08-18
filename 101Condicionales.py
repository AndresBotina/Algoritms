edad= int(input("Ingresa tu edad: "))

if edad <= 0 or edad > 150:
    print("Edad fuera de rango")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    