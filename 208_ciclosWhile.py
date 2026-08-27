password = "passdev123"
user = "numdev"
userr= str(input("Ingrese el usuario: "))
contraseña= str(input("Ingrese la contraseña "))
while userr != user and contraseña != password:
    userr= str(input("Ingrese el usuario: "))
    contraseña= str(input("Ingrese la contraseña "))
print("Bienvenido!")