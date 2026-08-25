# Variables simples de texto y booleanos
usuario = "Carlos"
sesion_activa = True

# Condicional de una sola línea según el estado de la sesión
saludo = f"¡Bienvenido de nuevo, {usuario}!" if sesion_activa else "Por favor, inicia sesión."

# Imprime el resultado directo
print(saludo)