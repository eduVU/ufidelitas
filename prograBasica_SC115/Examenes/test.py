
archivoOriginal = open('Personas.csv','r')
arregloDatos = []  # Este arreglo almacenará la matriz que se obtiene a partir de los datos del archivo original.
encabezado = True
lista1 = ['Edad','Estatura']  # Nuevas columnas de la matriz
lista2 = ['0','0']  # Nuevas columnas de la matriz
for linea in archivoOriginal:
    arregloDatos.append(linea.split(',')+lista1)  # Cada línea se agrega como una fila a la matriz, que contiene 5 columnas con los valores separados por coma del archivo + 2 adicionales.
print(arregloDatos)


