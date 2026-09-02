#Se requiere una aplcacion para validar la contraseña y permitir el acceso al sistema
# El usuario tiene 3 intentos, sino se bloquea el acceso
# Si la pass es incorrecta se le pide que la ingrese nuevamente
#Si es correcta se otorga el acceso y se finaliza el programa

password = "123abc"
c = 0
clave = str(input("Ingresa la contraseña, solo tienes 3 intentos: "))
if clave == password:
    print("!Success!")
else:
    while clave != password:
        c+=1
        if password != clave and c <=2:
            print (f"Te quedan {3-c} intentos")
            clave = str(input("Contraseña incorrecta, ingresala nuevamente: "))
        elif password != clave and c >=3:
            print("Acceso Bloqueado")
            break
        elif password == clave:
            print("!Success!")
        else:
            pass