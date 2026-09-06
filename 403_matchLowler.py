#Un ejemplo utilizando cadenas de texto para simular un control de acceso según el rol de un usuario
rol = "admin"

match rol.lower():
    case "admin":
        print("Acceso total: Puedes crear, editar y eliminar usuarios.")
    case "editor":
        print("Acceso limitado: Puedes crear y editar contenido.")
    case "visitante" | "invitado":
        print("Acceso de solo lectura: Solo puedes ver el contenido.")
    case _:
        print("Rol no reconocido. Acceso denegado.")