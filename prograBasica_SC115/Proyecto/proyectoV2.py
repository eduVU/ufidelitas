import os
import json
from datetime import datetime

# ------------------- FUNCIONES PARA MANIPULAR ARCHIVOS ----------------------

# Funcion para crear los archivos json que manejan los registros y los archivos csv para mostrar la disponibilidad de horarios.
def crear_archivos():
    nombresArchivoJSON = ['usuarios', 'reservas']
    nombresArchivoCSV = ['fut5_1', 'fut5_2', 'fut5_3', 'fut7', 'fut11']
    for nombre in nombresArchivoJSON:
        try:  # Intenta abrir el archivo y leerlo, si no existe, lo crea.
            archivo1 = open(f'{nombre}.json','r')
            archivo1.close()
        except FileNotFoundError:
            data = {}
            archivo1 = open(f'{nombre}.json', 'w')
            json.dump(data, archivo1, indent=2)
            archivo1.close()
    for nombre in nombresArchivoCSV:
        archivo1 = open(f'{nombre}.csv','a')
        archivo1.close()

# Esta funcion abre el archivo solicitado, lee sus contenidos y los retorna en una variable.
def leer_archivo(nombreArchivo, tipo='json'):
    if tipo == 'json':
        archivo = open(f'{nombreArchivo}.json','r')
        datos = json.load(archivo)
        archivo.close()
        return datos
    else:
        archivo = open(f'{nombreArchivo}.csv','r')
        arregloDatos = []  # Este arreglo almacenara la matriz que se obtiene a partir de los datos del archivo.
        for linea in archivo:
            arregloDatos.append(linea.split(','))  # Cada línea se agrega como una fila a la matriz.
        archivo.close()
        return arregloDatos

# Esta funcion sobrescribe los archivos JSON y CSV con los nuevos datos.
def guardar_archivo(nombreArchivo, datos, tipo='json'):
    if tipo == 'json':
        archivoUsuarios = open(f'{nombreArchivo}.json', 'w')
        json.dump(datos, archivoUsuarios, indent=2)
        archivoUsuarios.close()
    else:
        registroHorarios = '' 
        # Se guardan los datos de la disponibilidad de horarios separados por coma en el archivo csv que corresponda.
        for i in range(len(datos)):
            for j in range(30):
                if j == 29:
                    registroHorarios = registroHorarios+str(datos[i][j])+'\n'
                else:
                    registroHorarios = registroHorarios+str(datos[i][j])+','
        archivoDisponibilidad = open(f'{nombreArchivo}.csv', 'w')
        archivoDisponibilidad.write(registroHorarios)
        archivoDisponibilidad.close()
    
#-------------------------- FUNCIONES DEL MODULO 1 ------------------------------

# Funcion que muestra el menu principal del programa, muestra los principales modulos y la opcion de salir.
def menu_principal():
    print('\t======================================================')
    print('\tMenu principal')
    print('\t======================================================\n')
    print('\t[1] Modulo de Clientes')
    print('\t[2] Modulo de Administrador')
    print('\t[3] Modulo de Reservas')
    print('\t[4] Modulo de Informes')
    print('\t[5] Salir')

    cicloMenuPrincipal = True
    while cicloMenuPrincipal == True:
        modulo = input('\tSeleccione un modulo [1,2,3,4,5]: ')
        if modulo == '1':
            modulo = 'clientes'
            cicloMenuPrincipal = False
        elif modulo == '2':
            modulo = 'administrador'
            cicloMenuPrincipal = False
        elif modulo == '3':
            modulo = 'reservas'
            cicloMenuPrincipal = False
        elif modulo == '4':
            modulo = 'informes'
            cicloMenuPrincipal = False
        elif modulo == '5':
            modulo = 'salir'
            cicloMenuPrincipal = False
            print('\tSaliendo del programa, ¡Adios!')
        else:
            print('\tERROR: El modulo ',modulo,' no es valido. Intente de nuevo.\n')

    # Cuando el usuario ingresa una opcion valida, se muestra en la terminal la opcion elegida.   
    if modulo == 'clientes' or modulo == 'administrador' or modulo == 'reservas' or modulo == 'informes':
        print('\n\t======================================================')
        print('\tModulo:',modulo)
        print('\t======================================================\n')
    
    # Cuando el usuario ingresa una opcion valida, se llama la funcion que maneja el menu de cada opcion.
    if modulo == 'clientes':
        menu_clientes()
    elif modulo == 'administrador':
        menu_administrador()
    elif modulo == 'reservas':
        menu_reservas()
    elif modulo == 'informes':
        menu_informes()

