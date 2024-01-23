import matplotlib.pyplot as plt
import numpy as np

dominio = np.linspace(0,1600, num=1601)  # Dominio de las funciones lineales especificadas: [0,1500]
unos = np.ones(1601)

f1 = 20*dominio + 5000*unos  # Equivale a f(x) = 20x + 5000
f2 = (260/15)*dominio + 6500*unos  # Equivale a f(x) = (260/15)x + 6500

# Graficar la funcion f1.
valorMaximo = 1600
plt.title("Tarifa telefónica en colones en función a los minutos de llamada")
plt.xlabel("Cantidad de minutos de llamada") 
plt.ylabel("Tarifa [colones]") 
plt.plot(dominio,f1,label='f(x)=20x+5000')
plt.scatter(dominio[valorMaximo],f1[valorMaximo],color='black',label='Tarifa máxima: 37000')
plt.legend()
plt.grid()
plt.show()

# Graficar la funcion f2.
valorMaximo = 1600
plt.title("Tarifa telefónica en colones en función a los minutos de llamada")
plt.xlabel("Cantidad de minutos de llamada")
plt.ylabel("Tarifa [colones]")
plt.scatter(dominio[valorMaximo],f2[valorMaximo],color='black',label='Tarifa máxima: 34233.33')
plt.plot(dominio,f2,label='f(x)=(260/15)x+6500',color = 'r')
plt.legend()
plt.grid()
plt.show()

# Graficar las 2 funciones en el mismo eje.
puntoInterseccion = 562

plt.title("Comparación de los modelos de tarifa telefónica") 
plt.xlabel("Cantidad de minutos de llamada") 
plt.ylabel("Tarifa [colones]")
plt.scatter(dominio[puntoInterseccion],f1[puntoInterseccion],color='black',label='Punto de intersección: (562.5, 16250)')
plt.plot(dominio,f1,label='f(x)=20x+5000')
plt.plot(dominio,f2,label='f(x)=(260/15)x+6500',color='r')
plt.grid()
plt.legend()
plt.show()
