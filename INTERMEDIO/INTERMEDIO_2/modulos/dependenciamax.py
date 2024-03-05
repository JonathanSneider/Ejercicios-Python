import os
def verco22(c02:dict):
    numeromax = float('-inf')
    nombre = None
    for keyS, Value in c02.items():
        valor = Value.get('co2total')
        if valor is not None and valor > numeromax:
            numeromax = valor
            nombre =  Value.get('dependencia')
        
    print(f'La dependencia que mas co2 producido fue {nombre} con un total de {numeromax} co2 producido')