# Funcion que despliega el menu del modulo de clientes, incluye las opciones dentro de este modulo y la opcion de salir.
def menu_clientes():
    print('\t[1] Registrarse')
    print('\t[2] Actualizar un cliente existente')
    print('\t[3] Consultar un cliente')
    print('\t[4] Lista de reservas')
    print('\t[5] Salir')

    cicloMenuClientes = True
    while cicloMenuClientes == True:
        opcionMenuCliente = input('\tSeleccione una opcion [1,2,3,4,5]: ')
        if opcionMenuCliente == '1':
            opcionMenuCliente = 'registrarse'
            cicloMenuClientes = False
        elif opcionMenuCliente == '2':
            opcionMenuCliente = 'actualizar'
            cicloMenuClientes = False
        elif opcionMenuCliente == '3':
            opcionMenuCliente = 'consultar'
            cicloMenuClientes = False
        elif opcionMenuCliente == '4':
            opcionMenuCliente = 'lista_reservas'
            cicloMenuClientes = False
        elif opcionMenuCliente == '5':
            cicloMenuClientes = False
            print('\tSaliendo del modulo de clientes...\n')
            menu_principal()  # Al cerrar este menu, vuelve al menu principal.
        else:
            print('\tERROR: La opcion ',opcionMenuCliente,' no es valida. Intente de nuevo.\n')

    if opcionMenuCliente == 'registrarse':
        registrar_usuario()
        menu_principal()
    elif opcionMenuCliente == 'actualizar':
        actualizar_usuario()
        menu_principal()
    elif opcionMenuCliente == 'consultar':
        consultar_usuario()
        menu_principal()
    elif opcionMenuCliente == 'lista_reservas':
        enlistar_reservas()
        menu_principal()

"""
Funcion que realiza el proceso de registrar un nuevo usuario.
Solicita la siguiente informacion:
1. Identificación.
2. Nombre
3. Primer Apellido
4. Segundo Apellido.
5. Teléfono
6. Correo
7. Estado: Activo o Inactivo (por defecto inactivo)
"""
def registrar_usuario():
    print('\n\tCREAR CUENTA\n')

    # Se abre el archivo usuarios.json y se cargan sus contenidos.
    datosUsuarios = leer_archivo('usuarios')

    identificacion = input('\tIngrese su numero de identificacion (formato: 0-0000-0000): ')
    
    # Se verifica si el ID brindado existe en el archivo usuarios.json. Si no es así, se crea un usuario con los datos brindados y se guarda el archivo.
    if identificacion in datosUsuarios:
        print('\tERROR: La identificación del usuario ingresada ya ha sido registrada.\n')
    else: 
        nombre = input('\tIngrese su nombre: \n\t')
        primerApellido = input('\tIngrese su primer apellido: \n\t')
        segundoApellido = input('\tIngrese su segundo apellido: \n\t')
        telefono = input('\tIngrese su numero de telefono (formato: 0000-0000): \n\t')
        correo = input('\tIngrese su correo electronico: \n\t')
        estado = 'inactivo'

        datosUsuarios[identificacion] = {
    'nombre': nombre,
    'primer_apellido': primerApellido,
    'segundo_apellido': segundoApellido,
    'telefono': telefono,
    'correo': correo,
    'estado': estado}
        
        # Se guardan los datos en formato JSON en el archivo designado.
        guardar_archivo('usuarios', datosUsuarios)
        print('\t¡Se ha registrado el usuario exitosamente!\n\t')
  
