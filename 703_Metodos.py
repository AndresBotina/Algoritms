"""Ejercicio: Control de Turnos de Atención en Banco
Tienes una lista con los turnos de atención pendientes en una sucursal bancaria. Debes procesarla aplicando métodos nativos de listas.

Lista Inicial
turnos = ["A-10", "A-11", "A-12", "A-13"]

Tareas a Realizar (Usando Métodos de Listas):
Atender (Extraer): Atender al primer cliente de la fila eliminando y guardando el elemento "A-10" (índice 0).

Prioridad (Insertar al inicio): Insertar a un cliente VIP "VIP-1" al inicio de la lista (índice 0).

Limpiar turno específico: Un cliente se retiró de la fila; elimina directamente el turno "A-12".

Fusionar turnos: Fusionar al final de la lista una segunda lista con turnos prioritarios: ["B-01", "B-02"]."""

turnos = ["A-10", "A-11", "A-12", "A-13"]

atendido = turnos.pop(0)

turnos.insert(0, "VIP-1")

turnos.remove("A-12")

turnos.extend(["B-01", "B-02"])

print("Turno atendido:", atendido)
print("Lista final de turnos:", turnos)
