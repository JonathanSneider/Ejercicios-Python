import os
import modulos.menu as mn
import modulos.registrociu as re
import modulos.registrosismo as res
import modulos.Buscarsismo as bu
import modulos.Riesgo as ri
sismos = []
if __name__ == "__main__":
    isRunn = True
    while isRunn:
        os.system('cls')
        op = mn.menu()
        if op == 1:
            isrunciu = True
            while isrunciu:
                os.system('cls')
                re.registrociudad(sismos)
                isrunciu = bool(input('Si desea agregar otro equipo presione S(SI) O ENTER(NO) : '))
        if op == 2:
            isrunsis = True
            while isrunsis:
                os.system('cls')
                res.registrosis(sismos)
                isrunsis = bool(input('Si desea registrar otro sismo presione S(SI) O ENTER(NO) : '))
                
        if op == 3:
            isrun3 = True
            while isrun3:
                os.system('cls')
                bu.buscarsismo(sismos)
                isrun3 = bool(input('Presiona ENTER para contiunar'))
                
        if op == 4:
            isrun4 = True
            while isrun4:
                os.system('cls')
                ri.inforiesgo(sismos)
                isrun4 = bool(input('Presiona ENTER para contiunar'))

        if op == 5:
            isRunn = False  