"""
Funcion que se encarga de actualizar un cliente existente, permitiendo modificar toda la información del cliente y únicamente dejando intacto el estado.
Como funcionalidad extra, se implemento un metodo para actualizar tambien la identificacion.
"""
def actualizar_usuario():
    print('\n\tACTUALIZAR DATOS DE UN USUARIO\n')

    # Se abre el archivo usuarios.json y se cargan sus contenidos.
    datosUsuarios = leer_archivo('usuarios')

    # Se consulta si es necesario cambiar el ID asociado al usuario.
    cicloCambios = True
    while cicloCambios == True:
        cambioID = input('\t¿Desea cambiar su numero de identificacion actual? [s/n] \n\t')
        if cambioID == 's': 
            cicloCambios = False
            identificacionActual = input('\tIngrese el numero de identificacion actual del usuario: \n\t')
            identificacionNueva = input('\tIngrese el nuevo numero de identificacion del usuario: \n\t')
        elif cambioID == 'n':
            cicloCambios = False
            identificacionActual = input('\tIngrese el numero de identificacion actual del usuario: \n\t')
        else:
            print('\tERROR: ingrese una opcion valida.')
    
    # Se verifica si el usuario dado existe actualmente en el sistema.
    if identificacionActual not in datosUsuarios:
        print('\tERROR: La identificacion actual del usuario ingresada no existe en el registro actual.\n')
    else: 
        nombre = input('\tIngrese su nombre: \n\t')
        primerApellido = input('\tIngrese su primer apellido: \n\t')
        segundoApellido = input('\tIngrese su segundo apellido: \n\t')
        telefono = input('\tIngrese su numero de telefono: \n\t')
        correo = input('\tIngrese su correo: \n\t')

        # Si no hace falta cambiar el ID, se sobrescriben los otros datos dejando el ID igual.
        if cambioID == 'n':
            datosUsuarios[identificacionActual] = {
    'nombre': nombre,
    'primer_apellido': primerApellido,
    'segundo_apellido': segundoApellido,
    'telefono': telefono,
    'correo': correo,
    'estado': datosUsuarios[identificacionActual]['estado']}
        # Si es necesario cambiar el ID, se borra el registro del ID viejo del archivo de usuarios y reservas y se guardan los nuevos datos.
        elif cambioID == 's':
            datosUsuarios[identificacionNueva] = {
    'nombre': nombre,
    'primer_apellido': primerApellido,
    'segundo_apellido': segundoApellido,
    'telefono': telefono,
    'correo': correo,
    'estado': datosUsuarios[identificacionActual]['estado']}
            datosUsuarios.pop(identificacionActual)  # Se borra el registro actual.            

            # Se actualizan las reservas que estaban bajo el antiguo ID.
            revisar_reservas('actualizarID', identificacionActual, identificacionNueva)

        # Se guardan los datos en formato JSON en el archivo designado.
        guardar_archivo('usuarios', datosUsuarios)
        print('\t¡Se ha actualizado el usuario exitosamente!\n\t')

# Funcion que se encarga de mostrar toda la informacion de un cliente a partir de su identificacion.
def consultar_usuario():
    print('\n\tCONSULTAR DATOS DEL CLIENTE\n')

    # Se abre el archivo usuarios.json y se cargan sus contenidos.
    datosUsuarios = leer_archivo('usuarios')

    identificacion = input('\tIngrese el numero de identificacion: \n\t')

    if identificacion not in datosUsuarios:
        print('\tERROR: La identificacion de usuario ingresada no existe en el registro actual.\n')
    else: 
        print('\n\tNombre:', datosUsuarios[identificacion]['nombre']) 
        print('\tPrimer apellido:', datosUsuarios[identificacion]['primer_apellido']) 
        print('\tSegundo apellido:', datosUsuarios[identificacion]['segundo_apellido']) 
        print('\tTelefono:', datosUsuarios[identificacion]['telefono']) 
        print('\tCorreo electronico:', datosUsuarios[identificacion]['correo'],'\n') 
   
