num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el ultimo numero: "))

if num1>num2 and num1>num3:
    print("El numero mayor es: ",num1)

elif num2>num1 and num2>num3:
    print("El numero mayor es: ",num2)
else:
    print("El numero mayor es: ",num3)

if num3>num2 and num3<num1 or num3<num2 and num3>num1:
    print(num3," es el numero de la mitad")
elif num1>num2 and num1<num3 or num1<num2 and num1>num3:
    print(num1," es el numero de la mitad")
elif num2>num1 and num2<num3 or num2<num1 and num2>num3:
    print(num2," es el numero de la mitad")