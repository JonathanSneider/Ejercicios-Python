import os
def menu():
    dicopciones = {
        '1': 1,
        '2': 2,
        '3': 3,
    }
    titulo = """
    ++++++++++++++++++++++++++++
    +           MENU           +
    ++++++++++++++++++++++++++++
    """
    print(titulo)
    try:
        opciones = '1. Regristar estudiante\n2. Ver Reportes\n3. Salir'
        print(opciones)
        op = str(input('Seleccione una opcino : '))
        if op not in dicopciones:
            return menu()
                 
    except ValueError:
        print('Dato invalido Intentalo otra vez')
        os.system('pause')
        os.system('cls')
        menu()        
    else:
        return op