# Funcion que maneja el listado de reservas y el muestra el numero de solicitud, la cancha, el dia y la hora reservados, la fecha de solicitud y el estado de la reserva.
def enlistar_reservas():
    print('\n\tLISTA DE RESERVAS\n')

    # Se abre el archivo reservas.json y se cargan sus contenidos.
    datosReservas = leer_archivo('reservas')

    identificacion = input('\tIngrese el numero de identificacion del usuario: ')

    for numSolicitud in datosReservas:
        if datosReservas[numSolicitud]['identificacion'] == identificacion:
            print('\n\tNumero de solicitud:', numSolicitud)
            print('\tCancha:', datosReservas[numSolicitud]['cancha']) 
            print('\tDia:', datosReservas[numSolicitud]['dia']) 
            print('\tHora:', datosReservas[numSolicitud]['hora']) 
            print('\tFecha de registro:', datosReservas[numSolicitud]['fecha_registro'])
            print('\tHora de registro:', datosReservas[numSolicitud]['hora_registro'])
            print('\tCosto:', datosReservas[numSolicitud]['costo'])
            print('\tEstado:', datosReservas[numSolicitud]['estado']) 
    print('\n')

#------------------------------- FUNCIONES DEL MODULO 2 ----------------------------

# Funcion que despliega el menu del modulo de administrador, incluye las opciones dentro de este modulo y la opcion de salir.
def menu_administrador():
    print('\t[1] Activar un cliente')
    print('\t[2] Revisar reservas')
    print('\t[3] Salir')

    cicloMenuAdmin = True
    while cicloMenuAdmin == True:
        opcionMenuAdmin = input('\tSeleccione una opcion [1,2,3]: ')
        if opcionMenuAdmin == '1':
            opcionMenuAdmin = 'activar'
            cicloMenuAdmin = False
        elif opcionMenuAdmin == '2':
            opcionMenuAdmin = 'revisar'
            cicloMenuAdmin = False
        elif opcionMenuAdmin == '3':
            cicloMenuAdmin = False
            print('\tSaliendo del modulo de administrador...')
            menu_principal()  # Al cerrar este menu, vuelve al menu principal.
        else:
            print('\tLa opcion ',opcionMenuAdmin,'no es valida. Intente de nuevo.\n')
            
    if opcionMenuAdmin == 'activar':
        activar_usuario()
        menu_principal()
    elif opcionMenuAdmin == 'revisar':
        revisar_reservas()
        menu_principal()

# Funcion que se encarga de activar un usuario determinado. Solo se modifica el atributo "estado".
def activar_usuario():
    print('\n\tACTIVAR USUARIOS\n')

    # Se abre el archivo usuarios.json y se cargan sus contenidos.
    datosUsuarios = leer_archivo('usuarios')
    
    identificacion = input('\tIngrese el numero de identificacion del usuario que desea activar: ')

    if identificacion not in datosUsuarios:
        print('\tERROR: La identificacion de usuario ingresada no existe en el registro actual.\n')
    elif datosUsuarios[identificacion]['estado'] == 'activo':
        print('\tERROR: El usuario ingresado ya esta activo.\n')
    else:
        datosUsuarios[identificacion]['estado'] = 'activo'
        guardar_archivo('usuarios', datosUsuarios)
        print('\t¡Se ha activado el usuario exitosamente!\n\t')

# Esta funcior permite al admin visualizar las solicitudes una por una y aprobarlas siempre y cuando no choquen.
# Ademas, tiene un modo que permite cambiar el ID de las solicitudes registradas en caso de que se actualice el ID de un usuario.
def revisar_reservas(modo='admin', identificacion ='', identificacionNueva=''):
    datosReservas = leer_archivo('reservas')
    if modo == 'actualizarID':
        for numSolicitud in datosReservas:
            if datosReservas[numSolicitud]['identificacion'] == identificacion:
                datosReservas[numSolicitud]['identificacion'] = identificacionNueva
                guardar_archivo('reservas', datosReservas)
    elif modo == 'admin':
        print('\n\tREVISAR RESERVAS PENDIENTES\n')   
        for numSolicitud in datosReservas:
            datosReservas = leer_archivo('reservas')
            if datosReservas[numSolicitud]['estado'] == 'pendiente':
                matrizDisponibilidad = leer_archivo(datosReservas[numSolicitud]['cancha'], 'csv')
                if matrizDisponibilidad[int(datosReservas[numSolicitud]['hora'])-10][int(datosReservas[numSolicitud]['dia'])-1] == 'X':
                    print('\tNOTA: se eliminaron solicitudes que coincidian con espacios que ya fueron ocupados.\n')
                    datosReservas.pop(numSolicitud)
                    guardar_archivo('reservas', datosReservas)
                else:
                    print('\n\tNumero de solicitud:', numSolicitud)
                    print('\tCancha:', datosReservas[numSolicitud]['cancha']) 
                    print('\tDia:', datosReservas[numSolicitud]['dia']) 
                    print('\tHora:', datosReservas[numSolicitud]['hora']) 
                    print('\tFecha de registro:', datosReservas[numSolicitud]['fecha_registro'])
                    print('\tHora de registro:', datosReservas[numSolicitud]['hora_registro'])
                    print('\tCosto:', datosReservas[numSolicitud]['costo'])
                    print('\tIdentificacion:', datosReservas[numSolicitud]['identificacion'])
                    confirmacion = input('\t¿Desea aprobar esta solicitud? [s/n]: ')
                    if confirmacion == 's':
                        datosReservas[numSolicitud]['estado'] = 'aprobado'
                    guardar_archivo('reservas', datosReservas)
                    actualizar_disponibilidad(datosReservas[numSolicitud]['cancha'])

