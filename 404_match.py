nota = "A"

match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bueno")
    case "C":
        print("Suficiente")
    case "F":
        print("Reprobado")
    case _:
        print("Nota no válida")