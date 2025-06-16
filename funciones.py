# # funciones

# def suma(n1,n2):
#     print(n1+n2)
    

# def resta(n1,n2):
#     print(n1-n2)


# def multiplicacion(n1,n2):
#     print(n1*n2)

# def division(n1,n2):
#     try:
#         print(n1/n2)
#     except ZeroDivisionError:
#         print("No se puede dividir entre cero")
    


# while True:
#     num1=(int(input("ingrese un numero")))
#     num2=(int(input("ingrese un numero")))
#     op=int(input('''seleccione una opcion
#             1. suma
#             2. resta
#             3. multiplicacion
#             4. division         
             
#              '''))
#     match op:
#         case 1:
#             print("suma")
#             suma(num1,num2)
#         case 2:
#             print("resta")
#             resta(num1,num2)
#         case 3:
#             print("multiplicacion")
#             multiplicacion(num1,num2)
#         case 4:
#             print("division")
#             division(num1,num2)
#         case _:
#             print("opcion no valida")
#             break

# def suma_return():
#     num1=(int(input("ingrese un numero")))
#     num2=(int(input("ingrese un numero")))
#     return num1+num2

# print(suma_return())
# #el return nos deja manipular lo que resulta de la funcion

# def promedio(x,y,z):
#     return (x+y+z)/3

# crear un programa para calcular un descuento
# pedir al usuario el precio y el descuento a aplicar
# mostrar los resultados

# def dsc(n1,n2):
#     return n1*(n2/100)



# p=(int(input("ingrese el precio del producto")))
# d=(int(input("ingrese el descuento del producto")))

# print("el descuento es", dsc(p,d))
# print("el precio final es", p-dsc(p,d))


# def milis():
#     dato=(input)

producto=["Zapato"]
precio=[20000]
list_prod=[

        {"nombre":"zapato", "precio":20000},
        {"nombre":"pelota", "precio":24000}
]

# list_prod[0]["nombre"]
# list_prod.append({"nombre":"paleta", "precio":1000})
#o poner.insert(el indice de la lista)+ diccionarios

i=0
while True:
    print('''
1.- agregar producto
2.- mostrar productos
3.- actualizar producto
4.- salir
          ''')
    op=int(input("seleccione una opcion"))
    match op:
        case 1:
            nom=input("ingrese el nombre del producto")
            pre=int(input("ingrese el precio del producto"))
            list_prod.append({"nombre":nom, "precio":pre})

        case 2:
            for p in (list_prod):
                print (p)
        case 3:
            for p in range(len(list_prod)):
                
                print(i+1,".- ", list_prod[i])
                i+=1
            op=int(input("seleccione una opcion"))
            print(list_prod[op-1])
            nn=input("ingrese el nombre nuevo")
            np=int(input("ingrese el nombre nuevo"))
            list_prod[op-1]["nombre"]=nn
            list_prod[op-1]["precio"]=np
            print("articulo actualizado")
        case 4:
            print("saliendo")
            break
        case _:
            print("seleccion no valida")
