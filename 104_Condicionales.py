num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el ultimo numero: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    medio = num1
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    medio = num2
else:
    medio = num3

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)
print("El numero de la mitad es:", medio)

