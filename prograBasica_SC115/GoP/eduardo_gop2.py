"""
Problema 1: Escribe un programa en Python que simule un sistema de votación para una elección. El programa debe solicitar a varios usuarios que emitan su voto 
por uno de los candidatos y calcular el resultado de la elección.
Notas importantes:
- No se conoce la cantidad de votantes.
- Los candidatos deben ser solicitados al usuario.
- Al finalizar debe mostrar el ganador.
- Debe verificar que el voto ingresado corresponda a uno de los candidatos, caso contrario, deberá contar como voto nulo.
"""

# Lista de candidatos.
candidato1 = input('Ingrese el nombre del primer candidato: ')

candidato2 = input('Ingrese el nombre del segundo candidato: ')

candidato3 = input('Ingrese el nombre del tercer candidato: ')

# Contadores de votos de los candidatos y de votos nulos.
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_nulos = 0

cantidad_votantes = int(input('Ingrese la cantidad de votantes: '))

for i in range(cantidad_votantes):
    if i == 0:
        voto = input('Primer votante, ingrese el nombre del candidato elegido: ')
    else:
        voto = input('Siguiente votante, ingrese el nombre del candidato elegido: ')

    if voto == candidato1:
        votos_candidato1 += 1
    elif voto == candidato2:
        votos_candidato2 += 1
    elif voto == candidato3:
        votos_candidato3 += 1
    else:
        votos_nulos += 1

# Se determina el ganador de las votaciones:
ganador = ''
if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
    ganador = candidato1
elif votos_candidato1 < votos_candidato2 and votos_candidato2 > votos_candidato3:
    ganador = candidato2
elif votos_candidato1 < votos_candidato3 and votos_candidato2 < votos_candidato3:
    ganador = candidato3
else:
    ganador = 'empate'

print('Votos para el candidato',candidato1,':',votos_candidato1)
print('Votos para el candidato',candidato2,':',votos_candidato2)
print('Votos para el candidato',candidato3,':',votos_candidato3)

if ganador == 'empate':
    print('El resultado fue un empate.')
else:
    print('El ganador de las elecciones es:',ganador)


"""
Problema 2: Escribe un programa en Python que permita al usuario convertir temperaturas de grados Celsius a grados Fahrenheit y viceversa. El programa debe solicitar
al usuario la temperatura y la unidad de medida (Celsius o Fahrenheit), y realizar la conversión correspondiente.

a.	Si la unidad de medida es "C", realiza la conversión de Celsius a Fahrenheit utilizando la fórmula: Fahrenheit = Celsius * 9/5 + 32.
b.	Si la unidad de medida es "F", realiza la conversión de Fahrenheit a Celsius utilizando la fórmula: Celsius = (Fahrenheit - 32) * 5/9.

Notas importantes:
-	Debe verificar que la medida ingresada sea únicamente Celsius o Fahrenheit.
"""

unidad = input('Ingrese la unidad de temperatura que desea utilizar (C/F): ')

temperatura = float(input('Ingrese la magnitud de la temperatura: '))

if unidad == 'C':
    resultado = temperatura * 9/5 + 32
    print(temperatura,'°C equivalen a',resultado,'°F')
elif unidad == 'F':
    resultado = (temperatura - 32) * 5/9.
    print(temperatura,'°F equivalen a',resultado,'°C')
else:
    print('Se ingreso una unidad erronea, ingrese la opcion C para Celsius o la opcion F para Fahrenheit')