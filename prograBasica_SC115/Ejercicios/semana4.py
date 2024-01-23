"""
Ejercicio 1: Desarrolle un programa que calcule el salario de un colaborador.
Si estes inferior a $1000 aplíquele un 15% de incremento.
Si su salario es igual o superior a $1000 no recibe incremento
"""

salario = float(input('Ingrese el salario del colaborador en dolares: '))
if salario < 1000:
    salario *= 1.15

print('El salario final del colaborador en dolares es de:', salario)

"""
Ejercicio 2: Desarrolle un programa que calcule el salario de un colaborador
Si este es superior a $1000 aplíquele un 15% de incremento
De lo contrario aplíquele un 20% de incremento. 
En ambos casos muestre al usuario su nuevo salario.
"""

salario = float(input('Ingrese el salario del colaborador en dolares: '))
if salario > 1000:
    salario *= 1.15
else:
    salario *= 1.20

print('El salario final del colaborador en dolares es de:', salario)

"""
Ejercicio 3: Desarrolle un programa que calcule el salario de un colaborador, según su categoría se le aplica el aumento correspondiente.
Categoría Porcentaje:
1: 10%
2: 12%
3: 15%
4: 20%
"""

salario = float(input('Ingrese el salario del colaborador en dolares: '))
categoria = int(input('Ingrese la categoria del colaborador: '))
if categoria == 4:
    salario *= 1.20
elif categoria == 3:
    salario *= 1.15
elif categoria == 2:
    salario *= 1.12
elif categoria == 1:
    salario *= 1.10

print('El salario final del colaborador en dolares es de:', salario)

"""
Ejercicio 4:
a. Desarrolle un programa que muestre el mayor de dos numeros.
b. Modifique el programa para que funcione para 4 numeros.
"""
# 4.a:
a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))
if a > b:  
    print('El numero mayor es:',a)
elif a < b:
    print('El numero mayor es:',b)
elif a == b:
    print('Los numeros son iguales.')

# 4.b:
a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))
c = float(input('Ingrese el tercer numero: '))
d = float(input('Ingrese el cuarto numero: '))
mayor = a  # Se parte de la premisa de que a es el mayor para simplificar el proceso.

if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
if d > mayor:
    mayor = d

if a == b and b == c and c == d:
    print('Los numeros son iguales.')
else:
    print('El numero mayor es:',mayor)

"""
Ejercicio 5: Desarrolle un programa que ordene de forma descendente 3 números.
Nota: suponga que los numeros son diferentes entre si.
"""

a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))
c = float(input('Ingrese el tercer numero: '))

primero = a
segundo = b
tercero = c

if a > b and a > c and b > c:
    primero = a
    segundo = b
    tercero = c
elif a > b and a > c and b < c:
    primero = a
    segundo = c
    tercero = b
elif a > b and a < c:
    primero = c
    segundo = a
    tercero = b
elif a < b and a < c and c > b:
    primero = c
    segundo = b
    tercero = a
elif a > c and b > a:
    primero = b
    segundo = a
    tercero = c
elif a < c and b > a and b > c:
    primero = b
    segundo = c
    tercero = a

print(primero)
print(segundo)
print(tercero)

"""
Ejercicio 6: Desarrolle un programa que le indique si su año de nacimiento es en año bisiesto.
Considere que un año bisiesto es aquel que es divisible entre 4 pero que no es divisible entre 100,
excepto el que es divisible entre 400.
"""

anio = int(input('Ingrese su anio de nacimiento: '))
if anio % 400 == 0:
    print('Su anio de nacimiento es bisiesto.')
elif anio % 4 == 0 and anio % 100 != 0:
    print('Su anio de nacimiento es bisiesto.')
else:
    print('Su anio de nacimiento no es bisiesto.')
