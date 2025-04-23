# exlicacion y uso while 

##clave intentos infinitos
# clave=3311
# password=int(input("ingrese su password"))
# while clave!=password:
#     print("error, clave invalida")
#     password=int(input("ingrese su password"))

# print("su clave es correcta")

clave=3311
intentos=3
password=int(input("ingrese su password"))
while clave!=password and intentos<=3:
    intentos-=1
    print("error, clave invalida")
    password=int(input("ingrese su password"))

if intentos>=1:
    print("se han acabado sus intentos")
else:
    print("su clave es correcta")