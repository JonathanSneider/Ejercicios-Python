import os
import Menu as mn
import menureportes as mr
import reportes as rp
import registros as rgt
if __name__ == "__main__":
    registroess = {}
    IsRunnMenu = True
    while IsRunnMenu == True:
        op = mn.menu()
        if op == '1':
            os.system('cls')
            isrunreg = True
            while isrunreg == True:
                os.system('cls')
                rgt.imc(registroess)
                isrunreg = bool(input('Presiones ENTER para regresar el menu principal'))
        elif op == '2':
            isRunMenur = True
            while isRunMenur == True:
                os.system('cls')
                opmr = mr.reportes()
                if opmr == 'A':
                   isrunA = True
                   while isrunA:
                        rp.reporteA(registroess)
                        isrunA = bool(input('Presiones ENTER para regresar el menu principal'))
                if opmr == 'B':
                    isrunB = True
                    while isrunB:
                        rp.reportB(registroess)
                        isrunB =  bool(input('Presiones ENTER para regresar el menu principal'))
                if opmr == 'C':
                    isrunC = True
                    while isrunC:
                        rp.reportC(registroess)
                        isrunC = bool(input('Presiones ENTER para regresar el menu principal'))
                if opmr == 'D':
                    isrunD = True
                    while isrunD:
                        rp.reportD(registroess)
                        isrunD = bool(input('Presiones ENTER para regresar el menu principal'))
                if opmr == 'E':
                    isrunE = True
                    while isrunE:
                        rp.reportE(registroess)
                        isrunE = bool(input('Presiones ENTER para regresar el menu principal'))
                if opmr == 'F':
                    isRunMenur = False
                   
        elif op == '3':
            IsRunnMenu = False
                
            
            
                
            
            
            


    
    