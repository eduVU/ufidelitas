"""
Ejercicio 1: Eduardo es un joven ciclista, cada semana debe reportar a su entrenador la cantidad de kilómetros recorridos en sus prácticas.
Haga un programa que le permita almacenar para cada día los kilómetros recorridos y luego al final de la semana muestre por cada día, junto con el total de la semana.
Para la solución, utilice arreglos y ciclos.
"""
total = 0

recordSemana = [0,0,0,0,0,0,0]
for dia in range(len(recordSemana)):
    recordSemana[dia] = float(input(f'Ingrese los kilometros del dia {dia+1}: '))

for marca in range(len(recordSemana)):
    total += recordSemana[marca]

print('Record por dias:')
for i in range(len(recordSemana)):
    print(f'Dia {i+1}: {recordSemana[i]}.')

print(f'Total semanal: {total}')
