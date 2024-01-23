"""
NOTAS GENERALES PARA FUTUROS AVANCES: 
- Se planea implementar metodos de lectura/escritura de archivos.
- Se planea crear como minimo 3 archivos tipo JSON:
    - usuarios.json: maneja todos los usuarios creados en el sistema.
    - reservas_solicitadas.json: maneja todas las nuevas reservas que deben ser revisadas y aprobadas.
    - reservas_aprobadas.json: maneja todas las reservas que han sido aprobadas y facturadas.
"""

# ---------------------- INICIO DE LAS FUNCIONES DEFINIDAS PARA EL PROGRAMA ----------------------

# Funcion que muestra el menu principal del programa, muestra los principales modulos y la opcion de salir.
def menu_principal():
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
            print("\tSaliendo del programa, ¡Adios!")
        else:
            print("\tEl modulo ",modulo," no es valido. Intente de nuevo.\n")

    # Cuando el usuario ingresa una opcion valida, se muestra en la terminal la opcion elegida.   
    if modulo == "clientes" or modulo == "administrador" or modulo == "reservas" or modulo == "informes":
        print("\n\t======================================================")
        print("\tModulo:",modulo)
        print("\t======================================================\n")
    
    # Cuando el usuario ingresa una opcion valida, se llama la funcion que maneja el menu de cada opcion.
    if modulo == "clientes":
        menu_clientes()
    elif modulo == "administrador":
        menu_administrador()
    elif modulo == "reservas":
        print("Por definir para el proximo avance.")
    elif modulo == "informes":
        print("Por definir para el avance final.")

# Funcion que despliega el menu del modulo de clientes, incluye las opciones dentro de este modulo y la opcion de salir.
def menu_clientes():
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
            print("\tSaliendo del modulo de clientes...")
            menu_principal()  # Al cerrar este menu, vuelve al menu principal.
        else:
            print("\tLa opcion ",opcion_menu_cliente," no es valida. Intente de nuevo.\n")

    if opcion_menu_cliente == "registrarse":
        registrar_usuario()
    elif opcion_menu_cliente == "actualizar":
        actualizar_usuario()
    elif opcion_menu_cliente == "consultar":
        consultar_usuario()
    elif opcion_menu_cliente == "lista_reservas":
        enlistar_reservas()

"""
Funcion que realiza el proceso de registrar un nuevo usuario.
Solicita la siguiente informacion:
1. Identificación.
2. Nombre
3. Primer Apellido
4. Segundo Apellido.
5. Teléfono
6. Correo
7. Activo o Inactivo (Por defecto Inactivo)
"""
def registrar_usuario():
    print("\n\tCREAR CUENTA\n")

    identificacion = input("\tIngrese el numero de identificacion: \n\t")
    nombre = input("\tIngrese el nombre: \n\t")
    primerApellido = input("\tIngrese el primer apellido: \n\t")
    segundoApellido = input("\tIngrese el segundo apellido: \n\t")
    telefono = input("\tIngrese el numero de telefono: \n\t")
    correo = input("\tIngrese el correo: \n\t")
    estado = "inactivo"

    # Se crea una lista con toda la información correspondiente al nuevo cliente. Esto podría representarse como un diccionario en futuros avances para crear un archivo JSON.
    cliente_nuevo = [identificacion, nombre, primerApellido, segundoApellido, telefono, correo, estado]

    """ 
    POR HACER en futuros avances: 
    - Crear un archivo "usuarios.json" para almacenar los clientes usando como etiqueta unica de cada usuario su ID.
    - Cada vez que se registre un nuevo usuario, se crea una entrada nueva en el archivo "usuarios.json" con los datos recopilados en "cliente_nuevo".
    - Se debe acceder primero al archivo "usuarios.json" y confirmar que el usuario que se desea registrar no exista previamente.
    """

# Funcion que se encarga de actualizar un cliente existente, permitiendo modificar toda la información del cliente y únicamente dejando intacto el estado.
def actualizar_usuario():
    print("\n\tACTUALIZAR DATOS DE UN CLIENTE\n")

    identificacion_actual = input("\tIngrese el numero de identificacion actual del usuario: \n\t")
    identificacion = input("\tIngrese el nuevo numero de identificacion del usuario: \n\t")
    nombre = input("\tIngrese el nombre: \n\t")
    primerApellido = input("\tIngrese el primer apellido: \n\t")
    segundoApellido = input("\tIngrese el segundo apellido: \n\t")
    telefono = input("\tIngrese el numero de telefono: \n\t")
    correo = input("\tIngrese el correo: \n\t")

    # Se crea una lista con toda la información correspondiente al cliente actualizado. Esto podría representarse como un diccionario en futuros avances para crear un archivo JSON.
    cliente_actualizado = [identificacion, nombre, primerApellido, segundoApellido, telefono, correo]

    """
    POR HACER en futuros avances:    
    - Cargar el archivo "usuarios.json".
    - Sobrescribir los atributos correspondientes a la "identificacion_actual" brindada dentro del archivo "usuarios.json", utilizando la nueva informacion brindada en "cliente_actualizado".
    - Es importante recalcar que el estado no se modifica con este metodo.
    - Notificar si no existe el usuario especificado.
    """

