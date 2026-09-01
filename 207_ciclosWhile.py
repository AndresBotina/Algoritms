"""Control de producción de una fábrica
Realizar una aplicacion que permita registrar la cantidad
de unidades producidas durante 7 dias.
El programa debe solicitar por teclado la cantidad producida en cada dia y al finalizar debe mostrar:
-La produccion total de la semana
-El promedio diario de produccion
-Cuantos dias tuvieron una produccion mayor a 100 unidades.

"""
promedio = 0
c = 0
produccion_total = 0
for i in range(7):
    cantidad_producida = int(input(f"Ingrese la cantidad del dia {i+1}: "))
    produccion_total += cantidad_producida
    if cantidad_producida >=101:
        c+=1
promedio = produccion_total/7
print(f"El promedio vendido por dia es: {promedio}")
print("La producción total de la semana es: ",produccion_total)
print(f"El numero de dias que tuvieron una produccion mayor a 100 fue: {c}")