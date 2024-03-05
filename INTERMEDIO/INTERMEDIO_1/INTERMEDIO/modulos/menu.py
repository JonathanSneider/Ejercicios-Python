import os
def menu():
    opcioness = [1,2,3,4,5]
    
    opciones = ['1. Registrar Ciudad','2. Registrar Sismo','3. Buscar sismos por ciudad','4. Informe de riesgo','5. Salir']
    titulo = """
    +++++++++++++++++++++++++++
    +           MENU          +
    +++++++++++++++++++++++++++
    """
    print(titulo)

    for item in opciones:
        print(item)
    try:
        op = int(input('Seleccion una opcion : '))
        if op not in opcioness:
            print('Ingresaste una opcion no valida')
            os.system('pause')
            os.system('cls')
            menu()
    except ValueError:
        print('Error ingresaste una opcion no valida')
        os.system('pause')
        os.system('cls')
        menu()
    else:
        return op
  
        
    
        
    

        
    