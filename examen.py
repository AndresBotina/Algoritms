
turno = 0
nombre_pasciente = ""
turno_medicina = 0
turno_laboratorio = 0
turno_odontologia = 0
servicio_mayor = 0
while True:
    turno +=1
    nombre_pasciente = str(input("\nIngrese su nombre porfavor: "))
    while nombre_pasciente == ""or nombre_pasciente == " " or nombre_pasciente== "  " or nombre_pasciente== "   ":

        if nombre_pasciente == "" or nombre_pasciente== " " or nombre_pasciente== "  " or nombre_pasciente== "   ":
            print("El nombre no puede estar vacío, intenta nuevamente: ")
        else:
            continue
        nombre_pasciente = str(input("\nIngrese su nombre porfavor: "))
        
            
    if nombre_pasciente =="FIN":
        print("\nSaliendo..")
        print("___________________________________________________________________")
        break

    print("""
        --Motivos de consulta--

        Opción:
        1: Medicina General
        2: Examenes de laboratorio
        3: Odontología
        4: Salir
        """)
    print ("---------------------------------------------------------------------------")
    try:
        motivo_de_consulta = int(input("Elije una opción (Numero): "))

        match motivo_de_consulta:
            case 1:
                turno_medicina+=1
                medicina = "Medicina General"
                motivo_de_consulta = medicina
            case 2:
                turno_laboratorio +=1
                laboratorio = "Examenes de laboratorio"
                motivo_de_consulta = laboratorio
            case 3:
                turno_odontologia+=1
                odontologia = "Odontología"
                motivo_de_consulta = odontologia
            case 4:
                print("\nSaliendo..")
                print("______________________________________________________________")
                break
            case _:
                print("\nOpción Inválida")
                continue

        print("\n--DATOS DEL PACIENTE--")
        print(f"Turno: {turno}")    
        print(f"Nombre del pasciente: {nombre_pasciente}")
        print(f"Motivo de consulta: {motivo_de_consulta}")
    except ValueError:
        print ("\nOpcion inválida")
        

if turno_medicina> turno_laboratorio and turno_medicina >turno_odontologia:
    servicio_mayor = "Medicina General"
elif turno_laboratorio> turno_medicina and turno_laboratorio> turno_odontologia:
    servicio_mayor = "Exámenes de Laboratorio"
else:
    servicio_mayor = "Odontología"


print(f"Total de turnos registrados: {turno-1}")
print(f"Cantidad de turnos Medicina General: {turno_medicina}")
print(f"Cantidad de turnos Examenes de Laboratorio: {turno_laboratorio}")
print(f"Cantidad de turnos Odontología: {turno_odontologia}")
print(f" \nServicio con mas turnos: {servicio_mayor}")

if turno_odontologia == turno_laboratorio or turno_laboratorio == turno_medicina:
    print("\nExiste un empate entre turnos")
