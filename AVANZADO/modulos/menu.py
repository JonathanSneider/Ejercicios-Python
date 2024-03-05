import os
def menu():
    opciones = [1,2,3,4,5]
    titulo = """
    -------------------------------
    +  MENU TORNEO TENIS DE MESA  +
    -------------------------------
    """
    print(titulo)
    opcioness = '1. Registrar jugador\n2. Registrar Partido\n3. Registro detallado de cada jugador\n4. Ganador por categoria\n5. Salir'
    print(opcioness)
    try:
        op = int(input('Seleccione una opcion : '))
    except ValueError:
        print('Ingrese una opcion valida')
        os.system('pause')
        os.system('cls')
        menu()
    else:
        pass
    if op in opciones:
        return op
    else:
        print('Ingrese una opcion Valida')
        os.system('pause')
        os.system('cls')
        menu()

    
    