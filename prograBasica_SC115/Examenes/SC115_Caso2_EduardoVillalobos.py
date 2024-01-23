"""
Ejercicio 1: Elabore un menú en Python que permita:
a. Cargar los datos del archivo “Personas.csv” suministrados por el profesor en una matriz de 7 columnas. (Se carga exactamente igual que un archivo de texto)
b. Actualizar datos, mediante esta opción, en las últimas dos columnas se almacenará la edad actual y el IMC de cada persona.
    i. La edad actual se obtiene restando el año actual y el año de nacimiento.
    ii. El IMC se calcula: peso / (estatura * estatura)
c. Mostrar resultados, mediante la cual se imprimirá en pantalla la siguiente información estadística:
    i. Cantidad de personas con IMC mayor a 30.
    ii. Edad máxima y Edad mínima.
    iii. Cantidad de personas menores de 18 con IMC mayor a 30.
    iv.	Cantidad de personas mayores a 18 con IMC mayor a 30.
d. Guardar datos, mediante esta opción se crearán dos archivos, el primero llamado Personas_act.txt, guardará el arreglo de personas, con cada dato de la persona separado por comas. El segundo arreglo, denominado resultado.txt guardará el arreglo de los cálculos separados por comas.
e. Cargar datos, mediante esta opción se abrirán ambos archivos y se cargarán los datos en cada uno de los arreglos.
f. Mostrar datos, imprimirá ambos arreglos por pantalla de forma tabulada para facilitar su lectura.
g. Salir, saldrá del programa.
"""

# Funcion para crear los archivos Personas_act.txt y resultado.txt.
def crear_archivos():
    archivo1 = open('Personas_act.txt', 'a')
    archivo1.close()
    archivo2 = open('resultado.txt', 'a')
    archivo2.close()

# Funcion para cargar los datos del archivo Personas.csv al programa.
def cargar_datos_originales():
    archivoOriginal = open('Personas.csv','r')
    arregloDatos = []  # Este arreglo almacenará la matriz que se obtiene a partir de los datos del archivo original.
    columnasExtra = ['0','0']  # Nuevas columnas de la matriz
    for linea in archivoOriginal:
        arregloDatos.append(linea.split(',')+columnasExtra)  # Cada línea se agrega como una fila a la matriz, que contiene 5 columnas con los valores separados por coma del archivo + 2 adicionales.
    return arregloDatos

# Funcion para actualizar las columnas de edad e IMC con datos de las personas.
def actualizar_datos(arregloDatos):
    for i in range(1, len(arregloDatos)):
        arregloDatos[i][5] = 2023 - int(arregloDatos[i][1])  # Se calcula la edad de cada persona y se almacena en la sexta columna.
        arregloDatos[i][6] = float(arregloDatos[i][3]) / (float(arregloDatos[i][4])**2)  # Se calcula el IMC de cada persona y se almacena en la séptima columna.
        print('Se ha actualizado exitosamente la edad y el IMC para los datos brindados.')
    return arregloDatos

# Funcion para registrar la cantidad de personas con IMC mayores a 30, la edad minima y maxima y la cantidad de personas mayores y menores a 18 con IMC superior a 30.
def realizar_calculos(arregloDatos):
    print(len(arregloDatos))
    edadMinima = 10000
    edadMaxima = 0
    conteoIMC30 = 0  # Cantidad de personas con IMC mayor a 30
    conteoMayor18 = 0  # Cantidad de personas con 18 anios o mas con IMC mayor a 30
    conteoMenor18 = 0  # Cantidad de personas con menos de 18 anios con IMC mayor a 30
    for i in range(1, len(arregloDatos)):
        if int(arregloDatos[i][5]) <= edadMinima:  # Comprobar edad minima
            edadMinima = int(arregloDatos[i][5])
        if int(arregloDatos[i][5]) >= edadMaxima:  # comprobar edad maxima
            edadMaxima = int(arregloDatos[i][5])
        if float(arregloDatos[i][6]) > 30:  # Comprobar los casos donde el IMC es mayor a 30
            conteoIMC30 += 1
            if int(arregloDatos[i][5]) < 18:  # Comprobar los casos donde IMC es mayor a 30 y la edad menor a 18
                conteoMenor18 += 1
            elif int(arregloDatos[i][5]) >= 18:  # Comprobar los casos donde IMC es mayor a 30 y la edad mayor a 18
                conteoMayor18 += 1
    listadoCalculos = [conteoIMC30,edadMaxima,edadMinima,conteoMenor18,conteoMayor18]
    print('Se han calculado exitosamente las estadisticas para el arreglo de personas brindado.')
    return listadoCalculos

