"""
Ejercicio 1: Desarrolle un programa que muestre los números pares del 20 al 40
y a la par de cada número muestre su cuadrado.
"""

inicio = 20 
while inicio <= 40:
    print(f'Numero: {inicio}, cuadrado: {inicio**2}')
    inicio += 2

"""
Ejercicio 2: Desarrolle un programa que permita determinar la nota mayor, la nota menor, la cantidad
de aprobados y la cantidad de reprobados de un grupo de alumnos. Muestre los resultados obtenidos.
Notas: No se conoce la cantidad de alumnos y la nota de aprobación es 70.
"""

alumnos = int(input('Ingrese la cantidad de alumnos: '))

notaMayor = 0
notaMenor = 101
aprobados = 0
reprobados = 0

for i in range(alumnos):
    nota = int(input(f'Ingrese la nota del alumno {i+1}: '))
    if nota < notaMenor:
        notaMenor = nota
    if nota > notaMayor:
        notaMayor = nota
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

print('Nota mayor:', notaMayor)
print('Nota menor:', notaMenor)
print('Cantidad de aprobados:', aprobados)
print('Cantidad de reprobados:', reprobados)