#------------------------------- FUNCIONES DEL MODULO 3 ----------------------------

"""
Esta funcion permite al usuario ingresar una reserva al brindar los siguientes datos:
1. Cancha que desea utilizar.
2. Dia
3. Hora

El local cuenta con lo siguiente:
- Tres canchas de fútbol 5 - 30 mil 
- Una cancha de fútbol 7 - 50 mil
- Una cancha para fútbol 11 - 95 mil

Se trabaja en los siguientes horarios:
- Los 7 días de la semana.
- De 10 am a 9 pm.

Al finalizar la reserva, el sistema imprimirá:
- Un número de solicitud
- El monto a pagar según los gastos administrativos, la cancha y un 13% de IVA

Se parte de los siguientes supuestos:
- Solo usuarios activos pueden hacer reservas
- Se muestran las reservas para un solo mes
- El mes tiene 30 dias
- Cada partido dura 1 hora
"""
def menu_reservas():
    print('\t[1] Reservar cancha de futbol 5')
    print('\t[2] Reservar cancha de futbol 7')
    print('\t[3] Reservar cancha de futbol 11')
    print('\t[4] Salir')

    cicloMenuReservas = True
    while cicloMenuReservas == True:
        opcionMenuReservas = input('\tSeleccione una opcion [1,2,3,4]: ')
        if opcionMenuReservas == '1':
            opcionMenuReservas = 'fut5'
            cicloMenuReservas = False
        elif opcionMenuReservas == '2':
            opcionMenuReservas = 'fut7'
            cicloMenuReservas = False
        elif opcionMenuReservas == '3':
            opcionMenuReservas = 'fut11'
            cicloMenuReservas = False
        elif opcionMenuReservas == '4':
            cicloMenuReservas = False
            print('\tSaliendo del modulo de reservaciones...\n')
            menu_principal()
        else:
            print('\tERROR: La opcion ',opcionMenuReservas,' no es valida. Intente de nuevo.\n')

    reservar_cancha(opcionMenuReservas)
    menu_principal()

