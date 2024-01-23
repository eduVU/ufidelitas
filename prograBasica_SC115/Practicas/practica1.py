# Ejercicio 1: Elabore un programa en Python que, solicite al usuario un número entero e imprima en pantalla si es un numero par o impar.
numero = int(input('Ingrese un numero entero: '))
if numero%2 == 0:
    print('El numero ingresado es par.')
else:
    print('El numero ingresado es impar.')

"""
Ejercicio 2: Desarrolle un programa en Python para determinar el pago bruto de varios empleados de una empresa.
La empresa paga un “turno ordinario” por las primeras 40 horas trabajadas por cada empleado y paga un “turno y medio” por las demás horas extras trabajadas, después de las primeras 40 horas. 
Su programa debe permitir solicitar la tarifa por hora del empleado, la cantidad de horas trabajadas y desplegar el pago bruto del empleado.  
"""

tarifa = float(input('Ingrese la tarifa por hora en colones que cobra el empleado: '))
horasTotales = float(input('Ingrese la cantidad de horas trabajadas: '))

# Calculo del pago bruto cuando no hay horas extra.
if horasTotales <= 40:
    pagoBruto = tarifa*horasTotales

# Calculo del pago bruto cuando hay horas extra. Las horas extra se cobran como 1.5 veces la tarifa normal.
else:
    horasExtra = horasTotales - 40
    pagoBruto = tarifa*40 + tarifa*1.5*horasExtra

print('El salario bruto del empleado en colones es de:', pagoBruto)

""" 
Ejercicio 3: Elabore un programa en Python que, solicite al usuario el precio de cuatro productos diferentes y tras sumarlos, 
si el monto es mayor a 15 mil colones, le aplique un descuento del 10%, mostrando por pantalla el resultado final al cliente.
"""

producto1 = float(input('Ingrese el precio del primer producto: '))
producto2 = float(input('Ingrese el precio del segundo producto: '))
producto3 = float(input('Ingrese el precio del tercer producto: '))
producto4 = float(input('Ingrese el precio del cuarto producto: '))
montoTotal = producto1 + producto2 + producto3 + producto4

# En caso de que el monto supere los 15 mil, se aplica un 10% de descuento.
if montoTotal > 15000:
    montoTotal *= 0.9

print('El monto total en colones es de:',montoTotal)


"""
Ejercicio 4: La tienda de ropa “Vestimentas OnLine” cuenta con una promoción en las siguientes prendas:
a. Pantalones, si son 2 o más pantalones, aplica un 10% de descuento.
b. Camisas de vestir, si compra 2, la segunda es a mitad de precio.
c. Más de 4 prendas (si son camisas o pantalones, o ambas) un 30% de descuento.

Elabore un programa en Python que, solicite al usuario el tipo de prenda que está comprando, la cantidad de prendas, el monto individual de cada una
y calcule el monto total a pagar con base en los descuentos indicados anteriormente.
"""

descuento = 1  # No hay descuento
cantidad_camisas = int(input('Ingrese la cantidad de camisas compradas: '))
precio_camisas = float(input('Ingrese el precio unitario de las camisas compradas: '))
cantidad_pantalones = int(input('Ingrese la cantidad de pantalones comprados: '))
precio_pantalones = float(input('Ingrese el precio unitario de los pantalones comprados: '))

cantidad_prendas = cantidad_pantalones + cantidad_camisas

# Condicion c: 30% de descuento si lleva 4 o mas prendas.
if cantidad_prendas >= 4:
    descuento = 0.7
    precio_total = (precio_camisas*cantidad_camisas + precio_pantalones*cantidad_pantalones)*descuento
# Condicion a: 10% de descuento si lleva 2 o mas pantalones.
elif cantidad_pantalones >= 2:
    descuento = 0.9
    precio_total = (precio_camisas*cantidad_camisas + precio_pantalones*cantidad_pantalones)*descuento
# Condicion b: si lleva dos camisas la segunda tiene 50% de descuento
elif cantidad_camisas == 2:
    precio_camisas = precio_camisas + precio_camisas/2
    precio_total = precio_camisas + precio_pantalones*cantidad_pantalones
else: 
    precio_total = (precio_camisas*cantidad_camisas + precio_pantalones*cantidad_pantalones)*descuento

print('El total a pagar es de:',precio_total,'colones.')
