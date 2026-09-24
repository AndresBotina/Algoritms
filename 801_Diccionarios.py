"""Ejercicio: Sistema de Inventario y Facturación
Contexto
Tienes una lista de diccionarios que representa el inventario de un supermercado. Cada diccionario contiene el nombre del producto, su precio unitario y la cantidad disponible en stock.

Además, tienes una lista de diccionarios que representa el carrito de compras de un cliente.

Datos iniciales
Python
# Inventario de la tienda (Lista de diccionarios)
inventario = [
    {"nombre": "Manzana", "precio": 1.2, "stock": 10},
    {"nombre": "Leche", "precio": 2.5, "stock": 5},
    {"nombre": "Pan", "precio": 1.0, "stock": 8},
    {"nombre": "Huevos", "precio": 0.2, "stock": 30}
]

# Carrito del cliente (Lista de diccionarios)
carrito = [
    {"nombre": "Manzana", "cantidad": 3},
    {"nombre": "Leche", "cantidad": 2},
    {"nombre": "Pan", "cantidad": 10}  # Nota que piden más de lo que hay en stock
]
Tu objetivo
Escribe un programa en Python que realice las siguientes acciones:

Procesar la compra:

Recorre los elementos del carrito.

Para cada producto del carrito, busca si existe en el inventario.

Verifica si hay suficiente stock:

Si hay suficiente stock: Resta la cantidad comprada del inventario y calcula el subtotal de ese producto (cantidad × precio).

Si NO hay suficiente stock: Imprime un mensaje indicando que no se pudo procesar esa compra por falta de existencias (y no modifiques el inventario).

Imprimir el ticket de compra:

Muestra en pantalla el detalle de los productos efectivamente comprados y el total final a pagar.

Mostrar el inventario actualizado:

Muestra la lista del inventario final para confirmar que el stock bajó correctamente."""

inventario = [
    {"nombre": "Manzana", "precio": 1.2, "stock": 10},
    {"nombre": "Leche", "precio": 2.5, "stock": 5},
    {"nombre": "Pan", "precio": 1.0, "stock": 8},
    {"nombre": "Huevos", "precio": 0.2, "stock": 30}
]

carrito = [
    {"nombre": "Manzana", "cantidad": 3},
    {"nombre": "Leche", "cantidad": 2},
    {"nombre": "Pan", "cantidad": 10}
]

ticket = []
total = 0.0

for producto in carrito:
    nombre = producto["nombre"]
    cantidad = producto["cantidad"]

    encontrado = None
    for item in inventario:
        if item["nombre"] == nombre:
            encontrado = item
            break

    if encontrado is None:
        print(f"No se pudo procesar {nombre}: producto no encontrado en el inventario.")
        continue

    if cantidad > encontrado["stock"]:
        print(f"No se pudo procesar {nombre}: falta de existencias.")
        continue

    encontrado["stock"] -= cantidad
    subtotal = cantidad * encontrado["precio"]
    total += subtotal
    ticket.append({"nombre": nombre, "cantidad": cantidad, "subtotal": subtotal})

print("\n--- Ticket de compra ---")
for linea in ticket:
    print(f"{linea['nombre']} x{linea['cantidad']} = ${linea['subtotal']:.2f}")
print(f"Total a pagar: ${total:.2f}")

print("\n--- Inventario actualizado ---")
for item in inventario:
    print(f"{item['nombre']}: stock {item['stock']}")

