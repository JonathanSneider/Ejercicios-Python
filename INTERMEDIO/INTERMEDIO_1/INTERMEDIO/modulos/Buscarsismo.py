import os
def buscarsismo(listasismos:list):
    totalsismos = len(listasismos[0])
    for i in listasismos[1:]:
        if len(i) != totalsismos:
            print('Las ciudades no tienen las mismas cantidades de sismos')
            os.system('pause')
            return
            
        else:
            pass
    ciudadbusc = input('Ingrese la ciudad de la cual desea saber los sismos : ')
    

    for i,value in enumerate(listasismos):
        if ciudadbusc in value:
            print(f'Los sismos de la ciudad {ciudadbusc} son {listasismos[i][2:]}')
            return

    print('La ciudad de la cual deseas saber el sismo no se encuentra registrada')
    
        

            