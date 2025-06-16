
import random
# # op=int(input("seleccione una opcion"))
# # while True:
# #     match op:
# #         case 1:
# #             print("opcion 1")
# #         case 2:
# #             print("opcion 2")
# #         case 3:
# #             print("opcion 3")
# #         case 4:
# #             print("salir")
# #             break
# #         case _:
# #             print("opcion no valida")
# #             break

# def arancel():
#     print("segun el menu eliga la opcion correspondiente a su contexto")
#     print('''
#         1.la florida
#         2.la pintana
#         3.puente alto
#         4.san joaquin
#         ''')
#     op=int(input())
#     if op==1:
#         dsc=0.2
#     elif op==2:
#         dsc=0.3
#     elif op==3:
#         dsc=0.25
#     elif op==4:
#         dsc=0.15
#     else:
#         print("elija una opcion valida")
#     print("elija la cantidad de personas de su grupo familiar")
#     print('''
#         1.1
#         2.2 a 4
#         3.5 o mas
#         ''')
#     op=int(input())
#     if op==1:
#         dsc=0.2
#     elif op==2:
#         dsc=0.3
#     elif op==3:
#         dsc=0.5
#     else:
#         print("elija una opcion valida")

#     arancel-=arancel*dsc 
#     print("usted debera pagar", arancel )

# def azarN():
#     num:random.randint(1,10)
#     return num

# def menutarea():
#     while True:
#         print('''
#             seleccione una opcion
#             1. numero al azar
#             2. calcular arancel
#             3. salir
#             ''')
#         op=int(input())
#         match op:
#             case 1:
#                 print("el numero al azar es", azarN())
#             case 2:
#                 arancel()
#             case 3:
#                 print("saliendo")
#                 break
#             case _:
#                 print("opcion no valida")

#crear menu de carrito con las siguientes opciones:
# 1. INGRESAR NOMBRE DEL CLIENTE
#2. comprar (agregar los productos disponbles)
#3. sacar boleta calcular el precio neto y el precio mas iva. MOSTRAR TOTALES
#4. salir
# consideraciones:
# por lo menos 3 productos
# no hay limi|te de tiempo
# se puede salir en |cualquier momento
# los montos de los productos son fijos
    
# def nombre():
#     name=input("ingrese su nombre")
#     return name 

# def carrito():
#     while True:
#         totalp=0
#         print('''
#             1.galletas de mantequilla     $1500
#             2.cheesecake frambuesa        $3500
#             3.cupcakes chispas chocolate  $2000
#             4.pie de limon                $3000
#             5.rol de canela               $2850
#             6. Salir
#             ''')
#         op=int(input())
#         match op:
#             case 1:
#                 totalp+=1500
#             case 2:
#                 totalp+=3500
#             case 3:
#                 totalp+=2000
#             case 4:
#                 totalp+=3000
#             case 5:
#                 totalp+=2850
#             case 6:
#                 break
#             case _:
#                 print("opcion no valida")
#         return totalp

# def boleta():
#     print("su total es: ", carrito())
#     print("su total con iva es: ", carrito() * 0.19)
#     print("gracias por su compra", nombre())

# while True:
#         print('''
#             seleccione una opcion
#             1. ingresar nombre
#             2. compra productos
#             3. total boleta
#             4. salir
#             ''')
#         opf=int(input())
#         match opf:
#             case 1:
#                 nombre()
#             case 2:
#                 carrito()
#             case 3:
#                 boleta()
#             case 4:
#                 print("saliendo")
#                 break
#             case _:
#                 print("opcion no valida")




#promedio cantidad de alumnos
# pedir cantidad de alumnos
#pedir notas por cada alumno
#promediar cada alumno
#mostrar si aprueba o reprueba
# bonus mostrar promedio de todos los alumnos (curso)

print("ingrese la cantidad de alumnos")
alumnos=int(input())
for i in range(alumnos):
    print("ingrese la cantidad de  notas del alumno", i+1)
    notas=int(input())
    promc=0
    for j in range(notas):
        proma=0
        print(f"ingrese la nota {j+1}, del alumno {i+1}" )
        na=float(input())
        proma+=na/notas
    promc+=proma

if proma>=4:
    print("feliciades, ha aprobado")
elif proma<=4:
    print("<Has reprobado")

print(f"el rpomedio del curso es {promc}")

    

    
2

