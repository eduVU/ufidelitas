"""
Ejercicio 1: Un profesor necesita un programa que calcule la nota final de sus estudiantes.
Tiene 25 estudiantes que realizan 4 actividades evaluativas (para efectos de esta clase, se reducira a 5 estudiantes).
Utilice una matriz para almacenar las calificaciones donde cada fila representara un estudiante y las columnas almacenaran la informacion de las actividades evaluativas.
"""

def registrar_calificaciones():
    print('REGISTRAR CALIFICACIONES')
    arregloNotas = [[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]]
    
    for i in range(5):
        print(f'\nCalificaciones del estudiante{i+1}:')
        for j in range(4):
            nota = float(input(f'Ingrese la nota de la actividad evaluativa {j+1}: '))
            arregloNotas[i][j] = nota
    return arregloNotas

def calcular_nota_final(calificaciones):
    notasFinales = [0,0,0,0,0]
    for i in range(5):
        promedio = 0
        for j in range(4):
            promedio += calificaciones[i][j]
        notasFinales[i] = promedio/4
    print('\nCALCULAR NOTAS FINALES')
    for i in range(5):
        print(f'La nota final del estudiante{i+1} es: {notasFinales[i]}')

def menu():
    cicloMenu = True
    while cicloMenu == True:
        print('\nREGISTRO DE CALIFICIACIONES')
        print('[1] Registrar calificaciones y calcular promedios.')
        print('[2] Salir.\n')

        opcion = input('Ingrese una opcion:  ')

        if opcion == '1':
            registroActualizado = registrar_calificaciones()
            calcular_nota_final(registroActualizado)
        elif opcion == '2':
            print('¡Adios!')
            cicloMenu = False
        else: 
            print('Error: se ha ingresado una opcion invalida.')

menu()

# -------------------------------------------------------------------------------------------------------------

"""
Ejercicio 2: Desarrolle un programa para reservar espacios en una microbus que da servicio en 4 horarios. 
Se le pide que inicialmente almacene un valor 0 en los 20 espacios disponibles, luego le solicite al usuario la posición que desea reservar,
remplazando el valor de 0 por un 1 (que representa vendido)
"""

def reservar_espacios(asientos):
    print('\nRESERVAR ESPACIOS')
    print('\nHorarios disponibles: ')
    print('[1] Horario de madrugada.')
    print('[2] Horario de dia.')
    print('[3] Horario de tarde.')
    print('[4] Horario de noche.')

    horario = int(input('\nIngrese el horario deseado [1,2,3,4]: '))
    espacio = int(input('Ingrese el asiento que desea reservar [1-20]: '))

    if asientos[horario-1][espacio-1] == 1:
        print('Lo sentimos, este espacio ya esta reservado.')
    else: 
        asientos[horario-1][espacio-1] = 1
    return asientos

def consultar_reservas(asientos):
    print('\nCONSULTAR LAS RESERVAS')
    print('Los asientos disponibles tienen un 0.')
    print('Los asientos comprados tienen un 1.\n')
    
    for i in range(4):
        for j in range(20):
            print(asientos[i][j],end=" ")
        print("\n")
    
# Al iniciar el programa, todos los espacios en cada horario están disponibles (su valor es 0).
espacios = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

cicloMenu = True
# Menu principal.
while cicloMenu == True:
    print('\nMENU DEL SERVICIO DE MICROBUS')
    print('[1] Reservar espacios.')
    print('[2] Mostrar estado de las reservaciones.')
    print('[3] Salir.\n')

    opcion = input('Ingrese una opcion:  ')

    if opcion == '1':
        # El arreglo que almacena los espacios se actualiza por medio de la funcion de registro.
        espacios = reservar_espacios(espacios)
    elif opcion == '2':
        # Se muestran todos los asientos ocupados (valor = 1) y los asientos disponibles (valor = 0)
        consultar_reservas(espacios)
    elif opcion == '3':
        print('¡Adios!')
        cicloMenu = False
    else: 
        print('Error: se ha ingresado una opcion invalida.')
