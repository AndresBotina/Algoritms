dia_trabajado = 0
cantidad_horas_trabajadas= 0
dia = 0
hora = 8000
while True:
    cantidad_horas_trabajadas = int(input("Ingresa la cantidad de horas del empleado: "))
    if cantidad_horas_trabajadas <0:
        break
    if cantidad_horas_trabajadas >=8:
        dia+=1

