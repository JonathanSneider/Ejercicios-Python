import os
def wincat(partidoss:dict):
    numeromax = float('-inf')
    nombre = ''
    numeromaxInt = float('-inf')
    nombreInt = ''
    numeromaxAv = float('-inf')
    nombreAv = ''
    PuntosA = ''
    PuntosAint = ''
    PuntosAAV = ''
    
    for key, value in partidoss['Novato'].items():
        valor = value.get('TP')
        PuntosAs = value.get('PA')
        if valor is not None and valor > numeromax:
            numeromax = valor
            nombre = value.get('Nombre')
            PuntosA = PuntosAs
            
        if valor is not None and valor == numeromax:
            if PuntosAs > PuntosA:
                nombre = value.get('Nombre')
                numeromax = valor
                
            else:
                pass     
    for key, value in partidoss['Intermedio'].items():
        valor = value.get('TP')
        PuntosAss = value.get('PA')
        if valor is not None and valor > numeromaxInt:
            numeromaxInt = valor
            nombreInt = value.get('Nombre')
            PuntosAint = PuntosAss
            
        if valor is not None and valor == numeromaxInt:
            if PuntosAss > PuntosAint:
                nombreInt = value.get('Nombre')
                numeromaxInt = valor
                
            else:
                pass     
            
    for key, value in partidoss['Avanzado'].items():
        valor = value.get('TP')
        PuntosAsss = value.get('PA')
        if valor is not None and valor > numeromaxAv:
            numeromaxAv = valor
            nombreAv = value.get('Nombre')
            PuntosAAV = PuntosAsss
            
        if valor is not None and valor == numeromaxAv:
            if PuntosAsss > PuntosAAV:
                nombreAv = value.get('Nombre')
                numeromaxAv = valor
                
            else:
                pass  
            
    print(f'Novato : {nombre} con un total de {numeromax} Puntos')
    print(f'Intermedio : {nombreInt} con un total de {numeromaxInt} Puntos')
    print(f'Avanzado : {nombreAv} con un total de {numeromaxAv} Puntos')