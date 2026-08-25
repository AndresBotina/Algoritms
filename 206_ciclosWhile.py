#Cuente 10 iteraciones que ingresa el usuario
#Y solo sume los valores positivos que encuentre
suma = 0
c = 0
while c <10:
    num = int(input("Ingresa 10 numeros: "))
    c+=1
    if num > 0:
        suma+=num
print(f"La suma es: {suma}")