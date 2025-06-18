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



def mostrar_art(lista):
    for n , p in enumerate (lista):
        print(n+1, ".-", p["nombre"],"$", p["precio"])
#se pone la n y la p porque la p es lo que recorre la lista y la n es el numero del indice tipo 1,2,3 etc

def insertar(lista):
    nom=input("ingrese el nombre del producto")
    pre=int(input("ingrese el precio del producto"))
    lista.append({"nombre":nom, "precio":pre})
# el rgumento (lista) luego será reemplazado por la lista que deseamos

def actualizar_lista(lista):
    mostrar_art(lista)
    op=int(input("seleccione una opcion"))
    print(lista[op-1])
    nn=input("ingrese el nombre nuevo")
    np=int(input("ingrese el nombre nuevo"))
    lista[op-1]["nombre"]=nn
    lista[op-1]["precio"]=np
    print("articulo actualizado")

def eliminar(lista):
    mostrar_art(lista)
    opd=int(input("que elemento desea eliminar"))
    lista.pop(opd-1)

prod_college=[

        {"nombre":"lapiz", "precio":200},
        {"nombre":"estuche", "precio":2400}]
prod_sport=[

        {"nombre":"zapato", "precio":20000},
        {"nombre":"pelota", "precio":24000}
]

# prod_sport[0]["nombre"]
# prod_sport.append({"nombre":"paleta", "precio":1000})
#o poner.insert(el indice de la lista)+ diccionarios
def menu(lista):
    while True:
        print('''
    1.- agregar producto
    2.- mostrar productos
    3.- actualizar producto
    4.- borrar producto
    4.- salir
            ''')
        op=int(input("seleccione una opcion"))
        match op:
            case 1:
                insertar(lista)
            case 3:
                actualizar_lista(lista)
            case 4:
                eliminar(lista)
            case 5:
                print("saliendo")
                break
            case _:
                print("seleccion no valida")
####################################################################################################

'''crear programa crud del siguiente diccionario'''

personas={
    1:{"nombre": "vicky",
       "numeros":[392298392839],
       "estadocivil":"soltera",
       "trabajo":True,
       "edad":64},
    2:{"nombre": "vicky",
       "numeros":[392298392839],
       "estadocivil":"soltera",
       "trabajo":True,
       "edad":64},
    3:{"nombre": "vicky",
       "numeros":[392298392839],
       "estadocivil":"soltera",
       "trabajo":True,
       "edad":64}
}

while True:
        print('''
    1.- ingrese persona
    2.- mostrar listado
    3.- actualizar listado
    4.- borrar persona
    5.- salir
            ''')
        op=int(input("seleccione una opcion"))
        match op:
            case 1:
                nombre=input("ingrese el nombre")
                num=int(input("ingrese el numero telefonico"))
                est=int(input('''
                            1.- casado
                            2.- soltero
                          '''))
                if est==1:
                    estcivil="casado"
                else:
                    estcivil="soltero"
                edad=int(input("ingrese la edad"))
                nextkey=len(personas)+1
                personas[nextkey]={"nombre": nombre,
                "numeros":[num],
                "estadocivil":estcivil,
                "trabajo":True,
                "edad":edad}

            case 2:
                for pers , val in personas.items():
                    print (pers, val)
            case 3:
                for pers , val in personas.items():
                    print ( pers, val)
                
                
            case 4:
                for pers , val in personas.items():
                    print ( pers, val)
                nd=int(input("elija por el numero la persona que desea borrar"))
                del personas(nd)
            case 5:
                
                print("saliendo")
                break

            case 6:
                print("saliendo")
                break


            case _:
                print("seleccion no valida")