# Esta funcion despliega toda la informacion de la cancha seleccionada y permite al usuario hacer la reserva si aplica.
def reservar_cancha(cancha):
    mostrar_disponibilidad(cancha)
    if cancha == 'fut5':
        print('\t[1] Reservar cancha de futbol 5_1')
        print('\t[2] Reservar cancha de futbol 5_2')
        print('\t[3] Reservar cancha de futbol 5_3')
        print('\t[4] Salir')

        cicloFut5 = True
        while cicloFut5 == True:
            opcionFut5 = input('\tSeleccione una opcion [1,2,3,4]: ')
            if opcionFut5 == '1':
                opcionFut5 = 'fut5_1'
                cicloFut5 = False
            elif opcionFut5 == '2':
                opcionFut5 = 'fut5_2'
                cicloFut5 = False
            elif opcionFut5 == '3':
                opcionFut5 = 'fut5_3'
                cicloFut5 = False
            elif opcionFut5 == '4':
                cicloFut5 = False
                print('\tSaliendo de la seleccion de cancha...\n')
                menu_reservas()
            else:
                print('\tERROR: La opcion ',opcionFut5,' no es valida. Intente de nuevo.\n')

        cancha = opcionFut5
    matrizDisponibilidad = leer_archivo(cancha, 'csv')
    dia = input('\tIngrese el dia que desea reservar [1-30]:')
    hora = input('\tIngrese la hora que desea reservar [10-20]: ')

    if matrizDisponibilidad[int(hora)-10][int(dia)-1] == 'X':
        print('\tERROR: la fecha y hora solicitadas ya se encuentran reservadas.\n')
        menu_reservas()
    else: 
        # Verificar que el ID del usuario exista y que este activo.
        datosUsuarios = leer_archivo('usuarios')

        identificacion = input('\tIngrese su numero de identificacion (formato: 0-0000-0000): \n\t')
        
        if identificacion not in datosUsuarios:
            print('\tERROR: La identificacion de usuario ingresada no existe en el registro actual.')
            print('\tSaliendo de la seleccion de cancha...\n')
            menu_reservas()
        elif datosUsuarios[identificacion]['estado'] != 'activo':        
            print('\tERROR: El usuario ingresado no ha sido activado por el administrador.') 
            print('\tSaliendo de la seleccion de cancha...\n')
            menu_reservas()
        else:
            numSolicitud = generar_num_solicitud()
            monto = generar_cobro(cancha)
            crear_reserva(numSolicitud, cancha, dia, hora, identificacion, monto)

# Esta funcion muestra la disponibilidad para todas las canchas disponibles segun el formato elegido.
def mostrar_disponibilidad(cancha):
    if cancha == 'fut11' or cancha == 'fut7':
        actualizar_disponibilidad(cancha)
        mostrar_arreglo(cancha)
    elif cancha == 'fut5':
        actualizar_disponibilidad('fut5_1')
        mostrar_arreglo('fut5_1')
        actualizar_disponibilidad('fut5_2')
        mostrar_arreglo('fut5_2')
        actualizar_disponibilidad('fut5_3')
        mostrar_arreglo('fut5_3')

"""
Esta funcion se encarga de actualizar los arreglos de disponibilidad de horarios para cada cancha en el mes consultado.
Arreglo disponibilidad:
- 11 filas, una para cada hora del dia disponible.
- 30 columnas, una para cada dia del mes
"""
def actualizar_disponibilidad(canchaReservada):
    datosReservas = leer_archivo('reservas')
    matrizDisponibilidad = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    
    # Para cada dia y hora mostrado en una reserva que fue aprobada, se agrega una X en el arreglo.
    for numSolicitud in datosReservas:
        if datosReservas[numSolicitud]['cancha'] == canchaReservada and datosReservas[numSolicitud]['estado'] == 'aprobado':
            matrizDisponibilidad[int(datosReservas[numSolicitud]['hora'])-10][int(datosReservas[numSolicitud]['dia'])-1] = 'X'
    guardar_archivo(canchaReservada, matrizDisponibilidad, 'csv')

# Esta funcion muestra los datos alojados en los archivos CSV para la disponibilidad de las canchas.
def mostrar_arreglo(cancha):
    matrizDisponibilidad = leer_archivo(cancha, 'csv')

    print('\n\tDisponibilidad para la cancha:',cancha)
    print('\tNota: Cada fila comprende una hora del horario [10am - 9pm].\n')
    print('\nNota: Cada columna es un dia del mes [1-30]')

    for i in range(len(matrizDisponibilidad)):
        for j in range(30):
            print(matrizDisponibilidad[i][j],end=" ")
    print('\n')
  
# Esta funcion se encarga de generar un numero de solicitud nuevo para cada reserva valida.
def generar_num_solicitud():
    try:
        datosReservas = leer_archivo('reservas')
        numMayor = 0
        for numSolicitud in datosReservas:
            if int(numSolicitud) == numMayor:
                numMayor += 1
            elif int(numSolicitud) > numMayor:
                numMayor = int(numSolicitud) + 1
        return numMayor
    except KeyError:
        return '0'

