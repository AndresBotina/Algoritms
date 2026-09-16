""": El Sistema de Cobro para Parqueaderos InteligentesContexto:Vas a diseñar la lógica de la consola para un parqueadero automatizado. El sistema debe recibir los datos de entrada de los conductores, calcular el total a pagar y procesar el cobro. Al ser una máquina sin supervisión humana, el programa debe ser indestructible: no puede cerrarse ni crashear por ningún error de tipeo del usuario.Requerimientos del Programa:Entrada de Datos: El programa debe pedir dos datos obligatorios:La cantidad de horas que se quedó el vehículo (el costo es de $5.000 COP por hora).El monto de dinero en efectivo con el que va a pagar el usuario.Cálculo del Cambio: El sistema debe calcular el costo total, restar el dinero ingresado y mostrar en pantalla cuánto dinero devolver de cambio.🛑 El Reto del try-except (Manejo de Excepciones)Tu misión es blindar el código capturando específicamente los siguientes escenarios de error:Nivel Básico (ValueError): Si el usuario mete letras, símbolos o deja en blanco los campos de texto cuando el sistema pide números (por ejemplo, escribir "dos" en lugar de 2), el programa no debe romperse. Debe avisar del error y volver a pedir los datos de forma infinita hasta que se ingresen números válidos.Nivel Intermedio (Exception personalizada): Si el usuario ingresa un número negativo (ejemplo: -3 horas), el programa debe lanzar una excepción manual que diga que el tiempo o el dinero no pueden ser negativos.Nivel Avanzado (Lógica de negocio): Si el dinero ingresado por el usuario es menor al costo total del parqueadero, el programa debe lanzar un error indicando cuánto dinero le hace falta para poder salir y denegar el pago."""

COSTO_POR_HORA = 5000


class NumeroNegativoError(Exception):
    pass


while True:
    try:
        horas = int(input("Ingrese la cantidad de horas: "))
        if horas < 0:
            raise NumeroNegativoError("El tiempo no puede ser negativo.")
    except ValueError:
        print("Error: debe ingresar un número válido de horas.")
        continue
    except NumeroNegativoError as e:
        print(e)
        continue

    try:
        dinero = int(input("Ingrese el dinero en efectivo: "))
        if dinero < 0:
            raise NumeroNegativoError("El dinero no puede ser negativo.")
    except ValueError:
        print("Error: debe ingresar un número válido de dinero.")
        continue
    except NumeroNegativoError as e:
        print(e)
        continue

    total = horas * COSTO_POR_HORA

    if dinero < total:
        falta = total - dinero
        print(f"Error: le hace falta ${falta} para poder salir.")
        continue

    cambio = dinero - total
    print(f"Costo total: ${total}")
    print(f"Su cambio es: ${cambio}")
    break
