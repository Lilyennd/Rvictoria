
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
# asociar el saldo disponible

U1= 1123
U2= 1223
U3= 1233
S1=140000
S2=280000
S3=190000
caja5=30
caja10=30
caja20=30
b20e=0
b10e=0
b5e=0
r=0
rr=r
clave=int(input("ingrese su clave"))
if clave==U1:
    print(f"su saldo es {S1}")
elif clave==U2:
     print(f"su saldo es {S2}")
elif clave==U3:
    print(f"su saldo es {S3}")
else:
    print("ingrese una clave valida ")
while caja5>0 and caja10>0 and caja20>0:
    print('''
          1.-Retirar dinero
          2.-Consultar saldo
          3.-salir

          ''')
    op=int(input("Selecciones una opcion"))
    if op==1:
        print("cuanto dinero desea sacar (solo multiplos de 5)?")
        r=int(input())
        if r%5!=0:
            print("su monto no es valido, intente con un multiplo de 5")
        while r>=20000 and caja20>0:
            

            r-=20000
            caja20-=1
            b20e+=1


  
  
  
        print("Opcion 2 ")
    elif op==3:
        print("Opcion salir ")
        break
    else:
        print("Seleccione una opcion válida")

