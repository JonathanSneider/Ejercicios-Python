import os
from tabulate import tabulate
def vispro(inventario:dict):
    info = []
    for key,value in inventario.items():
        info.append(value)
        os.system('cls')
        print(tabulate(info,headers="keys",tablefmt='grid'))
