import os
inventarios = {}
def registropro(inventario:dict):
    try:
        codigo = input('Ingresa el codigo del producto : ')
        nombre = input('Ingresa el Nombre del producto : ')
        vcompra = int(input('Ingrese el valor de Compra : '))
        valordventa = int(input('Ingrese el valor de venta : '))
        sotckmin = int(input('Ingrese el stock minimo permitido : '))
        stockmax = int(input('ingrese el sotck maximo permitido : '))
        nomprov = input('ingrese el nombre del provedor del producto :')
    except ValueError:
        print('Ingresaste un Valor no valido Intentalo otra vez')
        os.system('pause')
        os.system('cls')
        registropro(inventario)

    inventarios = {
        'codigo' : codigo,
        'nombre' : nombre,
        'valorcompra' : vcompra,
        'valorventa' : valordventa,
        'stock' : 0,
        'stockmin' : sotckmin,
        'stockmax' : stockmax,
        'provedor' : nomprov,
    }
    inventario.update({codigo:inventarios})




