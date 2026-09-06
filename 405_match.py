numeros = [1, 2, 3, 4]

for num in numeros:
    match num % 2:
        case 0:
            print(f"El {num} es PAR")
        case 1:
            print(f"El {num} es IMPAR")