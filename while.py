# exlicacion y uso while 

##clave intentos infinitos
# clave=3311
# password=int(input("ingrese su password"))
# while clave!=password:
#     print("error, clave invalida")
#     password=int(input("ingrese su password"))

# print("su clave es correcta")

# clave=3311
# intentos=3
# password=int(input("ingrese su password"))
# while clave!=password and intentos<=3:
#     intentos-=1
#     print("error, clave invalida")
#     password=int(input("ingrese su password"))

# if intentos>=1:
#     print("se han acabado sus intentos")
# else:
#     print("su clave es correcta")


# suma=0
# while True:
#     numero=int(input("ingrese un numero"))
#     if numero==0:
#         break
#     suma+=numero
# print("la suma de los numeros es", suma)

#pida al usuario el limite superior e inferior de un rango y genere un numero al azar dentro de ese numero 
#el segundo numero no puede ser menor

# #aleatorios
# print("ingrese dos numeros")
# l1=int(input("ingrese el limite inferior"))
# l2=int(input("ingrese el limite superior"))
# while l2<l1:
#     print("el limite superior no puede ser menor que el inferior")
#     l2=int(input("ingrese el limite superior"))
    
# import random
# numero=random.randint(l1,l2)
# print("el numero es", numero)


#limite entre 1,50
#ir dando pitas sobre el numero
# mayor o menor


# import random
# resp=random.randint(1,50)
# print(resp)
# intentos=0
# answ=int(input("ingrese un numero entre 1 y 50")) 
# while answ!=resp:
#     intentos+=1
#     if intentos==5:
#         print("se han acabado sus intentos")
#         break
#     if answ>resp:
#         print("el numero que bsucas es menor")
#     else:
#         print("el numero que buscas es mayor")
#     answ=int(input("ingrese un numero entre 1 y 50"))