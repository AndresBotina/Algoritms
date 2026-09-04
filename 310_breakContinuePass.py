# Se requiere una aplicacion para validar la contraseña y permitir el acceso al sistema
# El usuario tiene 3 intentos, sino se bloquea el acceso
# Si la pass es incorrecta se le pide que la ingrese nuevamente
# Si es correcta se otorga el acceso y se finaliza el programa

password = "123abc"
max_intentos = 3

for intento in range(1, max_intentos + 1):
    clave = input(f"Ingresa la contraseña, intento {intento}/{max_intentos}: ")

    if clave == password:
        print("!Success!")
        break

    if intento < max_intentos:
        print(f"Te quedan {max_intentos - intento} intentos")
    else:
        print("Acceso Bloqueado")