# # El programa debe tener un menú de opciones de donde se pueda realizar el pago
# # del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# # una vez sumadas se resten al cupo disponible.
# # Las opciones disponibles deben estar construidas de la siguiente forma:
# # 1. Pago de Tarjeta de Crédito:
# # a. El usuario comienza con una deuda de $100.000
# # b. El usuario puede ingresar un monto para realizar un pago en la
# # tarjeta de crédito.
# # c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# # d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# # la tarjeta.
# # e. Al pagar el sistema debe descontar de la deuda total
# # f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# # saldo de la tarjeta.
# # 2. Simulación de Compras:
# # a. El usuario puede simular realizar un número ilimitado de compras.
# # b. Para cada compra, se solicita al usuario ingresar el monto de la
# # compra. El programa suma los montos de cada compra.
# # c. Se verifica que el monto de la compra sea mayor o igual a cero.
# # d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# # iteración del bucle for.
# # 3. Salir:
# # a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# # A considerar:
# # 1. Manejo de Errores:
# # a. Se utilizan bloques try y except para manejar posibles errores al
# # ingresar datos, validar valores no numéricos y errores inesperados.


# # deuda=100000


# # while True:
# #     try:
# #         print('''
# #             1.- pago de tarjeta de credito
# #             2.- Ingresar nueva compras
# #             3.- Salir
            
# #             ''')
# #         op=(int(input("ingrese su opción")))
# #         match op:
# #             case 1:
# #                 print(f"su deuda es de {deuda}")
# #                 while True:
# #                     try:
# #                         pago=(int(input("cuanto desea pagar de su deuda?"))) 
# #                         break
# #                     except Exception:
# #                         print("Error ingrese una opcion valida")
# #                         if pago>0 and pago<=deuda:
# #                             deuda-=pago
# #                         else:
# #                             print("su monto debe ser mayor a 0 y menor a la deuda total")
# #             case 2:
# #                     while ncompra>=0:
# #                         deudas=deuda
# #                         print(" simular el monto de la nueva compra")
# #                         ncompra=(int(input()))
# #                         deudas+=ncompra
# #                         print(f"su deuda total quedaria {deudas}")
# #                         cho=(int(input('''
# #                                     Desea seguir simulando compras?
# #                                     1.-si - 2.-no
# #                                     ''')))
# #                         if cho==2:
# #                             print("saliendo")
# #                             break                
# #             case 3:
# #                 print("saliendo")
# #                 break
# #             case _:
# #                 print("opcion no valida")
# #     except Exception:
# #         print("ha ocurrido un error inesperado")

# #HACER EN LA CASA

# #ver top de algo
# #hagoque top se inicie como 0
# #luego en la opcion mayor coloco un if top<opmayor osea si top 1
# #entonces top es 


# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# 2
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario



usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
while True:
    try:
        print('''
            1.- iniciar sesión
            2.- registrar usuario
            3.- Salir
            
            ''')
        op=(int(input("ingrese su opción")))
    except Exception:
        print("ERROR")
        match op:

            case 1:
                if usuario1==None or usuario2==None or usuario3==None:
                    print("No existen usuarios en el sistema por favor cree uno")
                nombreu=(input("ingrese su nombre de usuario"))
                passu=(input("ingrese su contraseña "))
                if nombreu==usuario1 and passu==contrasena1 or nombreu==usuario2 and passu==contrasena2 or nombreu==usuario3 and passu==contrasena3:
                    print("bienvenido al sistema")
                    while True:
                        try:
                            print('''
                                     1) Realizar llamada
                                     2) Enviar correo electrónico
                                     3) Cerrar sesión   
                                ''')
                            op=(int(input("ingrese su opción")))
                        except Exception:
                            print("ERROR")

                    
            case 2:
                if usuario1==None:
                     usuario1=(input("ingrese el nombre de usuario"))
                     contrasena1=(input("ingrese el contraseña del usuario"))
                elif usuario2==None:
                     usuario2=(input("ingrese el nombre de usuario"))
                     contrasena2=(input("ingrese el contraseña del usuario"))
                elif usuario3==None:
                     usuario3=(input("ingrese el nombre de usuario"))  
                     contrasena3=(input("ingrese el contraseña del usuario"))  
            case 3:
                print ("saliendo")
                break
            case _:
                print("opcion invalida")