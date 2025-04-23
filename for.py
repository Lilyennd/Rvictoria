# # repeticion con pedido del numero
# num1=int(input("ingrese un numero"))
# for i in range(num1):
#     print("repeticion", i+1)    


# # pide un numero al usuario y muestra la tabla a ese numero

# num=int(input("ingrese un numero"))
# for i in range(10):
#     print(num, "x",i+1, "=", (i+1)*num)

# #las 10 tablas de multiplicar

# for j in range(10):
#     for i in range(10):
#         print(j+1, "x",i+1, "=", (i+1)*(j+1) )

# #pedir al usuario ingresar notas y sacar el promedio

# cant=int(input("ingrese el numero de notas"))
# suma=0
# for i in range (cant):
#     print("ingrse nota", i+1)
#     nota=(int(input( )))
#     # suma+=nota
#     suma=suma+nota
#     prom=suma/cant
# print ("el promedio es", prom)


# #pedir cant de alumnos, y luego la cantidad de notas por alumno
# #mostrar el prmedio de cada uno

# print("ingrese la cantidad de alumnos")
# Cant=int(input())
# for j in range (Cant):
#     print("ingrese el numero de notas del alumno", j+1)
#     cant=int(input())
#     suma=0
#     for i in range (cant):
#         print("ingrese nota", i+1, "del alumno ", j+1)
#         nota=int(input( ))
#         # suma+=nota
#         suma=suma+nota
#         prom=suma/cant
#     print ("el promedio es", prom)
#     if prom>=4:
#         print("usted aprobo")
#     else:
#         print("usted reprobo")


# # pida al usuario un numero y sume todos los digitos anteriores
# suma=0
# rango=int(input("ingrese un numero"))
# for i in range(rango):
#     suma+=i
#     print("la suma de los numeros anteriores es", suma)


# pida al usuario la cantidad de numeros  y verifique que cada uno sea par o impar

# Cant=int(input("cuantos numeros desea verificar?"))
# for i in range(Cant):
#     print("insgrese un numero")
#     num=int(input())
#     if num%2==0:
#         print("su numero es par")
#     else:
#         print ("su numero es impar")


# Cant=int(input("hasta que numero desea verificar?"))
# for i in range(Cant):
#     i+=1
#     if i%2==0:
#         print("su numero es par")
#     else:
#         print ("su numero es impar")


# hola="chao"
# for i in hola:
#     print (i)
# voc=0
# wo=input("ingrese una palabra")
# for i in wo:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         print(i)
#         voc+=1
# print("la cantidad de vocales es", voc)

# wo=input("ingrese una palabra")
# voc=0
# ca=0
# co=0
# for i in wo:
#     if i.lower() in "aeiou":
#         voc+=1
#     elif i!= "aeiou" or " ":
#         ca+=1   
# print("la cantidad de vocales es", voc)
# print("la cantidad de caracteres es", ca)

#numero par - impar con contador
# cant=int(input("ingrese un numero"))
# imp=0
# par=0
# for i in range(cant):
#     if (i+1) %2==0:
#         print(f"el numero {i+1} es par")
#         par+=1
#     elif i %2==1:
#         print(f"el numero {i+1} es par")
#         imp+=1
# print(f"la cantidad de numeros pares es {par}")
# print(f"la cantidad de numeros impares es {imp}")


# #supermercado
# #preguntar al usuario cuantos prductos lleva,
# #  el listado de 3 productos, 
# # el total neto de la compra 
# # el valor con iva
# cant=int(input("ingrese cantidad e productos:"))
# total=0
# for i in range (cant):
#     print('''
#         "1.- Diazepam $9000"
#         "2.- Metametozona $18500"
#         "3.- Oblea China $1000"
#         ''')
#     op=int(input())
#     if op==1:
#         print("Usted lleva dIAZEPAM")
#         total+=9000
#     elif op==2:
#         print("usted lleva Metametozona")
#         total+=18500
#     elif op==3:
#         print("usted lleva Oblea China")
#         total+=1000
#     else:
#         print("error")

# print("Su total neto es" , total)
# print("Su total con iva agregado es" , total*1.19)
      