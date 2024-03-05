import os
from tabulate import tabulate
def tablaa(partidoss:dict):
    print('---------------')
    print('-Novato')
    print('-Intermedio')
    print('-Avanzado')
    print('---------------')
    op = input('Ingrese la categoria de la cual quieres mirar la tabla : -').lower().capitalize()
    if op == 'Novato':
        info = []
        for key,value in partidoss['Novato'].items():
            info.append(value)
            os.system('cls')
            print(tabulate(info,headers="keys",tablefmt='grid'))  
    elif op == 'Intermedio':
        info = []
        for key,value in partidoss['Intermedio'].items():
            info.append(value)
            os.system('cls')
            print(tabulate(info,headers="keys",tablefmt='grid'))  
    elif op == 'Avanzado':
        info = []
        for key,value in partidoss['Avanzado'].items():
            info.append(value)
            os.system('cls')
            print(tabulate(info,headers="keys",tablefmt='grid'))
    