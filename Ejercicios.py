
# c1 ="Dobby"
# c2 ="Morzat"
# print(f"Primera candidato {c1}")
# cv1=0
# print(f"Segundo candidato  {c2}")
# cv2=0
# Cant=int(input("ingrese cantidad de votantes"))
# for i in range(Cant):
#     voto=int(input("vote 1 por dobby, o 2 por morzat"))
#     if voto==1:
#         cv1+=1
#     elif voto==2:
#         cv2+=1
#     else:
#         print("ERROR")
# print("los votos de dobby son", cv1)
# print("los votos de morzat son", cv2)
# if cv1 > cv2:
#     print("Gano Dobby")
# elif cv1 > cv2:
#      print("Gano Morzat")
# else:
#     print("Es un empate")



#designe dos jugadores solicitando sus nombres
#la pelea es por turno
# cada jugador tiene 50 hp 
#debe mostrar barra de energia
#cada jugador tiene entre 3 y 15 de ataque
#crit de 20%

# import random
# print("ingrese el nombre delos jugadores")
# j1=input("jugador 1")
# j2=input("jugador 2")
# hp1=50
# hp2=50
# turno= random.randint(1,2)
# while hp1>0 and hp2>0:
#     if turno %2==0:
#         print("turno de", j1)
#         ataque=random.randint(3,15)
#         crit=random.randint(1,5)
#         if crit==1:
#             ataque=ataque*2
#             print(" ataque critico")
#         hp2-=ataque
#         print("/"*hp1)
#         print(f"la vida de {j1} es {hp1}")
#         turno+=1
#     else:
#         print("turno de", j2)
#         ataque=random.randint(3,15)
#         crit=random.randint(1,5)
#         if crit==1:
#             ataque=ataque*2
#             print(" ataque critico")
#         hp1-=ataque
#         print("/"*hp2)
#         print(f"la vida de {j2} es {hp2}")
#         turno+=1

# if hp1<=0:
#     print(f"gano {j2}")
# elif hp2<=0:
#     print(f"gano {j1}")


# Crear un cajero automatico
# Tener en cuenta cajas de billetes de 5000 , 10000 y 20000
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave 
# # asociar el saldo disponible
# saldo=0
# U1= 1123
# U2= 1223
# U3= 1233
# # S1=140000
# # S2=280000
# # S3=190000
# caja5=30
# caja10=30
# caja20=30
# b20e=0
# b10e=0
# b5e=0
# clave=int(input("ingrese su clave"))
# if clave==U1:
#     saldo=180000
# elif clave==U2:
#      saldo=280000
# elif clave==U3:
#     saldo=150000
# else:
#     print("ingrese una clave valida ")
# while caja5>0 and caja10>0 and caja20>0:
#     print('''
#           1.-Retirar dinero
#           2.-Consultar saldo
#           3.-salir

#           ''')
#     op=int(input("Selecciones una opcion"))
#     if op==1:
#         r=int(input("cuanto dinero desea sacar (solo multiplos de 5)?"))
#         if r>saldo:
#             print("no tiene salso suficiente")
#         while r %5!=0:
#             print("su monto no es valido, intente con un multiplo de 5")
#             r=int(input())
#         restante=r
#         while restante>=20000 and caja20>0:
#             restante-=20000
#             caja20-=1
#             b20e+=1
#         while restante>=10000 and caja10>0:
#             restante-=10000
#             caja10-=1
#             b10e+=1
#         while restante>=50000 and caja5>0:
#             restante-=10000
#             caja5-=1
#             b5e+=1
#         if restante == 0:
#             saldo -= r
#             print("ha retirado con exito el dinero")
#         else:
#             print("no se puede entregar esa cantidad")
#             caja20 += b20e
#             caja10 += b10e
#             caja5 += b5e
#     elif op==2:
#             print(f"su saldo es {saldo}")




