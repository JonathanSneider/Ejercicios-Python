import os
numeros = []
def ej4(numeross:list):
    isruna = True
    while isruna:
        try:
            n = int(input('Ingrese un numero entero positivo : '))
            if n < 0:
                pass
            else:
                numeross.append(n)
        except ValueError:
            print('Ingrese un numero valido')
            os.system('pause')
            ej4(numeross)
        
        if n < 0:
            os.system('cls')
            a = len(numeross)
            if a == 0:
                pass
            else:
                print(f'Los numeros ingresasdo en total fueron : {a}')
            isruna = False
            numpartol = 0
            for value in numeross:
                if value % 2 == 0:
                    numpartol += 1
            if numpartol == 0:
                pass
            else:
                print(f'El numero total de pares ingresados fueron : {numpartol}')
            totalpar = 0
            for value in numeross:
                if value % 2 == 0:
                    totalpar += value
            if numpartol == 0:
                pass    
            else:
                totalc = totalpar / numpartol
                print(f'El promedio de los numeros pares es : {totalc}')
            totalimpar = 0
            impartnums = 0
            for value in numeross:
                if value % 2 != 0:
                    impartnums += 1
                    totalimpar += value
            if impartnums == 0:
                pass    
            else:
                totalcm = totalimpar *1000 // impartnums / 1000
                print(f'El promedio de los numeros impares es : {totalcm}')
            numen10 = 0
            numen2050 = 0
            numen100 = 0
            for value in numeross:
                if value < 10:
                    numen10 += 1
                if ((value >= 20) and (value<= 50)):
                    numen2050 += 1
                if value > 100:
                    numen100 += 1
            if numen10 == 0:
                pass
            else:
                print(f'El total de numeros menores que 10 es : {numen10}')
            if numen2050 == 0:
                pass
            else:
                print(f'El total de numeros entre 20 y 50 es : {numen2050}')
            if numen100 == 0:
                pass
            else:
                print(f'El total de numeros mayores a 100 es : {numen100}')
            



ej4(numeros)       





    
       

