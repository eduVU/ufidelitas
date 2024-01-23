# Ejericio 1: Recibir 4 datos e imprimirlos en orden inverso.
a = input('Ingrese el primer dato: ')
b = input('Ingrese el segundo dato: ')
c = input('Ingrese el tercer dato: ')
d = input('Ingrese el cuarto dato: ')
print(d,c,b,a)

# Ejercicio 2: Pedir la edad y calcular su edad en 5 años.
edad = int(input('Ingrese la edad actual: '))
edad += 5
print('Dentro de 5 años tendra:',edad)

# Ejercicio 3: Solicitar los enteros a y b y devolver ((a+b)*2)/3
a = int(input('Ingrese el primer dato: '))
b = int(input('Ingrese el segundo dato: '))
resultado = ((a+b)*2)/3
print('El resultado es:',resultado)

# Ejercicio 4: solicitar un numero y calcular el cuadrado y el cubo del numero.
numero = float(input('Ingrese el numero deseado: '))
cuadrado = numero**2
cubo = numero**3
print(f'El cuadrado de {numero} es {cuadrado} y su cubo es {cubo}.')

# Ejercicio 5: calcular el area y perimetro de un rectangulo dadas su base y altura.
b =float(input('Ingrese la base del rectangulo: '))
h = float(input('Ingrese la altura del rectangulo: '))
area = b*h
perimetro = 2*b + 2*h
print(f'El area del rectangulo es {area} y su perimetro es {perimetro}.')

# Ejercicio 6: Calcular el costo de trasladarse a la U por cuatrimestre dadas la distancia, los dias entre semana y el costo por kilometro.
distancia = float(input('Ingrese la distancia desde su casa a la universidad en km: '))
costo = float(input('Ingrese el costo por kilometro en colones: '))
dias = int(input('Ingrese la cantidad de dias a la semana que visita la universidad: '))
distanciaTotal = 2*distancia  # Considerar que el viaje se calcula como ida y vuelta.
costoDia = costo*distanciaTotal  # Costo completo del viaje ida y vuelta de un dia.
SEMANASCUATRI = 15  # Se asume que el cuatrimestre tiene 15 semanas.
costoTotal = costoDia*dias*SEMANASCUATRI
print(f'El costo total de desplazarse a la U durante el cuatrimestre es de {costoTotal} colones.')

# Ejercicio 7: solicitar la edad de 5 personas y entregar la edad promedio.
edad1 = int(input('Ingrese la primera edad: '))
edad2 = int(input('Ingrese la segunda edad: '))
edad3 = int(input('Ingrese la tercera edad: '))
edad4 = int(input('Ingrese la cuarta edad: '))
edad5 = int(input('Ingrese la quinta edad: '))
promedio = (edad1+edad2+edad3+edad4+edad5)/5
print('El promedio de las edades ingresadas es:',promedio)

# Ejercicio 8: calcular el salario mensual a partir de las horas semanales trabajadas y el precio por hora con deducciones de 10.5% y 5%.
horasSemanales = float(input('Ingrese las horas semanales trabajadas: '))
precioHora = float(input('Ingrese el precio de la hora en colones: '))
SEMANAS = 4.2  # Cantidad de semanas del mes.
DEDUCCIONES = 0.105 + 0.05  # Deducciones totales de 15.5%.
salarioBruto = horasSemanales*precioHora*SEMANAS
salarioMensual = salarioBruto*(1-DEDUCCIONES)
print(f'El salario mensual es de {salarioMensual} colones.')

# Ejercicio 9: solicitar los ingresos mensuales y los gastos mensuales por alimentacion y devolver el porcentaje del total que se destina para ello.
ingresos = float(input('Ingrese sus ingresos mensuales en colones: '))
gastosAlimentacion = float(input('Ingrese sus gastos mensuales por alimentacion en colones: '))
porcentajeAlimentacion = 100*gastosAlimentacion/ingresos
porcentajeRestante = 100 - porcentajeAlimentacion
print(f'Los gastos de alimentacion corresponden a un {porcentajeAlimentacion}% del ingreso total. Queda un {porcentajeRestante}% del salario disponible.')
