calificacion = int(input("Ingresa tu nota: "))

while calificacion != 0:
    if calificacion<0:
        print("Calificacion inválida")
    elif calificacion <70:
        print("Necesitas mejorar")
    elif calificacion <=79:
        print("Bien")
    elif calificacion <=89:
        print("Muy bien")
    else:
        print("Ecxelente")
    calificacion = int(input("Ingresa tu nota: "))


