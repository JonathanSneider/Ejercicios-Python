import os
def menu():
    opciones = ['1','2','3','4','5']
    Titulo = """
    ------------------------
    +         MENU         +
    ------------------------
    """
    print(Titulo)
    opcioness = '1. Registrar Dependencia\n2. Registrar consumo de dependencia\n3. Ver CO2 producido\n4. Dependencia que produce mayor C02\n5. Salir'
    print(opcioness)
    op = input('Seleccione una opcion : ')
    if op not in opciones:
        print('seleccione una opciones valida')
        os.system('pause')
        os.system('cls')
        menu()
    else:
        return op