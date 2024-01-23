# Ejercicio 1: mensaje de bienvenida para el usuario segun su nombre y apellido.
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese sus apellidos: ')
print('Bienvenido, estimado',nombre,apellido)

# Ejercicio 2: calcular la suma, resta, multiplicacion y division de dos numeros dados.
a = float(input('ingrese el primer numero: '))
b = float(input('ingrese el segundo numero: '))
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
print('Resultados para los numeros dados:\n'
      f'Suma: {suma}\n' 
      f'Resta: {resta}\n'
      f'Multiplicacion: {multiplicacion}\n'
      f'Division: {division}\n')

# Ejercicio 3: calcular area y perimetro de un cuadrado.
lado = float(input('Ingrese la base del rectangulo: '))
area = lado**2
perimetro = 4*lado
print(f'El area del cuadrado es {area} y su perimetro es {perimetro}.')

# Ejercicio 4: Obtener las edades de Pedro y Luis e intercambiarlas.
edadPedro = input('Ingrese la edad de Pedro: ')
edadLuis = input('Ingrese la edad de Luis: ')
print(f'La edad de Pedro ahora es {edadLuis} y la edad de Luis ahora es {edadPedro}.')

# Ejercicio 5: Pedir un numero y elevarlo a una potencia dada.
base = float(input('Ingrese el numero que desea trabajar: '))
exponente = float(input('Ingrese el valor del exponente: '))
resultado = base**exponente
print('El resultado es:',resultado)
