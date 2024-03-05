import os
def menu():
    opciones = [1,2,3,4,5,6]
    titulo = """
    ++++++++++++++++++++++++++++++++++
    +   MENU CONTROL DE PRODUCTOS    +   
    ++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    print('1. Registro de productos\n2. Visualizacion de Productos\n3. Actualizacion de stock\n4. Informe de productos criticos\n5. Calculo de ganancia potencial\n6. Salir')
    try:
        op = int(input('Seleccione una opcion : '))
    except ValueError:
        print('Ingresaste una opcion no validad')
        os.system('pause')
        os.system('cls')
        menu()
    
    else:
        return op