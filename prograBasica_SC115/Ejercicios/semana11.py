import os

"""
Desarrolle un programa que controla las notas obtenidas por los estudiantes del curso de Programación Básica.
En un archivo debe registrar la siguiente información: nombre, número de grupo y calificación.
Cree las funciones para agregar y mostrar información.
Es conveniente que el acceso a las funciones se realice a través de un menú.
"""

def crear_archivo():
    archivo = open('datosAlumnos.txt', 'a')
    archivo.close()

def agregar_datos():
    print('AGREGAR DATOS')
    nombre = input('Ingrese el nombre del estudiante: ')
    grupo = input('Ingrese el grupo del estudiante: ')
    calificacion = int(input('Ingrese la calificacion del estudiante: '))
    archivo = open('datosAlumnos.txt', 'a')
    archivo.write(f'{nombre}, {grupo}, {calificacion}')
    archivo.write('\n')
    archivo.close()

def mostrar_datos():
    print('MOSTRAR DATOS')
    archivo = open('datosAlumnos.txt', 'r')
    datos = archivo.read()
    print(datos)
    archivo.close()

def menu():
    cicloMenu = True
    while cicloMenu == True:
        print('\nMenu del programa: ')
        print('[1] Agregar datos')
        print('[2] Mostrar datos')
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

#---------------------------- INICIO DEL PROGRAMA ----------------------------
crear_archivo()
menu()