# Funcion que se encarga de mostrar toda la informacion de un cliente a partir de su identificacion.
def consultar_usuario():
    print("\n\tCONSULTAR DATOS DEL CLIENTE\n")

    identificacion = input("\tIngrese el numero de identificacion: ")

    """
    POR HACER en futuros avances:
    - Leer el archivo .json de los clientes.
    - Extraer los datos del usuario, usando como referencia su ID.
    - Mostrar la informacion que corresponde.
    - Notificar si no existe el usuario especificado.
    """
    
# Funcion que maneja el listado de reservas: muestra.
def enlistar_reservas():
    print("\n\tLISTA DE RESERVAS\n")

    identificacion = input("\tIngrese el numero de identificacion del usuario: ")

    """
    POR HACER en futuros avances:
    - Cargar el archivo de reservas llamado "reservas_aprobadas.json".
    - Buscar dentro del archivo "reservas_aprobadas.json" los datos historicos de reservas para un usuario dado mediante el uso de la identificacion.
    - Mostrar los datos de las reservas realizadas por el usuario: fecha, hora y cancha alquilada.
    - Notificar si no existen reservas para un usuario dado.
    """
   
# Funcion que despliega el menu del modulo de administrador, incluye las opciones dentro de este modulo y la opcion de salir.
def menu_administrador():
    print("\t[1] Activar un cliente")
    print("\t[2] Revisar reservas")
    print("\t[3] Salir")

    ciclo_menu_admin = True
    while ciclo_menu_admin == True:
        opcion_menu_admin = input("\tSeleccione una opcion [1,2,3]: ")
        if opcion_menu_admin == "1":
            opcion_menu_admin = "activar"
            ciclo_menu_admin = False
        elif opcion_menu_admin == "2":
            opcion_menu_admin = "revisar"
            ciclo_menu_admin = False
        elif opcion_menu_admin == "3":
            ciclo_menu_admin = False
            print("\tSaliendo del modulo de administrador...")
            menu_principal()  # Al cerrar este menu, vuelve al menu principal.
        else:
            print("\tLa opcion ",opcion_menu_admin," no es valida. Intente de nuevo.\n")
            
    if opcion_menu_admin == "activar":
        activar_usuario()
    elif opcion_menu_admin == "revisar":
        revisar_reservas()

# Funcion que se encarga de activar un usuario determinado. Solo se modifica el atributo "estado".
def activar_usuario():
    print("\n\tACTIVAR USUARIOS\n")

    identificacion = input("\tIngrese el numero de identificacion del usuario que desea activar: ")

    """
    POR HACER en futuros avances:
    - Cargar el archivo de usuarios llamado "usuarios.json".
    - Buscar dentro del archivo "usuarios.json" los datos del usuario dado mediante el uso de la identificacion.
    - Modificar el atributo de "estado" y cambiarlo a "activo" para el usuario especificado.
    - Notificar si no existe el usuario dado.
    """

def revisar_reservas():
    print("\n\tREVISAR RESERVAS\n")

    print("\n\tNuevas reservas: \n")
    print("\n\tReservas aprobadas: \n")

    """
    POR HACER en futuros avances:
    - Cargar el archivo "reservas_solicitadas.json" y almacenar los datos temporalmente usando variables, arreglos.
    - Cargar el archivo "reservas_aprobadas.json" y almacenar los datos temporalmente usando variables, arreglos.
    - Para cada reserva proveniente de "reservas_solicitadas.json":
        - Comprobar que la reserva no coincida en términos de fecha, hora y tipo de cancha con una reserva de "reservas_aprobadas.json"
        - De ser así, la reserva se aprueba y puede agregarse al archivo reservas_aprobadas.json"
    """

# ---------------------- FIN DE LAS FUNCIONES DEFINIDAS PARA EL PROGRAMA ----------------------

# Mensaje de bienvenida del Complejo Futbolistico “Los Mejengueros”
print("\t======================================================")
print("\tBienvenido al Complejo Futbolistico “Los Mejengueros”")
print("\t======================================================\n")

# Se llama al menu Principal, este se repite hasta que el usuario salga o ingrese una opcion valida.
menu_principal()   
