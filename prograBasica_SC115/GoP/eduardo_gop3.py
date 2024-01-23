"""
Ejercicio 1. Solicitar una cadena de caracteres al usuario y una letra específica y mediante funciones
y ciclos muestre en pantalla la cantidad de veces que aparece el carácter en la cadena de caracteres.
"""

def encontrar_caracteres(palabra, caracter):
    contador = 0
    for letra in palabra:
        if letra == caracter:
            contador += 1
    return contador


palabra = input('Ingrese la palabra que desea revisar: ')
caracter = input('Ingrese la letra o caracter que desea encontrar dentro de la palabra dada: ')
contador = encontrar_caracteres(palabra, caracter)
print('El caracter '+caracter+', aparece', contador,'veces en la palabra.')

"""
Ejercicio 2. Solicitar una cadena de caracteres al usuario y mediante una función propia devuelva el tamaño de la cadena.
Investigar el caracter “\n” para finalizar una cadena de caracteres.
"""

def contar_caracteres(palabra):
    contadorLetras = 0
    for letra in palabra:
        contadorLetras += 1
    return contadorLetras

string = input('Ingrese una cadena de caracteres: ')
longitud = contar_caracteres(string)
print('El string dado tiene', longitud,'caracteres.\n')

# NOTA: El uso de \n al final de una cadena de caracteres permite hacer un salto de linea.

"""
Ejercicio 3. Solicitar una cadena de caracteres al usuario, y solicite una posición inicial y una posición final y devuelva el
contenido de la cadena de caracteres que se encuentra entre ambas posiciones. 
Considere validar las posiciones solicitadas para que efectivamente pertenezcan a la cadena de caracteres.
"""

# Esta funcion revisa las posiciones iniciales y finales dadas por el usuario y verifica que cumplan con los requisitos para que
# el programa trabaje de la manera esperada.
def revisar_datos(string, inicio, final):
    estado = 'error'
    if inicio > final:  # Comprobar que el inicio no sea mayor al final.
        print('Error: la posicion inicial no puede ser mayor a la posicion final.')
    elif inicio < 0 or final < 0:  # Comprobar que el inicio o el final no sean menores a 0.
        print('Error: ninguna de las posiciones dadas puede ser menor a cero.')
    elif inicio > len(string) - 1 or final > len(string) - 1:   # Comprobar que las posiciones inicio/fin no sobrepasen el largo de la cadena de caracteres.
        print('Error: las posiciones dadas no pueden sobrepasar el largo de la cadena de caracteres.')
    else:
        estado = 'ok'
    return estado

# Esta funcion devuelve el contenido de la cadena de caracteres que se encuentra dentro de las posiciones dadas.
def recortar_string(string, inicio, final):
    resultado = ''
    for i in range(inicio, final+1):
        resultado = resultado + string[i]
    return resultado

cadena = input('Ingrese una cadena de caracteres: ')
posicionInicial = int(input('Ingrese la posicion inicial (de 0 en adelante): '))
posicionFinal = int(input('Ingrese la posicion final: '))

revision = revisar_datos(cadena, posicionInicial, posicionFinal)
if revision == 'ok':
    nuevaCadena = recortar_string(cadena, posicionInicial, posicionFinal)
    print('Resultado:'+nuevaCadena)