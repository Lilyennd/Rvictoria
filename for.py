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

# Algoritmo votos
# 	Escribir "ingrese un numero de votantes"
# 	Leer num
	
# 	kaiser=0
# 	nose=0
	
# 	Para i<-1 Hasta num Con Paso 1 Hacer
# 		Escribir "ingrese su voto: Kaiser 1, Nose 2"
# 		Leer voto
# 		Si voto==1 Entonces
# 			kaiser=kaiser+1
# 		SiNo
# 			Si voto==2 Entonces
# 				nose=nose+1
# 			SiNo
# 				Escribir "Error, selecione un voto válido"
# 			Fin Si
# 		Fin Si
# 	Fin Para
# 	Escribir "los votos de Kaiser son ",kaiser
# 	Escribir "los votos de Nose son ",nose
# 	Si kaiser>nose Entonces
# 		Escribir "Gano Kaiser"
# 	SiNo
# 		Escribir "Gano Nose"
# 	Fin Si
# FinAlgoritmo
print("Primera candidata Dobby")
Dobby=0
print("Segundo candidato Morzat")
Morzat=0
Cant=int(input("ingrese cantidad de votantes"))
for i in range(Cant):
    voto=int(input("vote 1 por dobby, o 2 por morzat"))
    if voto==1:
        Dobby+=1
    elif voto==2:
        Morzat+=1
    else:
        print("ERROR")
        print("los votos de dobby son", Dobby)
        print("los votos de morzat son", Morzat)
        if Dobby > Morzat:
            print("Gano Dobby")
        elif Morzat > Dobby:
            print("Gano Morzat")
        else:
            print("Es un empate")


