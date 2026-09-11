"""Ejercicio de Práctica: Sistema de Gestión e Inspección de Vuelos (Aeropuerto)
Un sistema aeroportuario necesita procesar una lista de vuelos programados para el día. No se sabe cuántos vuelos hay en total, así que el programa se detendrá cuando el usuario ingrese el número de vuelo 0.

Por cada vuelo se debe ingresar la siguiente información:

Número de vuelo: (Entero mayor a 0, o 0 para finalizar el programa).

Tipo de vuelo: 'N' (Nacional) o 'I' (Internacional).

Cantidad de pasajeros a bordo: (Entero positivo o cero).

Capacidad máxima del avión en pasajeros: (Debe ser estricta y lógicamente mayor o igual a la cantidad de pasajeros a bordo).

Minutos de retraso en la salida: (Entero mayor o igual a 0).

Reglas de Negocio y Cálculos por Vuelo
1. Cálculo de Penalización por Retraso
El aeropuerto cobra una multa por minuto de retraso según la categoría del vuelo y la cantidad de minutos:

Vuelo Nacional (N):

Si el retraso es de 1 a 30 minutos: $15.000 por minuto.

Si el retraso supera los 30 minutos: $25.000 por cada minuto excedente (los primeros 30 se pagan a $15.000).

Vuelo Internacional (I):

Tarifa única de $40.000 por minuto de retraso desde el minuto 1.

2. Tasa Aeroportuaria
Cada vuelo paga un costo operativo base:

Si la ocupación del avión es menor al 50% de su capacidad, se le aplica un sobrecargo del 12% sobre la multa de retraso (si no tuvo retraso, la multa es $0, por lo que el sobrecargo no aplica).

Si la ocupación es del 100% (vuelo lleno), el vuelo recibe un descuento del 10% sobre la multa total calculada.

Requerimientos de Salida por Registro
Por cada vuelo ingresado se debe imprimir:

Porcentaje de ocupación del avión.

Valor de la multa por retraso.

Ajuste aplicado (monto del sobrecargo o del descuento, si aplica).

Total a pagar por el vuelo.

Requerimientos del Informe Final (Al ingresar 0)
(Si no se procesó ningún vuelo, mostrar el mensaje "No se registraron datos").

Diferencia de Retraso Promedio: Calcular y mostrar la diferencia entre el promedio de minutos de retraso de los vuelos Nacionales versus los Internacionales. (¿Cuál categoría tuvo más retraso en promedio y por cuántos minutos?).

Vuelo en Caso Crítico: Identificar y mostrar el número del vuelo Internacional que tuvo la menor ocupación en pasajeros (en cantidad de personas, no en porcentaje). Si no hubo vuelos internacionales, indicarlo con un mensaje.

Evaluación de Puntualidad General:

Si más del 70% de todos los vuelos procesados despegaron sin retraso (0 minutos), mostrar: "Operación Eficiente".

Si está entre el 40% y el 70%, mostrar: "Operación Regular".

Si es menos del 40%, mostrar: "ALERTA: Colapso Operativo".

Validaciones Obligatorias
El Tipo de vuelo solo debe aceptar 'N', 'n', 'I' o 'i'.

Los pasajeros a bordo y los minutos de retraso no pueden ser negativos.

La capacidad máxima no solo debe ser positiva, sino que no puede ser menor a los pasajeros a bordo ya ingresados (ej: no puedes tener 150 pasajeros en un avión con capacidad de 100).

Si algún dato es erróneo, se debe mostrar un error específico y solicitarlo de nuevo.

¿Por qué este ejercicio rompe los patrones anteriores?
Validación relacional entre variables: La validación de la capacidad depende de lo que ingresaste en pasajeros.

Cálculo por tramos mixtos: El retraso nacional usa una tarifa por tramos (los primeros 30 a un precio, el resto a otro).

Mínimo condicionado: El punto 2 no pide el mínimo global; pide el mínimo solo de los vuelos internacionales.

Promedios comparativos: Debes llevar acumuladores y contadores independientes para dos categorías (N e I) para luego restar sus promedios.

Rangos en informe final: La evaluación final usa porcentajes cruzados con decisiones de 3 vías."""