# Esta funcion se encarga de informar al usuario sobre el valor total de su reserva.
def generar_cobro(cancha):
    gastosAdm = 2000
    if cancha == 'fut7':
        precioBase = 50000
    elif cancha == 'fut11':
        precioBase = 95000
    else:
        precioBase = 30000
    print('\n\tTOTAL A PAGAR\n')    
    print('\tPrecio de la cancha (1 hora):', precioBase)    
    print('\tGatos administrativos:', gastosAdm)
    print('\tSubtotal:', precioBase+gastosAdm)
    print('\tIVA: 13%')
    print('\tTotal:', round((precioBase+gastosAdm)*1.13,2),'\n')
    return round((precioBase+gastosAdm)*1.13,2)

"""
Esta funcion permite crear una nueva solicitud de reserva con los siguientes datos:
1. Numero solicitud
2. Tipo de cancha
3. Dia
4. Hora
5. Fecha de solicitud
6. Hora de solicitud
7. Costo total
8. ID del usuario
9. Estado de la solicitud
"""    
def crear_reserva(numSolicitud, tipoCancha, dia, hora, identificacion, monto):
    print('\n\tCREAR NUEVA RESERVA\n')

    fecha_hora = datetime.now()  # Se genera la variable que contiene la fecha del sistema.
    fecha = fecha_hora.strftime("%d/%m/%Y")  # Se da formato a la fecha de registro.
    horaReserva = fecha_hora.strftime("%H:%M:%S")  # Se da formato a la hora de registro.

    datosReservas = leer_archivo('reservas')
    datosReservas[numSolicitud] = {
    'cancha': tipoCancha,
    'dia':dia,
    'hora': hora,
    'fecha_registro': fecha,
    'hora_registro': horaReserva,
    'costo': str(monto),
    'identificacion': identificacion,
    'estado': 'pendiente'}

    # Se guardan los datos en formato JSON en el archivo designado.
    guardar_archivo('reservas', datosReservas)
    print('\t¡Se ha registrado la solicitud exitosamente!\n\t')
    print('\tNumero de solicitud de esta reserva:',numSolicitud,'\n\t')

#-------------------------- FUNCIONES DEL MODULO 4 ------------------------------

"""
Esta funcion permite al usuario generar dos posibles informes:
1. Reporte de reservas: muestra todos los datos de reservas para una cancha dada.
2. Reporte de clientes: muestra todos los datos de usuarios para una fecha de registro dada. 
"""
def menu_informes():
    print('\t[1] Generar informe de reservas')
    print('\t[2] Generar informe de clientes')
    print('\t[3] Salir')

    cicloMenuInformes = True
    while cicloMenuInformes == True:
        opcionMenuInformes = input('\tSeleccione una opcion [1,2,3]: ')
        if opcionMenuInformes == '1':
            opcionMenuInformes = 'reservas'
            cicloMenuInformes = False
        elif opcionMenuInformes == '2':
            opcionMenuInformes = 'clientes'
            cicloMenuInformes = False
        elif opcionMenuInformes == '3':
            cicloMenuInformes = False
            print('\tSaliendo del modulo de informes...\n')
            menu_principal()
        else:
            print('\tERROR: La opcion ',opcionMenuInformes,' no es valida. Intente de nuevo.\n')

    if opcionMenuInformes == 'reservas':
        generar_reporte_reservas()
        menu_principal()
    elif opcionMenuInformes == 'clientes':
        generar_reporte_clientes()
        menu_principal()