#la florida 20%, la pintana 30%, puente alto 25%, san joaquin 15%
#grupi familiar 1=2%, 2 a 4 = 3%, 5 o mas =4%
# preguntar al u al comuna
# preguntar cuantas personas vive
# es arancel es 20mil
# basado en eso el dexcuento
# totaldsc=0
# arancel=200000
# comuna=input("ingrese su comuna")
# if comuna=="la florida":
#     dsc=20
# elif comuna=="la pintana":
#     dsc=30
# elif comuna=="puente alto":
#     dsc=25
# elif comuna=="san joaquin":
#     dsc=15
# else:
#     print("ingrese una comuna valida")
# familia=int(input("ingrese la cantidad de personas que viven con usted"))
# if familia==1:
#     dsc+=2
# if familia>2 and familia<5:
#     dsc+=3
# if familia>5:
#     dsc+=4
# ####ERROR, ES PARECIDO A LA PRUEBA ASI QUE REVISAR



# print("descuento", dsc)
# totaldsc=dsc/100
# arancel-=arancel*totaldsc
# print("usted debera pagar",arancel )


# print("segun el menu eliga la opcion correspondiente a su contexto")
# print('''
#       1.la florida
#       2.la pintana
#       3.puente alto
#       4.san joaquin
#       ''')
# op=int(input())
# if op==1:
#     dsc=0.2
# elif op==2:
#     dsc=0.3
# elif op==3:
#     dsc=0.25
# elif op==4:
#     dsc=0.15
# else:
#     print("elija una opcion valida")
# print("elija la cantidad de personas de su grupo familiar")
# print('''
#       1.1
#       2.2 a 4
#       3.5 o mas
#       ''')
# op=int(input())
# if op==1:
#     dsc=0.2
# elif op==2:
#     dsc=0.3
# elif op==3:
#     dsc=0.5
# else:
#     print("elija una opcion valida")

# arancel-=arancel*dsc 
# print("usted debera pagar", arancel )


#CLASIFICAR ENTRE CATEGORIA Y PRECIO
#CAT1 +200, CAT2 +400, CAT3 +600
#PRECIOS HASTA 1000, 3%  -  ENTRE 1001 Y 5000, 5% - 5MIL Y MAS ,6% (ESTO SE DESCUNENTA AL TOTAL)
#PONER LISTADO DE 3 PRODUCTOS POR CATEGORIA 
#AGREGAR LOS IMPUESTOS AL PRECIO SEGUN LA CATEGORIA
#APLICAR EL DESCUENTO SEGUN EL TOTAL


# total=0
# print("elija 3 productos por categoria")
# print('''
#       1.reposteria
#       2. frutas
#       3.lacteos
#       ''')
# cat=int(input())

# if cat==1:
#     print('''
#         1. mezclas postres 45
#         2. fondant 60
#         3. chispas chocolate 25
#       ''')
#     op=int(input())
#     if op==1:
#         total+=45+200
#     elif op==2:
#         total+=60+200
#     elif op==3:
#         total+=25+200
# elif cat==2:
#     print('''
#         1. manzana 15
#         2. pera 23
#         3. uva 19
#       ''')
#     op=int(input())
#     if op==1:
#         total+=15+400
#     elif op==2:
#         total+=23+400
#     elif op==3:
#         total+=19+400
# elif cat==3:
#     print('''
#         1. leche 20
#         2. yogurt 12
#         3. helado vainilla 30
#       ''')
#     op=int(input())
#     if op==1:
#         total+=20+600
#     elif op==2:
#         total+=12+600
#     elif op==3:
#         total+=30+600
# else:
#     print("elija una opcion valida")
    

# if total>=1000:
#     total=total*0.97
# elif total>=1001 and total<=5000:
#     total=total*0.95
# elif total>=5001:
#     total=total*0.94

# print("su total es", total)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#clase 05/05


