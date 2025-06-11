# #uso y ejemplo d e listas en python

# numeros=[2,5,8,77,6]
# #         0,1,2,3,4
# #        -4,-3,-2,-1
# # print(numeros[4])
# #todas las listas tienen dos indices, el positivo y el negativo, si ahora pongo -1 me mostrara el ultimo

# for numero in numeros:
#     print("numero",numero)


# nombres=["felipe", "larry", "curly", "moe"]
# print(nombres)
# nombres.append("luthien")
# print(nombres)
# #append agrega un elemento al final de la lista
# nombres=[]
# apellido=[]

# while True:
#     op=(int(input('''1.- ingrese nobre y apellido
#                     2.- mostrar nombre completo
#                     3.- buscar nombre
#                     3.- salir
#                 ''')))
#     match op:
#         case 1:
#             nuevo=input("ingrese su nombre: ")
#             nombres.append(nuevo)
#             nuevoa=input("ingrese su apellido: ")
#             apellido.append(nuevoa)
#         case 2:
#             c=0
#             for i in nombres:
#                 print(nombres[c], apellido[c])
#                 c+=1
#         case 3:
#             busca=input("indique que nombre buscara: ")
#             if busca in nombres:
#                 print(f"el nombre {busca} está en la lista")
#             else:
#                 print(f"el nombre {busca} no está en la lista")
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("ingrese una opcion valida")
        
################################################################################################################
# precio=[]
# productos=[cebolla, tomate, lechuga]
# carrito=[1000, 2000, 3000]
# while True:
#     op=int(input('''1.- agregar producto
#                     2.-  entrar a la compra de productos
#                     3.- crear boleta 
#                     4.- salir
#                 '''))
#     match op:
#         case 1: 
#             nuevop=input("ingrese nuevo producto: ")
#             productos.append(nuevop)
#             nuevop1=int(input("ingrese el valor del produco"))
#             precio.append(nuevop1)
#         case 2:
#             for i in range(len(productos)):
#                 p=0
#                 print(p+1,".- ",  productos[i], precio[i])
#             op=int(input())

#TERMINAAAAAAAAR

#####################################################################################################
'''
# append()  añade un elemento al final de la lista 
# min()      muestra el valor menor de la lista
# max()     muestra el valor mayor de la lista
# len()      muestra la cantidad de valores en la lista
# sum()     suma los valores de la lista
# pop()    elimina el ultimo valor o elimina por el indice de la lista
# remove()  elimina algo de la ista por su valor 
# clear()  elimina todo de la lista
# insert()  inserta en la lista segun su indice
# enumerate() enumera la lista en 
# extend()
# sort()
# reverse()

# '''




###################################################################################################
# # Ejemplo de una lista de estudiantes con sus calificaciones
# 1.-INGRESAR NOTA
# 2.-BORRAR NOTA 
# 3.-MOSTRAR NOTAS
# 4.-SACAR PROMEDIO , NOTA MAYOR Y NOTA MENOR
# 5.-LIMPIAR LAS NOTAS
# 6.- SALIR


# nota=[]
# while True:
#     op=int(input('''  
#                         1.-INGRESAR NOTA
#                         2.-BORRAR NOTA 
#                         3.-MOSTRAR NOTAS
#                         4.-SACAR PROMEDIO , NOTA MAYOR Y NOTA MENOR
#                         5.-LIMPIAR LAS NOTAS
#                         6.- SALIR
#                 '''))
#     match op:
#         case 1: 
#             notan=input("ingrese las notas: ")
#             nota.append(notan)
#         case 2:
#             ans=input("desea eliminar la ultima nota añadida?")
#             if ans=="si":
#                 nota.pop()
#         case 3:
#             print("las notas hasta el momento son: ", nota)
#         case 4:
#             suma=sum(nota)
#             prom=suma/len(nota)
#             print("el promedio es:", prom)
#             print("la nota maxima es:", max(nota))
#             print("la meno nota es:", min(nota))
#         case 5:
#             nota.clear()
#         case 6:
#             print("salendo...")
#             break
#         case _: 
#             print("eleccion invalida")


comp=[4,5,7,[3,4],
            [8,9]]
