import os

def reporteA(registroes: dict):
    esnormal = []
    for key, value in registroes.items():
        if 'NORMAL' in value['categoria']:
            esnormal.append(value['nombre'])
    
    if esnormal:
        print('Los estudiantes que se encuentran en la categoría NORMAL son:')
        for nombre in esnormal:
            print(nombre)
    else:
        print('No se encuentra ningún estudiante en la categoría NORMAL')
        
        
def reportB(registroes: dict):
    esobesidad = []
    for key, value in registroes.items():
        if 'OBESIDAD I' in value['categoria']:
            esobesidad.append(value['nombre'])
    
    if esobesidad:
        print('Los estudiantes que se encuentran en la categoría OBESIDAD I son:')
        for nombre in esobesidad:
            print(nombre)
    else:
        print('No se encuentra ningún estudiante en la categoría OBESIDAD I')
        
def reportC(registroes: dict):
    esobesidad2 = []
    for key, value in registroes.items():
        if 'OBESIDAD II' in value['categoria']:
            esobesidad2.append(value['nombre'])
    
    if esobesidad2:
        print('Los estudiantes que se encuentran en la categoría OBESIDAD II son:')
        for nombre in esobesidad2:
            print(nombre)
    else:
        print('No se encuentra ningún estudiante en la categoría OBESIDAD I')
        
def reportD(registroes: dict):
    esobesidad3 = []
    for key, value in registroes.items():
        if 'OBESIDAD III' in value['categoria']:
            esobesidad3.append(value['nombre'])
    
    if esobesidad3:
        print('Los estudiantes que se encuentran en la categoría OBESIDAD III son:')
        for nombre in esobesidad3:
            print(nombre)
    else:
        print('No se encuentra ningún estudiante en la categoría OBESIDAD III')
        
def reportE(registroes: dict):
    esobrepeso = []
    for key, value in registroes.items():
        if 'SOBREPESO' in value['categoria']:
            esobrepeso.append(value['nombre'])
    
    if esobrepeso:
        print('Los estudiantes que se encuentran en la categoría SOBREPESO son: ')
        for nombre in esobrepeso:
            print(nombre)
    else:
        print('No se encuentra ningún estudiante en la categoría SOBREPESO son: ')