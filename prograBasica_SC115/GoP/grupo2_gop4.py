"""
Ejercicio 1: Investigue la función SPLIT de Python y elabore mediante funciones un ejemplo de uso.
"""

""" 
La funcion split() permite separar un string en varios elementos para formar una lista.
Forma de uso: string.split(delimitador, maximoSplits), donde:
  - delimitador: es el elemento que se usa como criterio para segmentar el string, ejemplos: coma (,), numeral (#), dos puntos (:), etc.
  - maximoSplits: indica la cantidad de elementos maxima que se van a generar. Si este valor vale 2, entonces el string se divide en un maximo de 2 elementos.
                  Si no se indica un valor, su valor por defecto es -1, lo cual indica que no hay un limite en la cantidad de segmentos que se generan.
"""

"""
Ejemplo de uso:
Este programa permite registrar los productos de supermercado comprados y guardarlos en un archivo con formado CSV (comma-separated values).
El usuario tambien puede acceder al archivo y mostrar sus contenidos, para ello se lee el formato CSV, se elimina la coma y se muestra un listado de los productos.
"""

# Funcion para crear el archivo csv.
def crear_archivo():
    archivo = open('listaCompras.csv', 'a')
    archivo.close()

# Funcion para agregar datos al archivo en formato csv.
def agregar_datos():
    print('AGREGAR DATOS')
    registro = ''
    cantidadProductos = int(input('Ingrese la cantidad de productos que desea registrar: '))
    for i in range(cantidadProductos):
        producto = input('Ingrese el producto comprado: ')
        registro = registro+producto+','
    archivo = open('listaCompras.csv', 'a')
    archivo.write(registro)
    archivo.close()

# Funcion para mostrar los datos del archivo CSV, esta extrae los valores individuales del archivo y los muestra como un listado sin comas.
def mostrar_datos():
    print('MOSTRAR PRODUCTOS')
    archivo = open('listaCompras.csv', 'r')
    datos = archivo.read()
    listado = datos.split(',')
    for i in range(len(listado)):
        print(listado[i])
    archivo.close()

def menu():
    cicloMenu = True
    while cicloMenu == True:
        print('\nMenu del programa: ')
        print('[1] Agregar productos comprados')
        print('[2] Mostrar productos comprados')
        print('[3] Salir\n')

        opcion = input('Ingrese una opcion [1,2,3]: \n')
        if opcion == '1':
            agregar_datos()
            continuar = input('¿Desea realizar otra accion? [s/n]\n')
            if continuar == 's':
                cicloMenu = True
            elif continuar == 'n':
                print('¡Adios!')
                cicloMenu = False
        elif opcion == '2':
            mostrar_datos()
            continuar = input('¿Desea realizar otra accion? [s/n]\n')
            if continuar == 's':
                cicloMenu = True
            elif continuar == 'n':
                print('¡Adios!')
                cicloMenu = False
        elif opcion == '3':
            print('¡Adios!')
            cicloMenu = False
        else: 
            print('Error: ingrese una opcion valida.')

crear_archivo()
menu()


"""
Ejercicio 2: Elabore un menú en Python que permita:
a.	Solicitar un número entero, mediante el cual se creará un arreglo de números enteros.
b.	Rellenar el arreglo, mediante esta opción se incluirán números enteros con edades de personas hasta completar el tamaño del arreglo.
c.	Realizar cálculo, mediante esta opción, se creará un arreglo unidimensional que manejará en cada posición del arreglo los siguientes resultados:
i.	Edad mínima.
ii.	Edad máxima.
iii.	Edad promedio.
iv.	Cantidad de personas mayores a 18.
v.	Cantidad de personas mayores de 30.
d.	Guardar datos, mediante esta opción se crearán dos archivos, el primero llamado edades.txt, guardará el arreglo de edades, cada una separada por comas. El segundo arreglo, denominado resultado.txt guardará el arreglo de los cálculos separados por comas.
e.	Cargar datos, mediante esta opción se abrirán ambos archivos y se cargarán los datos en cada uno de los arreglos.
f.	Mostrar datos, imprimirá ambos arreglos por pantalla de tabulada para facilitar su lectura.
g.	Salir, saldrá del programa.
"""

# Funcion para crear los archivos edades.txt y resultado.txt.
def crear_archivos():
    archivo1 = open('edades.txt', 'a')
    archivo1.close()
    archivo2 = open('registro.txt', 'a')
    archivo2.close()

# Funcion para pedir las edades al usuario y crear un arreglo con los datos
def registrar_edades(tamano):
    print('NUEVO REGISTRO DE EDADES\n')
    listadoEdades = {}
    for i in range(tamano):
        if i == 0:
            listadoEdades[i] = int(input('Ingrese la primera edad: '))
        else:
            listadoEdades[i] = int(input('Ingrese la siguiente edad: '))
    return listadoEdades

