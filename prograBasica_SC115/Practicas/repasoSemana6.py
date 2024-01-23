"""
Ejercicio 1: Elabore un programa en Python que, solicite al usuario los ingresos mensuales, y después de totalizarlos, calcule la cantidad de
meses requeridos para obtener un ahorro de 500 mil colones si por mes se logra ahorrar un 2% del ingreso mensual.
"""

meses = 0
ingreso_mensual_total = 0
ahorro_mensual = 0
objetivo_ahorro = 500000
porcentaje_ahorro = 2
cantidad_ingresos = 0
nuevo_ingreso = 0
total_ingresos = 0

cantidad_ingresos = int(input("Digita la cantidad de ingresos mensuales que desea reportar: "))

for i in range (cantidad_ingresos):
    nuevo_ingreso = float(input('Ingrese el monto del ingreso mensual: '))
    total_ingresos += nuevo_ingreso
    
ahorro_mensual = total_ingresos * porcentaje_ahorro /100
meses = float(objetivo_ahorro / ahorro_mensual)

print('La cantidad de meses necesarios para ahorrar 500000 es:',meses)
    
"""
Ejercicio 2:
Elabore un programa en Python que solicite al usuario el ingreso de un número entero y
posteriormente, mediante un menú permita seleccionar entre realizar una sumatoria
o el factorial de los números, hasta el número ingresado, o bien realizar una cuenta
regresiva por pantalla desde el número ingresado y hasta cero.
"""

suma = 0
factorial = 1

while True :
    num = int(input("Digite un numero entero "))
    
    print("1. Calcular sumatoria")
    print("2. Calcular factorial")
    print("3. Realizar cuenta regresiva")
    opt = int(input("Seleccione una opción (1/2/3): "))

    if opt == 1 :  # Suma
        suma = 0  # Se reinicia la variable.
        for i in range(num+1):
            suma += i
        print("La suma es:",suma)
    
    elif opt == 2 :  # Factorial
        factorial = 1
        if num >= 2:  # El factorial de 0 y 1 es 1. Se estudian los números mayores a uno.
            for i in range(1,num+1):
                factorial *= i
        print("El factorial es:", factorial)                  
            
    elif opt == 3 :  # Cuenta regresiva 
        print("Cuenta regresiva")
        for i in range(0, num+1):
             print(num-i)
    else:
         print("Opción inválida, seleccione 1, 2 o 3 según el menú.")

"""
Ejercicio 3: Elabore un programa en Python que, mediante un menú en pantalla permita al usuario seleccionar entre 5 tipos diferentes de comida y sus respectivos precios.
Una vez seleccionado, se le debe calcular el 13% por concepto de IVA. 
Es importante considerar que el plato de niños cuenta con un 30% de descuento y que puede seleccionar más de un plantillo en la compra.
"""

precio_total = 0
repetir = 'si'

print('Menú de platillos con precio en colones:\n'
      '1. Plato especial: 5000\n'
      '2. Plato ejecutivo: 3000\n'
      '3. Desayuno: 2500\n'
      '4. Almuerzo: 3500\n'
      '5. Plato de ninos: 2000 (tiene descuento del 30% por hoy)\n')

while repetir == 'si':
    platillo = int(input('Ingrese el número del platillo que desea agregar a su compra: \n'))
    if platillo == 1:
        precio_total += 5000
    elif platillo == 2:
        precio_total += 3000
    elif platillo == 3:
        precio_total += 2500
    elif platillo == 4:
        precio_total += 3500
    elif platillo == 5:
        precio_total += (2000*0.7)
    
    repetir = input('¿Desea agregar algún otro platillo a la orden? (si/no): ')

precio_total *= 1.13  # Agregar el IVA a la orden.

print(f'El precio total de la compra es de {precio_total:.2f} colones.\n')  # Resultado redondeado a 2 decimales.