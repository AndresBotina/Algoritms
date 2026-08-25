# Lista de compras con precios
precios = [120, 45, 80, 200, 15, 60]

# Aplica 15% de descuento solo a productos mayores a $50
precios_finales = [precio * 0.85 if precio > 50 else precio for precio in precios]

print(precios_finales)
# Resultado: [102.0, 45, 68.0, 170.0, 15, 51.0]