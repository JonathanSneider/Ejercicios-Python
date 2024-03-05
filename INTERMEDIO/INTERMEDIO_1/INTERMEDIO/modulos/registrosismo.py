import os
def registrosis(listasismos:list):
    ciudadsismo = input('Ingrese la ciudad de la cual desea registrar el sismo : ')

    for i,item in enumerate(listasismos):
        if ciudadsismo == item[0]:
            try:
                sismo = float(input('Ingrese La Magnitud del sismo : '))
            except ValueError:
                print('Ingrese un numero valido')
                os.system('pause')
                os.system('cls')
                registrosis(listasismos)
            else:
                listasismos[i].insert(2,sismo)
                if sismo <= 2.5:
                    listasismos[i][1] = 'AMARILLO (sin riesgo)'
                elif ((sismo >= 2.6) and (sismo <= 4.5)):
                    listasismos[i][1] = 'NARANJA (riesgo medio)'
                elif sismo > 4.5:
                    listasismos[i][1] = 'ROJO (riesgo alto)'
                return
                
       
       
    print('La ciudad no se encuntra registrada intentalo otra vez ')
    