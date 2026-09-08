
num = int(input("ingrese un numero: "))

match num:
    case 1|2:
        print("opcion correcta")
    case 3:
        print("Opcion incorrecta")
    case  _:
        print("Opcion no válida")
