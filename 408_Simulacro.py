cantidadVentas = int(input("Ingrese la  cantidad de ventas que desea registrar: "))
subtotal = 0
precio = 0
producto = ""
totalVenta = 0
descuento= 0
objetivo =0
productoMayor1 = 0
productoMayor2 = 0
productoMayor3 = 0
for i in range(1, cantidadVentas+1):
    numeroVenta = str(input("Ingrese el numero o codigo de la venta: "))
    
    print("""
        ------- -PRODUCTOS- -------
        1: Café - $4000 c/u
        2: Sandwich - $8500 c/u
        3: Jugo - $5000 c/u
        ---------------------------
    """)

    tipoProducto = int(input("Ingrese el tipo de producto: "))
    cantidadUnidadesCompradas = int(input(f"Ingrese la cantidad de unidades compradas para [{numeroVenta}]: "))

    match tipoProducto:
        case 1:
            producto = "Cafe"
            precio = 4000
            valorVenta = cantidadUnidadesCompradas*precio
            if cantidadUnidadesCompradas >= 5 and cantidadUnidadesCompradas <=9:
                descuento = valorVenta*0.05
            elif cantidadUnidadesCompradas >=10:
                descuento = valorVenta*0.10
            else:
                pass

            productoMayor1 += cantidadUnidadesCompradas

        case 2:
            producto = "Sandwich"
            precio =8500
            valorVenta = cantidadUnidadesCompradas*precio
            if cantidadUnidadesCompradas >= 5 and cantidadUnidadesCompradas <=9:
                descuento = valorVenta*0.05
            elif cantidadUnidadesCompradas >=10:
                descuento = valorVenta*0.10
            else:
                pass

            productoMayor2 += cantidadUnidadesCompradas
    
 
        case 3:
            producto = "Jugo"
            precio = 5000
            valorVenta = cantidadUnidadesCompradas*precio
            if cantidadUnidadesCompradas >= 5 and cantidadUnidadesCompradas <=9:
                descuento = valorVenta*0.05
            elif cantidadUnidadesCompradas >=10:
                descuento = valorVenta*0.10
            else:
                pass

            productoMayor3 += cantidadUnidadesCompradas
    
        case _:

            print("Dato inválido, seleccione uno de la lista")
            continue



# --------------------------CALCULOS INDIVISUALES--------------------------------#

    totalVenta = valorVenta - descuento
    print(f"Producto: {producto}")
    print(f"Subtotal: {valorVenta}")
    print(f"Descuento: {descuento}")
    print(f"Total a pagar: {totalVenta}")
    print("")
    print("-----------------------------------------------------------")
    print("")

    objetivo+=totalVenta
    

# --------------------------PRODUCTOS MAS VENDIDOS POR CATEGORIA--------------------------------#

print(f"Total de unidades vendidas para Jugo: {productoMayor3}.")
print(f"Total de unidades vendidas para Cafe: {productoMayor1}.")
print(f"Total de unidades vendidas para Sandwich: {productoMayor2}")

print("")
print("-----------------------------------------------------------")
print("")


if (productoMayor1 == productoMayor2 and productoMayor2==productoMayor3) or productoMayor1 == productoMayor2 or productoMayor2==productoMayor3 or productoMayor1 == productoMayor3 :
    print ("Hubo empate de ventas entre productos vendidos")
elif productoMayor1>productoMayor2 and productoMayor1>productoMayor3:
    print(f"El producto mas vendido fue el Cafe con {productoMayor1} Unidades.")
elif productoMayor2>productoMayor1 and productoMayor2>productoMayor3:
    print(f"El producto mas vendido fue el Sandwich con {productoMayor2} Unidades.")
elif productoMayor3>productoMayor1 and productoMayor3>productoMayor2:
    print(f"El producto mas vendido fue el Jugo con {productoMayor3} Unidades.")
# --------------------------OBJETIVO DIARIO--------------------------------#

print("")
print("-----------------------------------------------------------  ")
print("")


if  objetivo > 500000:
    print(f"El objetivo de 500.000 en ventas diarias se cumplio. Total: {objetivo}")
else:
    dineroFaltante =objetivo - 500000
    print(f"No se logro el objetivo de 500.000 en ventas, falto {dineroFaltante}")