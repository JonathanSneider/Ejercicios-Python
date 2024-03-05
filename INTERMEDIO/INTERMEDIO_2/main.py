import os
import modulos.menu as mn
import modulos.regdep as re
import modulos.registrarconsumo as rec
import modulos.verc02 as ver
import modulos.dependenciamax as dpm
C02 = {}
if __name__ == "__main__":
    IsRun = True
    while IsRun:
        os.system('cls')
        op = mn.menu()
        if op == '1':
            isrun1 = True
            while isrun1:
                os.system('cls')
                re.importdep(C02)
                isrun1 = bool(input('Si desea registrar otra dependencia presion S(si) o ENTER(no) : '))
        if op == '2':
            isrun2 = True
            while isrun2:
                os.system('cls')
                rec.registrarcos(C02)
                isrun2 = bool(input('Si desea registrar el consumo de otra dependencia presiona S(SI) o ENTER(NO) : '))

        if op == '3':
            isrun3 = True
            while isrun3:
                os.system('cls')
                ver.verco2(C02)
                isrun3 = bool(input('presione ENTER para continuar : '))

        if op == '4':
            isrun4 = True
            while isrun4:
                os.system('cls')
                dpm.verco22(C02)
                isrun4 = bool(input('presione ENTER para continuar : '))
                
        if op == '5':
            IsRun = False
        
        
        
        
        
        
        