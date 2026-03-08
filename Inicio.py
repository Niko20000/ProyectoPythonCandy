
usuarios = []


def crear_cuenta():
    print("\ Crear cuenta ")
    usuario = input("Escribe un nombre de usuario: ")
    contraseña = input("Escribe una contraseña: ")

    cuenta = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    usuarios.append(cuenta)
    print("Tu cuenta se creó correctamente.\n")



def iniciar_sesion():
    print("\n Iniciar sesión ")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    for cuenta in usuarios:
        if cuenta["usuario"] == usuario and cuenta["contraseña"] == contraseña:
            print("Inicio de sesión exitoso. Bienvenido", usuario, "\n")
            return

    print("El usuario o la contraseña son incorrectos.\n")



def menu():
    while True:
        print(" opciones: ")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("vuelva pronto :)  ")
            break
        else:
            print("Opción no válida.\n")



menu()