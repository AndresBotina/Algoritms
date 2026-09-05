opcion = 2
saldo = 1000

match opcion:
    case 1:
        print(f"Tu saldo actual es: ${saldo}")
    case 2:
        monto = 200
        saldo += monto
        print(f"Has depositado ${monto}. Nuevo saldo: ${saldo}")
    case 3:
        monto = 150
        saldo -= monto
        print(f"Has retirado ${monto}. Nuevo saldo: ${saldo}")
    case 4:
        print("Gracias por usar el cajero. ¡Hasta luego!")
    case _:
        print("Opción no válida. Selecciona un número del 1 al 4.")