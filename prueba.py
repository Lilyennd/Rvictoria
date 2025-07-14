# Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar nombre de comprador, 
# tipo de entrada y código de confirmación por separado. 
# Para que la compra sea exitosa se debe cumplir lo siguiente:
# a) el nombre de comprador no debe estar repetido,
# b) el tipo de entrada solo permite “G” (General) o “V” (VIP),
# c) el código de confirmación debe tener largo mínimo de 6 caracteres, debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacio en blanco.
# En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
# Al ingresar la opción 2.- Consultar comprador, el menú debe permitir buscar compradores mediante el nombre. Si el comprador existe, debe mostrar los datos asociados: tipo de entrada y código de confirmación. Si no existe, debe mostrar un mensaje indicando que “El comprador no se encuentra.”
# Al ingresar la opción 3.- Cancelar compra, el menú debe permitir eliminar la compra y toda la información asociada mediante el ingreso de un nombre de comprador por teclado. Si la compra se cancela, se debe mostrar “¡Compra cancelada!”, pero si el comprador no existe, se muestra “No se pudo cancelar la compra.”
# Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
def val_nombre(nombre):
    for valor in compradores.values():
        # print(valor["nombre"])
        if valor["nombre"]==nombre:
            print("ya existe ese nombre")
            return False
    return True

def val_tipo(tipo):
    if tipo!="G" and tipo!="V":
        print("tipo solo puede ser G o V")
        return False
    return True

def val_cod(codigo):
    mayu=0
    dig=0
    for l in codigo:
        if l.isupper():
            mayu+=1
        if l.isdigit():
            dig+=1
        if l ==" ":
            return False
    if len(codigo)>0 and mayu>0 and dig>0:
        return True
    else:
        return False

def busqueda(busqueda):
    for valor in compradores.values():
# print(valor["nombre"])
        if valor["nombre"]==busq:
            print("nombre",valor["nombre"])
            print(valor["tipo"])
            print(valor["codec"])
            return True
    return False

aborrar="0"
compradores={"1": {"nombre":"vicky",
                        "tipo":"G",
                        "codec":"aseG12",
                        },
            "2": {"nombre":"v",
                        "tipo":"G",
                        "codec":"aseG32",
                        }
                 }
print('''
      1.- Comprar entrada
      2.- Consultar comprador
      3.- Cancelar compra
      4.- Salir
      ''')
op=int(input("ingrese la opcion"))
match op:
    case 1:
        print("compra de entradas")
        nc=input("ingrese el nombre del comprador")
        nt=input("ingrese el tipo de entrada (G/V)")
        ncod=input("ingrese el codigo (min 1 mayuscula y min 1 numero)")
        if val_cod(ncod) and val_nombre(nc) and val_tipo(nt):
            largo=len(list(compradores))+1
            compradores[largo]={"nombre":nc,
                            "tipo":nt,
                            "codec":ncod,
                            }
            print("se ha ingresado con exito")
    case 2:
        busq=input("ingrese el nombre a buscar")
        if busqueda(busq)== False:
            print("no se encontro el usuario")
    case 3:
        borrar=(input("ingrese el nombre del usuario a cancelar"))
        for b,i in compradores.items():
            if i["nombre"]==borrar:
                aborrar=b
        if aborrar!="0":
            del compradores[aborrar]
            print("se ha borrado")
        else: 
            print("no se encontro")

            

