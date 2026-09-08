cantidadVentas = int(input("Ingrese la  cantidad de ventas que desea registrar: "))
subtotal = 0
precio = 0
producto = ""
totalVenta = 0
descuento= 0
for i in range(1, cantidadVentas+1):
    numeroVenta = str(input("Ingrese el numero de la venta: "))
    print("""
        ------- -PRODUCTOS- -------
        1: Café - $4000 c/u
        2: Sandwich - $8500 c/u
        3: Jugo - $5000 c/u
    """)
    tipoProducto = int(input("Ingrese el tipo de producto: "))
    cantidadUnidadesCompradas = int(input(f"Ingrese la cantidad de unidades compradas para '{numeroVenta}':  "))

    match tipoProducto:
        case 1:
            producto = "Café"
            precio = 4000
            valorVenta = cantidadUnidadesCompradas*precio
            if cantidadUnidadesCompradas >= 5 and cantidadUnidadesCompradas <=9:
                descuento = valorVenta*0.05
            elif cantidadUnidadesCompradas >=10:
                descuento = valorVenta*0.10
            else:
                pass
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
        case _:

            print("Dato inválido, seleccione uno de la lista")
    totalVenta = valorVenta - descuento
    print(f"Prdocuto: {producto}")
    print(f"Subtotal: {valorVenta}")
    print(f"Descuento: {descuento}")
    print(f"Total: {totalVenta}")
