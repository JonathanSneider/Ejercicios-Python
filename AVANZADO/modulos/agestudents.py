import os
partidos = {}
def aggestudents(partidoss:dict):
    id = int(input('Ingrese la ID del estudiante : '))
    nombreestuden = input('Ingrese el Nombre del estudiante al cual quieres registrar : ')
    categoriaedad = int(input('Ingresa la edad del estudiante : '))
    if ((categoriaedad >= 15) and (categoriaedad <= 16)):
        partidos = {
            'id':id,
            'Nombre':nombreestuden,
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PA': 0,
            'TP': 0,
 
        }
        partidoss['Novato'].update({id:partidos})
    elif ((categoriaedad >= 17) and (categoriaedad <= 20)):
        partidos = {
            'id':id,
            'Nombre':nombreestuden,
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PA': 0,
            'TP': 0,
 
        }
        partidoss['Intermedio'].update({id:partidos})
    elif categoriaedad > 20:
        partidos = {
            'id':id,
            'Nombre':nombreestuden,
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PA': 0,
            'TP': 0,
        }
        partidoss['Avanzado'].update({id:partidos})
    else:
        print('Ingresaste una EDAD no valida')
        print('Intentalo otra vez')
        os.system('pause')
        os.system('cls')
        aggestudents(partidoss)
    