"""
1. Evalue el siguiente algortimo en Python y explique cual es su funcionamiento. Nota: En caso de tener errores, indique cuales son y adjuntelo corregido. 
"""

int numero = ("Digite número; ")
suma = 0;
    resultado = Falso
x == 1

while x <= numero
suma += x
    x -= 1


if suma % 2 = 0
Print("El resultado final es:, suma, "y es un número par")
else
Print("El resultado final es:",, suma "y no es número par")


"""
SOLUCIÓN:

1. Explicacion de la funcionalidad del algoritmo: este algoritmo pretende recibir un numero entero por parte del usuario, calcular la sumatoria de todos los numeros enteros
positivos hasta el numero ingresado y determinar si la sumatoria obtenida es par o impar.

2. Errores:

- Reemplazar: int numero = ("Digite número; ") por: numero = int(input("Digite numero: "))
- Corregir: suma = 0; de forma que quede: suma = 0 (se elimina el punto y coma)
- 'resultado = Falso' está identado y el string no tiene comillas simples o dobles, esto es erróneo. Se puede eliminar la línea por completo porque la variable "resultado" no es necesaria.
- Corregir la inicialización variable: x == 1 por: x = 1
- En el bloque del while, aplicar los siguientes cambios:
    - Agregar dos puntos a la condicion del while, resultado corregido: while x <= numero:
    - Identar correctamente la linea que sigue: suma += x, para que este dentro del while.
    - Corregir la siguiente linea: x -= 1 por: x += 1. La expresion original impide que se realice una sumatoria pues x decrece.
- En el if, agregar dos puntos a la condicion del if y usar operador de igualdad, resultado final: if suma % 2 == 0:
- Cambiar Print() por print() para ambos print que aparecen en el codigo, no deben llevar mayuscula.
- En el primer print(), identarlo para que quede dentro del if y corregir el argumento: "El resultado final es:, suma, "y es un número par" por: "El resultado final es:", suma, "y es un número par"
- En el else, agregar dos puntos al final, resultado: else:
- En el segundo print(), identarlo para que quede dntro del else y corregir el argumento: "El resultado final es:",, suma "y no es número par" por: "El resultado final es:", suma, "y no es número par"
"""

# Correcion del codigo proporcionado.
numero = int(input("Digite número: "))
suma = 0
x = 1

while x <= numero:
    suma += x
    x += 1


if suma % 2 == 0:
    print("El resultado final es:", suma, "y es un número par")
else:
    print("El resultado final es:", suma, "y no es número par")





"""
2. Una agencia de viajes vende paquetes para cuatro destinos diferentes, “España, Inglaterra, Brazil y Argentina”. 
Cada paquete tiene un valor de 800, 1200, 600 y 800 dólares por persona respectivamente.
Elabore un programa en Python que, mediante un menú solicite el paquete seleccionado, la cantidad de personas que van a viajar y despliegue en pantalla el monto a pagar por el paquete seleccionado.
Es importante considerar que menores de 2 años no pagan tiquete ni hospedaje y que si se viaja en el los meses de Enero, Julio y Diciembre, se le debe aplicar un 10% por “temporada alta”.
El menú debe permitir ingresar únicamente uno de los destinos indicados anteriormente. 
"""

# SOLUCION:

# Precio de los paquetes de viaje por persona.
paquete = 1
precioEspana = 800
precioInglaterra = 1200
precioBrazil = 600
precioArgentina = 800
precioTotal = 0
cantidadPersonas = 0
cantidadMenores = 0
cantidadPersonasFinal = 0
impuestoTemporada = 1.10

# Se solicita el paquete deseado y la cantidad total de viajantes.
paquete = int(input("Ingrese el numero del paquete que desea adquirir (1. Espana, 2. Inglaterra, 3. Brazil, 4. Argentina): "))

if paquete < 1 or paquete > 4:
    print("ERROR: ingrese una opcion de paquete de viajes valida.")

else:
    cantidadPersonas= int(input('Ingrese la cantidad de personas que desean viajar: '))

    # Se consulta si viajan menores de 2 anos y la cantidad. Estos se eliminan del total de personas al calcular el precio total.
    menores = input("¿Se han incluido menores de 2 anos en el total de personas que desean viajar? (si/no) ")
    if menores == "si":
        cantidadMenores = int(input("Ingrese la cantidad de menores de 2 anos que participaran en el viaje: "))
    cantidadPersonasFinal = cantidadPersonas - cantidadMenores

    # Se consulta si el viaje se hara en temporada alta, de ser asi se aplica el 10% adicional.
    temporada = input("¿Desea viajar en Enero, Julio o Diciembre? De ser asi, se aplicara un monto adicional del 10% (si/no) ")

    # Se calcula el precio total dependiendo de la cantidad de personas mayores a 2 anos y el paquete elegido.
    if paquete == 1:
        precioTotal = cantidadPersonasFinal * precioEspana
    elif paquete == 2:
        precioTotal = cantidadPersonasFinal * precioInglaterra
    elif paquete == 3:
        precioTotal = cantidadPersonasFinal * precioBrazil
    elif paquete == 4:
        precioTotal = cantidadPersonasFinal * precioArgentina

    # Se agrega la multa de temporada alta en caso de que aplique.
    if temporada == "si":
        precioTotal *= impuestoTemporada


    print("El precio total del paquete seleccionado es de:", precioTotal,"dolares.")