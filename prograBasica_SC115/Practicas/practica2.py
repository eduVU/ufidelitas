"""
Ejercicio 1: Se requiere analizar las calificaciones de los N niños de una escuela y extraer la siguiente estadística:

• Cantidad de calificaciones entre 0 y 50.
• Cantidad de calificaciones entre 51 y 60.
• Cantidad de calificaciones entre 61 y 70.
• Cantidad de calificaciones entre 71 y 100.
• Promedio de calificaciones.
• Muestre los resultados obtenidos
"""
notas0_50 = 0
notas51_60 = 0
notas61_70 = 0
notas71_100 = 0
notas_invalidas = 0
promedio = 0

cantidad_alumnos = int(input('Ingrese la cantidad de alumnos: '))

for i in range(cantidad_alumnos):
    nota = float(input('Ingrese la nota del alumno: '))
    if nota < 0:
        print('Error, ingrese un número entre 0 y 100.')
        cantidad_alumnos -= 1
        notas_invalidas += 1
    elif nota <= 50:
        notas0_50 += 1
        promedio += nota
    elif nota <= 60:
        notas51_60 += 1
        promedio += nota
    elif nota <= 70:
        notas61_70 += 1
        promedio += nota
    elif nota <= 100:
        notas71_100 += 1
        promedio += nota
    else:
        print('Error, ingrese un número entre 0 y 100.')
        cantidad_alumnos -= 1
        notas_invalidas += 1

promedio /= cantidad_alumnos

print('Resultados:\n'
        f'Cantidad de notas entre 0 y 50: {notas0_50}.\n'
        f'Cantidad de notas entre 51 y 60: {notas51_60}.\n'
        f'Cantidad de notas entre 61 y 70: {notas61_70}.\n'
        f'Cantidad de notas entre 71 y 100: {notas71_100}.\n'
        f'Cantidad de notas invalidas: {notas_invalidas}.\n'
        f'Promedio de notas: {promedio}.\n')

"""
Ejercicio 2: Desarrolle un programa que le solicita al usuario los salarios de 15 empleados de una compañía 
y que le indique cuánto dinero se necesita para que al menos todos ganen $500
"""

saldo = 0

for i in range(15):
    salario = float(input('Ingrese el salario del empleado en dolares: '))
    diferencia = 500 - salario
    if diferencia > 0:
        saldo += diferencia

if saldo == 0:
    print('No se necesita más dinero, todos ganan al menos $500.')
else:
    print('Se necesitan un total de:',saldo,'dolares para que todos los empleados ganen al menos $500.')