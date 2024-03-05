import os

def sumanumeros():
    num1 = input('Ingrese el primer numero que desea sumar : ')
    num2 = input('Ingrese el segundo numero que desea sumar : ')
    num3 = input('Ingrese el tercer numero que desea sumar : ')
    
    if num1.isdigit() and int(num1) > 0 and num2.isdigit() and int(num2) > 0 and num3.isdigit() and int(num3) > 0:
        resultado = int(num1) + int(num2) + int(num3)
        print(f'El resultado de la suma de los 3 numeros es {resultado}')
    else: 
        print('Ingresaste un numero invalido intentalo otra vez')
        os.system('pause')
        os.system('cls')
        sumanumeros()

sumanumeros()

        
    
    