#calcular puntaje de credito
# sedebecalcular que tanto credito tiene una persona
#en cierta entidad financiera debe considerar
# ingresos mensuales, nivel educacional y nacionalidad
# cantidad de ingresos
#500mil a 1palo= 300.000
#1palo a 1.5palos= 650000
#1.5palos o mas = 1.000.000
# nivel educacional
#basico: x1 mediao: x1,3 superior: x1,5
# nacionalidad
# chileno: +300mil , extranjero: +0



# credito=0
# print("elija su rango de ingresos")
# print('''
#       1.500.000 a 1.000.000
#       2. 1.000.001 a 1.500.000
#       3.1.500.000 o superior
#       ''')
# op=int(input())
# if op==1:
#     credito+=300000
# elif op==2:
#      credito+=650000
# elif op==3:
#      credito+=1000000
# else:
#     print("elija una opcion valida")

# print("elija su nivel educacional")
# print('''
#       1.Basica
#       2.Media
#       3.Superior
#       ''')
# op=int(input())
# if op==1:
#      credito*=1
# elif op==2:
#      credito*=1.3
# elif op==3:
#      credito*=1.5
# else:
#     print("elija una opcion valida")

# print("elija su nacionalidad")
# print('''
#       1.Chilena
#       2.Otra
#       ''')
# op=int(input())
# if op==1:
#      credito+=300000
# elif op==2:
#      credito+=0
# print(f"su puntaje de credito es {credito}")



#pedir dia y mes de nacimiento y mostrar el signo zodiacal
#Aries: 21 de marzo al 19 de abril                               21/03 - 19/04
# Tauro: 20 de abril y al 20 de mayo                             20/04 - 20/05
# Géminis: 21 de mayo al 20 de junio
# Cáncer: 21 de junio al 22 de julio
# Leo: 23 de julio al 22 de agosto
# Virgo: 23 de agosto al 22 de septiembre
# Libra: 23 de septiembre al 22 de octubre
# Escorpio: 23 de octubre al 21 de noviembre
# Sagitario: 22 de noviembre al 21 de diciembre
# Capricornio: 22 de diciembre al 19 de enero
# Acuario: 20 de enero al 18 de febrero
# Piscis: 19 de febrero al 20 de marzo








#pida al usuario 2 numeros verificando que el 2do sea mayor
#genere un numero aleatorio entre esos dos numeros 
# imprima la cantidad de veces el simbolor ▄
# import random
# print("ingrese dos digitos, el segundo debera ser mayor al primero")
# N1=(int(input()))
# N2=(int(input()))

# while N1>N2:
#     print("su segundo numero es menor al primero")
#     N2=(int(input()))

# N=random.randint(N1,N2)
# # for i in range (N):
# #     print ("▄")
# print("▄"*N)



#crear un programa que pida la cantidad de ramos 
#pida el promedio por materia
#basado en su promedio final aplicar puntaje de f¿beneficio
#4,5 y 5: 300 - 5.0 y 6.0:500 - 6.1 y 7.0 : 800
#agregar puntaje segun carrera
#tecnico mas +60, ing +40, diplomado +20
# beneficio=0
# prom=0
# c=(int(input("ingrese cantidad de ramos")))
# for i in range (c):
#     materia=(float(input(f"ingrese la nota de la materia {i+1}")))
#     prom+=materia/c
# print("su promedio es",prom)

# if prom>4.5 and prom<5.0:
#     print("su beneficio es de ", 300)
#     beneficio+=300
# elif prom>5.1 and prom<6.0:
#     print("su beneficio es de ", 500)
#     beneficio+=500
# elif prom>6.1 and prom<7.0:
#     print("su beneficio es de ", 800)
#     beneficio+=800
# else:
#     print("no posee beneficios")

# print("defina su carrera")
# print('''
#       1.tecnico
#       2.ingenieria
#       3.diplomado
#       ''')
# op=int(input())
# if op==1:
#     beneficio+=60
# if op==2:
#     beneficio+=40
# if op==3:
#     beneficio+=20

# print(f"su beneficio final es de {beneficio}")


# funcion
