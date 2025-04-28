
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


#CREAR UN CAJERO AUTOMATICO
# TENER EN CUENTA CAJAS DE BILLETES DE 5MIL,10MIL Y 20MIL
# HAY CAJAS DE 30 BILLETES
# EL USUARIO INGRESA LA CANTIDAD QUE QUIERE RETIRAR Y VERIFICAR SI HAY BILLETES FUFICIENTES, MOSTRAR SALDO DISPONIBLE
# 3 USUARIOS CON SU CLAVE CORRESPONDIENTE
#CADA USUARIO TIENE UNA CLAVE

U1= 1123
U2= 1223
U3= 1233
saldo=0
clave=int(input("ingrese su clave"))