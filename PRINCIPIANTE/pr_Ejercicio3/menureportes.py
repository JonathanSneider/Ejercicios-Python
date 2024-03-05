import os
def reportes():
    reportess = {
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
    }
    titulo = """
    +++++++++++++++++++++++++++++
    +       MENU REPORTES       +
    +++++++++++++++++++++++++++++
    """
    print(titulo)
    
    try:
        opciones = 'A. Cuantos estudiantes se encuentran en el peso ideal.\nB. Cuantos estudiantes se encuentran en obesidad grado I.\nC. Cunatos estudiantes se encuentran en obesidad grado II.\nD. Cuantos estudiantes se encuentran en obsesidad grado III.\nE. Cuantos estudiantes se encuentran en Sobrepeso.\nF. Salir'
        print(opciones)
        op = str(input('Seleccione una opcion : ')).upper()
        if op not in reportess:
            print('La opcion que ingresaste no es valida')
            return reportes()
    except ValueError:
        print('La opcion que ingresaste no es valida')
        os.system('pause')
        os.system('cls')
        reportes()
    else:
        return op
    