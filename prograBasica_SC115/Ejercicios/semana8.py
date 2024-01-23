"""
Ejercicio 1: Desarrolle un programa que convierta un número a su respectivo valor en base binaria, octal y hexadecimal.
Cada una de las conversiones debe ser un proceso independiente. 
El proceso binario debe mostrar el resultado, los otros dos procesos deben retornar el resultado para ser mostrado desde el proceso inicial.
Adicionalmente, programe un proceso que reciba dos parámetros (el valor y la base) y que muestre el número correspondiente.
"""

def convertirBinario(numero):
    numero_binario = ""
    cociente = numero
    while cociente > 0:
        numero_binario += str(cociente%2)
        cociente //=2
    print("El número", numero," en binario es:", numero_binario[::-1])

def convertirOctal(numero):
    numero_octal = ""
    cociente = numero
    while cociente > 0:
        numero_octal += str(cociente%8)
        cociente //=8
    return numero_octal[::-1]

def convertirHexadecimal(numero):
    numero_Hexa = ""
    cociente = numero
    while cociente > 0:
        if cociente%16==10:
            numero_Hexa+="A"
        elif cociente%16==11:
            numero_Hexa+="B"
        elif cociente%16==12:
            numero_Hexa+="C"
        elif cociente%16==13:
            numero_Hexa+="D"
        elif cociente%16==14:
            numero_Hexa+="E"
        elif cociente%16==15:
            numero_Hexa+="F"
        else:
            numero_Hexa += str(cociente%16)
        cociente //=16
    return numero_Hexa[::-1] 

numero = int(input("Ingrese el numero a convertir: "))
convertirBinario(numero)
print("El número", numero," en octal es:",convertirOctal(numero))
print("El número", numero," en Hexadecimal es:",convertirHexadecimal(numero))