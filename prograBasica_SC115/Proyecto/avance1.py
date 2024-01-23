# Complejo Futbolistico “Los Mejengueros”
print("\t======================================================")
print("\tBienvenido al Complejo Futbolistico “Los Mejengueros”")
print("\t======================================================\n")

# Menu Principal, se repite hasta que el usuario salga o ingrese una opcion valida.
print("\t======================================================")
print("\tMenu principal")
print("\t======================================================\n")
print("\t[1] Modulo de Clientes")
print("\t[2] Modulo de Administrador")
print("\t[3] Modulo de Reserva")
print("\t[4] Modulo de Informes")
print("\t[5] Salir")

ciclo_menu_principal = True
while ciclo_menu_principal == True:
    modulo = input("\tSeleccione un modulo [1,2,3,4,5]: ")
    if modulo == "1":
        modulo = "clientes"
        ciclo_menu_principal = False
    elif modulo == "2":
        modulo = "administrador"
        ciclo_menu_principal = False
    elif modulo == "3":
        modulo = "reservas"
        ciclo_menu_principal = False
    elif modulo == "4":
        modulo = "informes"
        ciclo_menu_principal = False
    elif modulo == "5":
        modulo = "salir"
        ciclo_menu_principal = False
    else:
        print("\tEl modulo ",modulo," no es valido. Intente de nuevo.\n")
    
    if modulo == "clientes" or modulo == "administrador" or modulo == "reservas" or modulo == "informes":
        print("\n\t======================================================")
        print("\tModulo:",modulo)
        print("\t======================================================\n")

# Modulo 1: Modulo de Clientes 
# Menu del modulo de clientes, se repite hasta que el usuario salga o se ingrese una opcion valida.
if modulo == "clientes":
    print("\t[1] Registrarse")
    print("\t[2] Actualizar un cliente existente")
    print("\t[3] Consultar un cliente")
    print("\t[4] Lista de reservas")
    print("\t[5] Salir")

    ciclo_menu_clientes = True
    while ciclo_menu_clientes == True:
        opcion_menu_cliente = input("\tSeleccione una opcion [1,2,3,4,5]: ")
        if opcion_menu_cliente == "1":
            opcion_menu_cliente = "registrarse"
            ciclo_menu_clientes = False
        elif opcion_menu_cliente == "2":
            opcion_menu_cliente = "actualizar"
            ciclo_menu_clientes = False
        elif opcion_menu_cliente == "3":
            opcion_menu_cliente = "consultar"
            ciclo_menu_clientes = False
        elif opcion_menu_cliente == "4":
            opcion_menu_cliente = "lista_reservas"
            ciclo_menu_clientes = False
        elif opcion_menu_cliente == "5":
            ciclo_menu_clientes = False
        else:
            print("\tLa opcion ",opcion_menu_cliente," no es valida. Intente de nuevo.\n")

# A) Registrar un nuevo cliente, solicitando la siguiente información:
# 1. Identificación.
# 2. Nombre
# 3. Primer Apellido
# 4. Segundo Apellido.
# 5. Teléfono
# 6. Correo
# 7. Activo o Inactivo (Por defecto Inactivo)
if modulo == "clientes" and opcion_menu_cliente == "registrarse":
    print("\n\tCREAR CUENTA\n")
    
    identificacion = input("\tIngrese el numero de identificacion: \n\t")
    nombre = input("\tIngrese el nombre: \n\t")
    primerApellido = input("\tIngrese el primer apellido: \n\t")
    segundoApellido = input("\tIngrese el segundo apellido: \n\t")
    telefono = input("\tIngrese el numero de telefono: \n\t")
    correo = input("\tIngrese el correo: \n\t")
    estado = "inactivo"

    # Se crea una lista con toda la información correspondiente al nuevo cliente.
    cliente_nuevo = [identificacion, nombre, primerApellido, segundoApellido, telefono, correo, estado]

    # POR HACER en futuros avances: crear un archivo .txt para el cliente usando como nombre su ID (ID.txt) para almacenar sus datos.

# B) Actualizar un cliente existente: Permitiendo modificar toda la información del cliente, únicamente dejando intacto la Identificación.
elif modulo == "clientes" and opcion_menu_cliente == "actualizar":
    print("\n\tACTUALIZAR DATOS DE UN CLIENTE\n")

    identificacion = input("\tIngrese el numero de identificacion: \n\t")
    nombre = input("\tIngrese el nombre: \n\t")
    primerApellido = input("\tIngrese el primer apellido: \n\t")
    segundoApellido = input("\tIngrese el segundo apellido: \n\t")
    telefono = input("\tIngrese el numero de telefono: \n\t")
    correo = input("\tIngrese el correo: \n\t")
    estado = "inactivo"

    # Se crea una lista con toda la información correspondiente al cliente actualizado.
    cliente_actualizado = [identificacion, nombre, primerApellido, segundoApellido, telefono, correo, estado]

    # POR HACER en futuros avances: sobrescribir el archivo .txt del cliente usando como nombre su ID (ID.txt) para almacenar sus datos.

# C) Consultar un cliente: Solicitando la identificación, desplegará la información básica del cliente.
elif modulo == "clientes" and opcion_menu_cliente == "consultar":
    print("\n\tCONSULTAR DATOS DEL CLIENTE\n")
    identifiacion = input("\tIngrese el numero de identificacion: ")

    # POR HACER en futuros avances: leer el archivo .txt del cliente usando como referencia su ID (ID.txt) y mostrar la informacion que contiene.
    
# D) Listado de reservas: mediante el cual el cliente podrá revisar las reservas que ha realizado en el complejo.
elif modulo == "clientes" and opcion_menu_cliente == "lista_reservas":
    print("\n\tLISTA DE RESERVAS\n")
    identificacion = input("\tIngrese el numero de identificacion para visualizar sus reservas: ")

    # POR HACER en futuros avance: cargar el archivo de reservas para este usuario (ID_reservas.txt) y mostrar sus contenidos.
    # Las reservas muestran la siguiente información: fecha, hora, cancha alquilada.