# Funcion para mostrar los calculos realizados en la terminal.
def mostrar_calculos(arregloCalculos):
    print('MOSTRAR CALCULOS\n')
    print('Estadisticas (cantidad de personas con IMC mayor a 30, edad maxima, edad minima, menores a 18 con IMC mayor a 30, mayores a 18 con IMC mayor a 30):')
    for i in range(len(arregloCalculos)):
        print(arregloCalculos[i],end=" ")
    print('\n')

# Funcion para agregar los datos a ambos archivos txt.
def guardar_datos(arregloEdades, arregloCalculos):
    registroEdades = ''
    registroCalculos = ''
    
    # Se guardan los datos de personas separados por coma en el archivo Personas_act.txt.
    for i in range(1, len(arregloEdades)):
        for j in range(7):
            if j == 6:
                registroEdades = registroEdades+str(arregloEdades[i][j])+'\n'
            else:
                registroEdades = registroEdades+str(arregloEdades[i][j])+','
    archivoEdades = open('Personas_act.txt', 'a')
    archivoEdades.write(registroEdades)
    archivoEdades.close()

    # Se guardan los calculos separados por coma en el archivo resultado.txt.
    for i in range(len(arregloCalculos)):
        if i == 4:
            registroCalculos = registroCalculos+str(arregloCalculos[i])+'\n'
        else:
            registroCalculos = registroCalculos+str(arregloCalculos[i])+','
    archivoCalculos = open('resultado.txt', 'a')
    archivoCalculos.write(registroCalculos)
    archivoCalculos.close()
    print('Se han guardado los datos exitosamente.')

# Funcion para cargar los datos de los archivos a los arreglos del programa.
def cargar_datos():
    # Cargar los datos de las personas
    archivoEdades = open('Personas_act.txt', 'r')
    edades = archivoEdades.read()
    arregloEdades = edades.split(',')
    archivoEdades.close()

    # Cargar los datos de calculos
    archivoCalculos = open('resultado.txt', 'r')
    calculos = archivoCalculos.read()
    arregloCalculos = calculos.split(',') 
    archivoCalculos.close()

    print('Se han cargado los datos exitosamente.')
    return arregloEdades, arregloCalculos

# Funcion para mostrar los datos en la terminal. El programa muestra los datos que esten actualmente cargados en el programa, ya sean los agregados al correr el programa o los cargados desde el archivo.
def mostrar_datos(arregloEdades, arregloCalculos):
    print('MOSTRAR DATOS\n')
    print('Arreglos de personas:')
    for i in range(1, len(arregloEdades)):
        for j in range(7):
            print(arregloEdades[i][j],end=" ")
    print('\n')

    print('Estadisticas:')
    for i in range(len(arregloCalculos)):
        print(arregloCalculos[i],end=" ")
    print('\n')

def menu():
    cicloMenu = True
    while cicloMenu == True:
        print('\nMenu del programa: ')
        print('[a] Cargar el archivo de referencia (personas.csv)')
        print('[b] Actualizar los datos')
        print('[c] Mostrar resultados estadísticos')
        print('[d] Guardar datos de los arreglos')
        print('[e] Cargar datos de los arreglos')
        print('[f] Mostrar datos de los arreglos')     
        print('[g] Salir\n')

        opcion = input('Ingrese una opcion [a,b,c,d,e,f,g]: \n')
        if opcion == 'a':
            registroDatos = cargar_datos_originales()
        elif opcion == 'b':
            registroDatos = actualizar_datos(registroDatos)
        elif opcion == 'c':
            registroCalculos = realizar_calculos(registroDatos)
            mostrar_calculos(registroCalculos)
        elif opcion == 'd':
            guardar_datos(registroDatos, registroCalculos)
            continuar = input('¿Desea realizar otra accion? [s/n]\n')
            if continuar == 's':
                cicloMenu = True
            elif continuar == 'n':
                print('¡Adios!')
                cicloMenu = False
        elif opcion == 'e':
            registroDatos, registroCalculos = cargar_datos()
        elif opcion == 'f':
            mostrar_datos(registroDatos, registroCalculos)
            continuar = input('¿Desea realizar otra accion? [s/n]\n')
            if continuar == 's':
                cicloMenu = True
            elif continuar == 'n':
                print('¡Adios!')
                cicloMenu = False
        elif opcion == 'g':
            print('¡Adios!')
            cicloMenu = False
        else: 
            print('Error: ingrese una opcion valida.')

crear_archivos()
menu()