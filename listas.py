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
precio=[]
productos=[]
while True:
    op=int(input('''1.- agregar producto
                    2.-  entrar a la compra de productos
                    3.- crear boleta 
                    4.- salir
                '''))
    match op:
        case 1: 
            nuevop=input("ingrese nuevo producto: ")
            productos.append(nuevop)
            nuevop1=int(input("ingrese el valor del produco"))
            precio.append(nuevop1)
        case 2:
            boleta=0
            p=0
            c=0
            for i in productos:
                print(p+1,".- ",  productos[c], precio[c])
                c+=1
                p+=1
            op=int(input())
