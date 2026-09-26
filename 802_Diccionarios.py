"""Ejercicio de Práctica: Gestión de Pedidos en una Cafetería
Una cafetería administra el menú disponible mediante un diccionario (donde la clave es el nombre del producto y el valor es su precio unitario) y la orden de un cliente mediante una lista con los productos seleccionados.

Datos Iniciales
Python
menu = {"Café": 3500, "Empanada": 2500, "Jugo": 4000, "Pastel": 3000}
pedido = ["Café", "Empanada", "Café", "Galleta", "Jugo"]
Requerimientos del Programa:
Actualizar el Menú (Métodos de Diccionarios):

Agregar un nuevo producto al menu llamado "Muffin" con un precio de 4500.

Actualizar el precio de la "Empanada" a 2800.

Obtener e imprimir una lista con todas las opciones/claves disponibles en el menu.

Gestión del Pedido (Métodos de Listas):

Agregar un "Pastel" al final de la lista pedido.

Eliminar la primera aparición del "Jugo" de la lista pedido.

Contar e imprimir cuántas veces solicitó "Café" el cliente en su pedido.

Cálculo de la Factura:

Recorrer la lista pedido para calcular el total a pagar.

Si un producto de la lista pedido no existe en el menu (como "Galleta"), se debe ignorar su cobro o asumir que cuesta $0 sin que el programa falle.

Imprimir la lista final de productos del pedido y el valor total a pagar."""

menu = {"Café": 3500, "Empanada": 2500, "Jugo": 4000, "Pastel": 3000}
pedido = ["Café", "Empanada", "Café", "Galleta", "Jugo"]

# 1. Actualizar el menú
menu["Muffin"] = 4500
menu["Empanada"] = 2800
opciones = list(menu.keys())
print("Opciones disponibles en el menú:", opciones)

# 2. Gestión del pedido
pedido.append("Pastel")
pedido.remove("Jugo")
cantidad_cafe = pedido.count("Café")
print(f"El cliente pidió 'Café' {cantidad_cafe} veces.")

# 3. Cálculo de la factura
total = 0
for producto in pedido:
    total += menu.get(producto, 0)

print("\n--- Pedido final ---")
print(pedido)
print(f"Total a pagar: ${total}")