# Funcion para calcular las edades minima, maxima y promedio y la cantidad de personas mayores a 18 y 30.
def realizar_calculos(arregloEdades):
    edadMinima = 10000
    edadMaxima = 0
    edadPromedio = 0
    conteo18 = 0  # Cantidad de edades iguales o superiores a 18
    conteo30 = 0  # Cantidad de edades iguales o superiores a 30
    for i in range(len(arregloEdades)):
        if arregloEdades[i] <= edadMinima:  # Comprobar edad minima
            edadMinima = arregloEdades[i]
        if arregloEdades[i] >= edadMaxima:  # comprobar edad maxima
            edadMaxima = arregloEdades[i]
        if arregloEdades[i] >= 30:  # Comprobar si la edad es mayor o igual a 18 y/o 30
            conteo18 += 1
            conteo30 += 1
        elif arregloEdades[i] >= 18:
            conteo18 += 1
        edadPromedio += arregloEdades[i]  # Calculo parcial del promedio de edades
    edadPromedio /= len(arregloEdades)  # Calculo final del promedio de edades
    listadoCalculos = [edadMinima,edadMaxima,edadPromedio,conteo18,conteo30]
    print('Se han calculado exitosamente las estadisticas para el arreglo de edades brindado.')
    return listadoCalculos

# Funcion para agregar los datos a ambos archivos txt.
def guardar_datos(arregloEdades, arregloCalculos):
    registroEdades = ''
    registroCalculos = ''
    
    # Se guardan las edades separadas por coma en el archivo edades.txt.
    for i in range(len(arregloEdades)):
        registroEdades = registroEdades+str(arregloEdades[i])+','
    archivoEdades = open('edades.txt', 'a')
    archivoEdades.write(registroEdades)
    archivoEdades.write('\n')
    archivoEdades.close()

    # Se guardan los calculos separados por coma en el archivo registro.txt.
    for i in range(len(arregloCalculos)):
        registroCalculos = registroCalculos+str(arregloCalculos[i])+','
    archivoCalculos = open('registro.txt', 'a')
    archivoCalculos.write(registroCalculos)
    archivoCalculos.write('\n')
    archivoCalculos.close()
    print('Se han guardado los datos exitosamente.')

# Funcion para cargar los datos de los archivos a los arreglos del programa.
def cargar_datos():
    # Cargar los datos de edades
    archivoEdades = open('edades.txt', 'r')
    edades = archivoEdades.read()
    arregloEdades = edades.split(',')
    archivoEdades.close()

    # Cargar los datos de calculos
    archivoCalculos = open('registro.txt', 'r')
    calculos = archivoCalculos.read()
    arregloCalculos = calculos.split(',') 
    archivoCalculos.close()

    print('Se han cargado los datos exitosamente.')
    return arregloEdades, arregloCalculos

# Funcion para mostrar los datos en la terminal. El programa muestra los datos que esten actualmente cargados en el programa, ya sean los agregados al correr el programa o los cargados desde el archivo.
def mostrar_datos(arregloEdades, arregloCalculos):
    print('MOSTRAR DATOS\n')
    print('Arreglos de edades:')
    for i in range(len(arregloEdades)):
        print(arregloEdades[i],end=" ")
    print('\n')

    print('Estadisticas (edad minima, edad maxima, edad promedio, mayores a 18, mayores a 30):')
    for i in range(len(arregloCalculos)):
        print(arregloCalculos[i],end=" ")
    print('\n')

def menu():
    cicloMenu = True
    while cicloMenu == True:
        print('\nMenu del programa: ')
        print('[a] Definir el tamaño del registro')
        print('[b] Rellenar el arreglo de edades')
        print('[c] Realizar calculos estadisticos')
        print('[d] Guardar datos de los arreglos')
        print('[e] Cargar datos de los arreglos')
        print('[f] Mostrar datos')     
        print('[g] Salir\n')

        opcion = input('Ingrese una opcion [a,b,c,d,e,f,g]: \n')
        if opcion == 'a':
            tamanoArreglo = int(input('Ingrese la cantidad de edades que desea registrar: '))
        elif opcion == 'b':
            registroEdades = registrar_edades(tamanoArreglo)
        elif opcion == 'c':
            registroCalculos = realizar_calculos(registroEdades)
        elif opcion == 'd':
            guardar_datos(registroEdades, registroCalculos)
            continuar = input('¿Desea realizar otra accion? [s/n]\n')
            if continuar == 's':
                cicloMenu = True
            elif continuar == 'n':
                print('¡Adios!')
                cicloMenu = False
        elif opcion == 'e':
            registroEdades, registroCalculos = cargar_datos()
        elif opcion == 'f':
            mostrar_datos(registroEdades, registroCalculos)
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