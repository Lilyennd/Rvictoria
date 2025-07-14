autos={
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
}
# stock tiene el medelo del auto para hacer el cruce entre diccionarios
# cada par de datos tiene el modelo y la cantidad de stock y el precio del mismo,
stock={
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000]  # Este auto no existe en Autos
}

cruce={}
'''
dado los diccionarios anteriores cerar un programa con sl sigueinte menu

'''
while True:
    print('''
    1.- Mostrar stock de cada uno 
    2.- Buscar precio mas alto 
    3.- Actualizar stock 
    4.- Borrar un modelo ( considerar borarr el stock tb)
    5.- Actualizar datos vehiculo
    6.- añadir nuevo auto
    7.- Salir      
        ''')
    op=int(input("que opcion desea elegir?"))
    match op:
        case 1:
            for patente in stock:
                if patente in autos:
                    datosa=autos[patente]
                    datoss=stock[patente]
                    cruce[patente]=datosa+datoss
                elif patente not in autos:
                    datosa=["auto sin modelo"]
                    datoss=stock[patente]
                    cruce[patente]=datosa+datoss
            print("modelo","stock")         
            for patente in cruce:
                print(cruce[patente][0]," (",cruce[patente][-2],")")
        case 2:
            precios=[]
            for i in stock.values():
                precios.append(i[1])
            print(max(precios))
        case 3:
            print("que auto desea actualizar")
            for n,v in stock.items():
                print(n,"(",v[0],")")
            matri=input("indique la patente")
            if matri in stock:
                ns=int(input("indique el nuevo stock"))
                stock[matri][0]=ns
                print("actualizado correctamente")
            else:
                print("matricula no existe")
        case 4:
            print("que auto desea eliminar")
            for n in stock:
                print(n)
            matri=input("indique la patente")
            if matri in stock:
                del stock[matri]
                print("ha sido borrado exitosamente de stock")
            else:
                print("matricula no existe en stock")
            if matri in autos:
                del autos[matri]
                print("ha sido borrado exitosamente de autos")
            else:
                print("matricula no existe en autos")
        case 5:
            print("que auto desea actualizar")
            for n in autos:
                print(n)
            matri=input("indique la patente")
            if matri in autos:
                print("que desea actualzar")
                print("1.-marca: ",autos[matri][0])
                print("2.-año: ",autos[matri][1])
                print("3.-tipo: ",autos[matri][2])
                print("4.-litros: ",autos[matri][3])
                op3=int(input())
                match op3:
                    case 1|3:
                        ans=input("indique el cambio")
                        autos[matri][op3-1]=ans
                        print(autos[matri])
                    case 2|4:
                        ansn=int(input("indique el cambio"))
                        autos[matri][op3-1]=ansn
                        print(autos[matri])
                print("ha sido actualizado exitosamente en autos")
            else:
                print("matricula no existe en autos")
        case 6:
            print("ingrese nuevo auto")
            nm=input("ingrese una nueva matricula")
            nmod=input("ingrese nuevo modelo")
            naño=int(input("ingrese el año"))
            ntipo=input("nuevo tipo")
            nlitros=float(input("ingresar litros"))
            autos[nm]=[nmod,naño,ntipo,nlitros]
            print(autos)
        case 7:
            print("saliendo")
        case _:
            print("opcion no valida")

        

        


        
        

        





            


        
        


