import os
co22 = {}
def importdep(C02:dict):
    nombredep = input('Ingrese el nombre de la dependencia la cual desea registrar : ')
    oficinas = int(input(f'ingrese la cantidad de oficinas de la dependencia {nombredep} : '))
    co22 = {
        'dependencia' : nombredep,
        'oficinas' : oficinas,
        'co2km' : 0,
        'co2kwhmm' : 0,
        'co2total' : 0,

        
    }
    C02.update({nombredep:co22})