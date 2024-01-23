import json
from datetime import datetime 

# # Crear un diccionario anidado.
# data = {}

# data['id1'] = {
#     'nombre': 'Sigrid',
#     'apellido': 'Mannock',
#     'edad': 27,
#     'estatura': 1.62}

# data['id2'] = {
#     'nombre': 'Joe',
#     'apellido': 'Hinners',
#     'edad': 31,
#     'estatura': 1.77}

# data['id3'] = {
#     'nombre': 'Eduardo',
#     'apellido': 'Villalobos',
#     'edad': 30,
#     'estatura': 1.84}

# # Crear archivo JSON
# archivo = open('data.json', 'w')
# json.dump(data, archivo, indent=2)
# archivo.close()

# # Cargar archivo JSON y guardarlo en una variable.
# archivo = open('data.json')
# data = json.load(archivo)
# archivo.close()

# Mostrar los contenidos del archivo.
# for id in data:
    # print(id)
    # print(type(id))
    # print('Nombre:', data[id]['nombre']) 
    # print('Apellido:', data[id]['apellido']) 
    # print('Edad:', data[id]['edad']) 
    # print('Estatura:', data[id]['estatura']) 
    # print('\n')

# # Actualizar los contenidos del archivo.
# if 'id4' in data:
#     print('ID already exists')
# else:
#     data['id4'] = {
# 'nombre': 'Victoria',
# 'apellido': 'Quesada',
# 'edad': 4,
# 'estatura': 1.00}

# archivo = open('data.json', 'w')
# json.dump(data, archivo, indent=2)
# archivo.close()


# # /--------------------------------------------------------------------/


# def leer_archivo(nombreArchivo, tipo='json'):
#     if tipo == 'json':
#         archivo = open(f'{nombreArchivo}.json','r')
#         datos = json.load(archivo)
#         archivo.close()
#         return datos
#     else:
#         archivo = open(f'{nombreArchivo}.csv','r')
#         arregloDatos = []  # Este arreglo almacenara la matriz que se obtiene a partir de los datos del archivo.
#         for linea in archivo:
#             arregloDatos.append(linea.split(','))  # Cada línea se agrega como una fila a la matriz.
#         archivo.close()
#         return arregloDatos


# def crear_archivos():
#     try:  # Intenta abrir el archivo y leerlo, si no existe, lo crea.
#         archivo1 = open('usuarios.json','r')
#         archivo1.close()
#     except FileNotFoundError:
#         data = {}
#         archivo1 = open('usuarios.json', 'w')
#         json.dump(data, archivo1, indent=2)
#         archivo1.close()

# def registrar_usuario(identificacion, nombre, primerApellido, segundoApellido, telefono, correo, estado):
#     # Se abre el archivo usuarios.json y se cargan sus contenidos.
#     archivoUsuarios = open('usuarios.json','r')
#     datosUsuarios = json.load(archivoUsuarios)
#     archivoUsuarios.close()
    
#     # Se verifica si el ID brindado existe en el archivo usuarios.json. Si no es así, se crea un usuario con los datos brindados y se guarda el archivo.
#     if identificacion in datosUsuarios:
#         print('ERROR: La identificación del usuario ingresado ya ha sido registrada.')
#     else: 
#         datosUsuarios[identificacion] = {
#     'nombre': nombre,
#     'primer_apellido': primerApellido,
#     'segundo_apellido': segundoApellido,
#     'telefono': telefono,
#     'correo': correo,
#     'estado': estado}
        
#         archivoUsuarios = open('usuarios.json', 'w')
#         json.dump(datosUsuarios, archivoUsuarios, indent=2)
#         archivoUsuarios.close()
        
# # Esta funcion se encarga de generar un numero de solicitud nuevo para cada reserva valida.
# def generar_num_solicitud():
#     try:
#         datosReservas = leer_archivo('reservas')
#         numMayor = 0
#         for numSolicitud in datosReservas:
#             if int(numSolicitud) > numMayor:
#                 numMayor = numSolicitud
#         return numMayor
#     except KeyError:
#         return '1'

# crear_archivos()

# try:
#     datosReservas = leer_archivo('reservas')
#     numMayor = 0
#     for numSolicitud in datosReservas:
#         if int(numSolicitud) > numMayor:
#             numMayor = numSolicitud
#     print(numMayor)
# except KeyError:
#     print('1')

# datosReservas = leer_archivo('reservas')
# numMayor = 0
# for numSolicitud in datosReservas:
#     if int(numSolicitud) == numMayor:
#         numMayor += 1
#     elif int(numSolicitud) > numMayor:
#         numMayor = int(numSolicitud) + 1
# print(numMayor)

# identificacion = '4-0238-0171'
# nombre = 'Stephanie'
# primerApellido = 'Araica'
# segundoApellido = 'Urbina'
# telefono = '7200-4397'
# correo = 'stephanie@algo.com'
# estado = 'inactivo'

# registrar_usuario(identificacion, nombre, primerApellido, segundoApellido, telefono, correo, estado)
# borrar_usuario(identificacion)


# fecha_hora = datetime.now()  # Variable que contiene la fecha y hora
# fecha_hora = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")  # Se da formato a la fecha y hora.
# print(fecha_hora)
