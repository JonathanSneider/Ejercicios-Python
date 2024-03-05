import os
import modulos.menu as mn
import modulos.registroproductos as rg
import modulos.visualizarpro as vs
import modulos.actstock as ac
import modulos.informespro as inf
import modulos.ganancia as gn
inventario = {}
if __name__ == "__main__":
    IsRun = True
    while IsRun:
        os.system('cls')
        op = mn.menu()
        if op == 1:
            isRunreg = True
            while isRunreg:
                os.system('cls')
                rg.registropro(inventario)
                isRunreg = bool(input('Si desea agregar otro producto presiona S(Si) o ENTER(No) : '))

        if op == 2:
            isRun2 = True
            while isRun2:
                os.system('cls')
                vs.vispro(inventario)
                isRun2 = bool(input('Presiona ENTER para continuar : '))

        if op == 3:
            isrun3 = True
            while isrun3:
                os.system('cls')
                ac.actstockk(inventario)
                isrun3 = bool(input('Si desea actualizar el stock de otro producto presiona S(Si) o ENTER(No) : '))
        if op == 4:
            isrun4 = True
            while isrun4:
                inf.infpro(inventario)
                os.system('pause')
                isrun4 = False
        if op == 5:
            isrun5 = True
            while isrun5:
                os.system('cls')
                gn.ganancias(inventario)
                isrun5 = bool(input('Presiona ENTER para continuar : '))
        if op == 6:
            IsRun = False


