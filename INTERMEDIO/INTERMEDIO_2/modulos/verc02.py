import os
def verco2(c02:dict):
    for key,value in c02.items():
        print(f'{key} : {c02[key]["co2total"]} CO2 producido')
    