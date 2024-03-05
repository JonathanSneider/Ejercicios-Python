import os
import modulos.menu as mn
import modulos.agestudents as ads
import modulos.adMatch as ad
import modulos.tabla as tb
import modulos.wincat as win
partidos = {
    'Novato':{},
    'Intermedio':{},
    'Avanzado':{},
    }
if __name__ == "__main__":
    Isrun = True
    while Isrun:
        os.system('cls')
        op = mn.menu()
        if op == 1:
            isrun1 = True
            while isrun1:
                os.system('cls')
                ads.aggestudents(partidos)
                isrun1 = bool(input('Si desea registrar a otro jugador presiona S(SI) o ENTER(NO) : '))
        if op == 2:
            isrun2 =  True
            while isrun2:
                os.system('cls')
                ad.admatch(partidos)
                isrun2 = bool(input('Si desea registrar a otro partido presiona S(SI) o ENTER(NO) : '))
        if op == 3:
            isrun3 = True
            while isrun3:
                os.system('cls')
                tb.tablaa(partidos)
                isrun3 = bool(input('Si desea visualizar la tabla de otra categoria presiona S(SI) o ENTER(NO) : '))
                
        if op == 4:
            isrun4 = True
            while isrun4:
                os.system('cls')
                win.wincat(partidos)
                isrun4 = bool(input('Presiona ENTER para continuar'))
                
        if op == 5:
            Isrun = False
       