# Esta funcion solicita la cancha que se desea consultar y muestra todas las reservas realizadas.
def generar_reporte_reservas():
    print('\t[1] Cancha fut5_1')
    print('\t[2] Cancha fut5_2')
    print('\t[3] Cancha fut5_3')
    print('\t[4] Cancha fut7')
    print('\t[5] Cancha fut11')
    print('\t[6] Salir')

    cicloReporte = True
    while cicloReporte == True:
        opcionReporte = input('\tSeleccione una opcion [1,2,3,4,5,6]: ')
        if opcionReporte == '1':
            opcionReporte = 'fut5_1'
            cicloReporte = False
        elif opcionReporte == '2':
            opcionReporte = 'fut5_2'
            cicloReporte = False
        elif opcionReporte == '3':
            opcionReporte = 'fut5_3'
            cicloReporte = False
        elif opcionReporte == '4':
            opcionReporte = 'fut7'
            cicloReporte = False
        elif opcionReporte == '5':
            opcionReporte = 'fut11'
            cicloReporte = False
        elif opcionReporte == '6':
            cicloReporte = False
            print('\tSaliendo de la generacion de reporte...\n')
            menu_informes()
        else:
            print('\tERROR: La opcion ',cicloReporte,' no es valida. Intente de nuevo.\n')

    print('\n\t======================================================')
    print('\tReporte de reservas para la cancha', opcionReporte)
    print('\t======================================================\n')

    datosReservas = leer_archivo('reservas')

    print('\n\tRESERVAS APROBADAS\n')
    for numSolicitud in datosReservas:
        if datosReservas[numSolicitud]['cancha'] == opcionReporte and datosReservas[numSolicitud]['estado'] == 'aprobado':
            print('\n\tNumero de solicitud:', numSolicitud)
            print('\tDia:', datosReservas[numSolicitud]['dia']) 
            print('\tHora:', datosReservas[numSolicitud]['hora']) 
            print('\tFecha de registro:', datosReservas[numSolicitud]['fecha_registro'])
            print('\tHora de registro:', datosReservas[numSolicitud]['hora_registro'])
            print('\tCosto:', datosReservas[numSolicitud]['costo'])
            print('\tIdentificacion:', datosReservas[numSolicitud]['identificacion'])
    print('\n')

    print('\n\tRESERVAS PENDIENTES\n')
    for numSolicitud in datosReservas:
        if datosReservas[numSolicitud]['cancha'] == opcionReporte and datosReservas[numSolicitud]['estado'] == 'pendiente':
            print('\n\tNumero de solicitud:', numSolicitud)
            print('\tDia:', datosReservas[numSolicitud]['dia']) 
            print('\tHora:', datosReservas[numSolicitud]['hora']) 
            print('\tFecha de registro:', datosReservas[numSolicitud]['fecha_registro'])
            print('\tHora de registro:', datosReservas[numSolicitud]['hora_registro'])
            print('\tCosto:', datosReservas[numSolicitud]['costo'])
            print('\tIdentificacion:', datosReservas[numSolicitud]['identificacion'])
    print('\n')

# Esta funcion solicita la fecha de registro que se desea consultar y muestra todos cliente activos en esa fecha.
def generar_reporte_clientes():
    datosUsuarios = leer_archivo('usuarios')
    datosReservas = leer_archivo('reservas')

    fechaConsultada = input('\tIngrese la fecha que desea consultar [formato: dd/mm/aaaa]: ')

    print('\n\t======================================================')
    print('\tReporte de usuarios activos para la fecha', fechaConsultada)
    print('\t======================================================\n')

    # Se verifica que existan reservas para la fecha ingresada, de ser asi se almacena el ID del usuario que hizo esa reserva.
    coincidenciasID = []
    for numSolicitud in datosReservas:
        if datosReservas[numSolicitud]['fecha_registro'] == fechaConsultada:
            coincidenciasID.append(datosReservas[numSolicitud]['identificacion'])

    # Para cada ID recolectado, se muestran los datos completos del usuario que corresponde.
    if len(coincidenciasID) == 0:
        print('\tNo se registraron usuarios activos para la fecha consultada.\n')
    else:
        for id in coincidenciasID:
            print('\n\tNombre:', datosUsuarios[id]['nombre']) 
            print('\tPrimer apellido:', datosUsuarios[id]['primer_apellido']) 
            print('\tSegundo apellido:', datosUsuarios[id]['segundo_apellido']) 
            print('\tTelefono:', datosUsuarios[id]['telefono']) 
            print('\tCorreo electronico:', datosUsuarios[id]['correo'])
            print('\tEstado:', datosUsuarios[id]['estado'])
        print('\n')


# ---------------------- FIN DE LAS FUNCIONES DEL PROGRAMA ----------------------

# Se crean los archivos que necesita el programa.
crear_archivos()

# Mensaje de bienvenida del Complejo Futbolistico “Los Mejengueros”
print("\t======================================================")
print("\tBienvenido al Complejo Futbolistico “Los Mejengueros”")
print("\t======================================================\n")

# Se llama al menu Principal, este se repite hasta que el usuario salga o ingrese una opcion valida.
menu_principal()   