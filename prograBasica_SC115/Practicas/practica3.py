"""
Ejercicio 1. Una fábrica de zapatos recibe un pedido de zapatos de forma masiva.
Para llevar un control se requiere elaborar un programa en Python que solicite la cantidad de zapatos a fabricar, el precio de cada zapato fabricado
y al final imprima por cada zapato el monto respectivo. 
Se debe totalizar al final la cantidad de zapatos fabricados y el monto total del pedido. 
Se deben usar funciones y ciclos y no se deben usar funciones de librería.
"""

# ------------------------------------------------------------------
# VERSION DE MARIO
# def obtener_monto(cantidad,valor):
#     return cantidad * valor
  
# def inicio():
#     salir = "s"
#     cantidad_total = 0
#     monto_total = 0
    
#     while salir == "s":
#         salir = input("Desea realizar un pedido. (S/N)  ")
        
#         if salir == "s" or salir == "S":
#             cantidad = int(input("Dijite la cantidad de zapatos a comprar: "))
#             precio = float(input("Dijite el precio por cada zapato:  "))
            
#             monto_total += obtener_monto(cantidad,precio)
#             cantidad_total += cantidad
            
#             print("Detalles del pedido")
            
#             for i in range(cantidad):
#                 print("Zapato",i+1,"precio:", precio)
            
#     print("Total del pedido ", cantidad_total)
#     print("Monto total a pagar ", monto_total)
            
# inicio()


"""
Ejercicio 2. Un supermercado está realizando el inventario de 5 productos en bodega: Arroz, Frijoles, Leche, Macarrones y Salsas.
Elabore un programa en Python que, por cada producto solicite la cantidad de cada uno, y posteriormente imprima el arreglo de cantidades por pantalla.
En cada impresión debe evaluar si la cantidad del producto es menor a 10 unidades, debe indicarle al usuario que debe realizar un pedido de reabastecimiento.
Usar funciones, arreglos y ciclos. Solo lo visto en clase.
"""

# VERSION DE EDDY.
# # Esta función se encarga de solicitar las cantidades de cada producto y agregarlas a la lista.
# def registro_cantidades(nombreProductos, listadoProductos):
#     for i in range(len(listadoProductos)):
#         print('Ingrese la cantidad de', nombreProductos[i],':')
#         listadoProductos[i] = int(input())
#     return listadoProductos

# # Esta funcion muestra en pantalla la cantidad de cada producto.
# def mostrar_inventario(listadoProductos):
#     for i in range(len(listadoProductos)):
#         print('Cantidad de',nombreProductos[i],':',listadoProductos[i])
    
# # Esta funcion verifica si algun producto tiene menos de 10 unidades. Si es asi, indica que debe reabastecerse.
# def comprobar_reabastecimiento(nombreProductos, listadoProductos):
#     for i in range(len(listadoProductos)):
#         if listaProductos[i] < 10:
#             print('Reabastecer', nombreProductos[i])


# # Esta lista contiene el orden elegido para los productos.
# nombreProductos = ['Arroz', 'Frijoles', 'Leche', 'Macarrones', 'Salsas']

# # Esta lista contiene la cantidad de productos en este orden: arroz, frijoles, leche, macarrones y salsas.
# listaProductos = [0,0,0,0,0]

# listaActualizada = registro_cantidades(nombreProductos, listaProductos)
# print('Inventario actual:\n')
# mostrar_inventario(listaActualizada)
# print('\nVerificacion de la cantidad de productos:\n')
# comprobar_reabastecimiento(nombreProductos, listaProductos)

# -----------------------------------------------------------------------------
# VERSION DE JALIESKA
# arroz = 0
# frijoles = 0
# leche = 0
# macarrones = 0
# salsa = 0
# cantidades = [0,0,0,0,0]
# cantidades[0] = int(input("Digite la cantidad de arroz disponible: "))
# cantidades[1] = int(input("Digite la cantidad de frijoles disponible: "))
# cantidades[2] = int(input("Digite la cantidad de leche disponible: "))
# cantidades[3] = int(input("Digite la cantidad de macarrones disponible: "))
# cantidades[4] = int(input("Digite la cantidad de salsa disponible: "))
# productos = ["Arroz", "Frijoles", "Leche", "Macarrones", "Salsas"]
# for i in range(5):     
#      if cantidades[i] < 10:
#           print ("Se debe realizar pedido de reabastecimiento para " + productos[i] + " - Actualmente hay en existencia: " + str(cantidades[i]))
#      else:
#           print ("Para el producto: " + productos[i] + " - Actualmente hay en existencia: " + str(cantidades[i]))
          

"""
Ejercicio 3. Una compañía está elaborando un programa para dispositivos móviles que permita registrar la lista de actividades de una persona durante la semana
y que permita asignar nuevas tareas a cada día de la semana.
Usted ha sido contratado para elaborar un programa en Python que, mediante arreglos (uno dinámico por cada día de la semana), solicite al usuario las actividades
que realiza para cada día y al final imprima en pantalla los arreglos con la cantidad de actividades realizadas.
Se debe usar ciclos, funciones y arreglos. Solo lo visto en clase.
"""

# # Esta funcion se encarga de crear un arreglo de longitud variable con las tareas de un dia de la semana. 
# def registrar_tareas():
#     tareasDiarias = {}
#     cantidadTareas = int(input('Ingrese la cantidad de tareas para este dia de la semana: '))
#     for i in range(cantidadTareas):
#         if i == 0:
#             tareasDiarias[i] = input('\nIngrese la primera actividad del dia: ')
#         elif i == cantidadTareas-1:
#             tareasDiarias[i] = input('Ingrese la ultima actividad del dia: ')
#         else:
#             tareasDiarias[i] = input('Ingrese la siguiente actividad del dia: ')
#     print('\n')
#     return tareasDiarias

# # Esta funcion se encarga de listar todas las tareas de un arreglo dado.
# def listar_tareas(listadoTareas):
#     for i in range(len(listadoTareas)):
#         print(listadoTareas[i])
#     print('\n')


# print('¡Bienvenido(a) al registro de tareas!\n')
# print('Tareas del dia Lunes:\n')
# tareasLunes = registrar_tareas()
# print('Tareas del dia Martes:\n')
# tareasMartes = registrar_tareas()
# print('Tareas del dia Miercoles:\n')
# tareasMiercoles = registrar_tareas()
# print('Tareas del dia Jueves:\n')
# tareasJueves = registrar_tareas()
# print('Tareas del dia Viernes:\n')
# tareasViernes = registrar_tareas()
# print('Tareas del dia Sabado:\n')
# tareasSabado = registrar_tareas()
# print('Tareas del dia Domingo:\n')
# tareasDomingo = registrar_tareas()

# print('Presentacion de resultados:\n')
# print('Dia Lunes: \n')
# listar_tareas(tareasLunes)
# print('Dia Martes: \n')
# listar_tareas(tareasMartes)
# print('Dia Miercoles: \n')
# listar_tareas(tareasMiercoles)
# print('Dia Jueves: \n')
# listar_tareas(tareasJueves)
# print('Dia Viernes: \n')
# listar_tareas(tareasViernes)
# print('Dia Sabado: \n')
# listar_tareas(tareasSabado)
# print('Dia Domingo: \n')
# listar_tareas(tareasDomingo)
