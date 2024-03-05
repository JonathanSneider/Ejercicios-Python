import os
masomenoss = ['+','-']
def actstockk(inventario:dict):
    op = input('Ingrese El codigo del producto al cual le quieres cambiar el stock : ')
    for i, value in inventario.items():
        if op == i:
            masomenos = input('Si quiere agregar stock presiona + si quieres restar stock presion - : ')
            for i in masomenoss:
                if masomenos not in masomenoss:
                    print('Ingresaste una opcion no valida')
                    os.system('pause')
                    os.system('cls')
                    actstockk(inventario)
                else:
                    pass
            if masomenos == '+':
                try:
                    mastock = int(input('Ingrese la cantidad de stock que quiera agregar : '))
                except ValueError:
                    print('Ingresaste un valor invalido intentalo otra vez')
                    os.system('pause')
                    os.system('cls')
                    actstockk(inventario)
                else:
                    inventario[op]['stock'] += mastock
                    break
            elif masomenos == '-':
                try:
                    mastock = int(input('Ingrese la cantidad de stock que quiera quitar : '))
                except ValueError:
                    print('Ingresaste un valor invalido intentalo otra vez')
                    os.system('pause')
                    os.system('cls')
                    actstockk(inventario)
                else:
                    inventario[op]['stock'] -= mastock
                    break
    else:
        print('El Producto no se encuentra registrado')
        os.system('pause')
        

