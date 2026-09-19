"""Ejercicio: Gestión de Inventario de Tienda
Tienes una lista con el inventario actual de un producto (precios de artículos en stock). Debes actualizar la lista aplicando métodos nativos de listas.

Lista Inicial
precios = [1200, 4500, 3000, 800, 4500]

Tareas a Realizar (Usando Métodos de Listas):
Contar: Contar cuántas veces se repite el precio 4500 en la lista.

Insertar: Insertar un nuevo precio de 2500 en la segunda posición (índice 1).

Eliminar el último: Extraer (eliminar) el último elemento de la lista y guardarlo en una variable.

Invertir: Invertir el orden completo de los elementos en la lista."""

precios = [1200, 4500, 3000, 800, 4500]

repeticiones = precios.count(4500)

precios.insert(1, 2500)

ultimo = precios.pop()

precios.reverse()

print("Veces que se repite 4500:", repeticiones)
print("Último elemento eliminado:", ultimo)
print("Lista final:", precios)