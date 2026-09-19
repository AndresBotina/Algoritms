"""Ejercicio: Procesamiento de Registro de Estudiantes
Un profesor tiene una lista inicial de calificaciones y necesita actualizarla aplicando métodos nativos de listas.

Lista Inicial
notas = [3.5, 2.0, 4.8, 1.5, 4.0]

Tareas a Realizar (Usando Métodos de Listas):
Agregar: Agregar la nota 5.0 al final de la lista.

Eliminar: Remover la nota más baja de la lista (1.5).

Ordenar: Ordenar la lista de mayor a menor.

Buscar: Mostrar en qué posición (índice) quedó la nota 4.0."""

notas = [3.5, 2.0, 4.8, 1.5, 4.0]

notas.append(5.0)

notas.remove(min(notas))

notas.sort(reverse=True)

indice = notas.index(4.0)

print("Lista final:", notas)
print("Posición de la nota 4.0:", indice)
