import os
from tabulate import tabulate
def inforiesgo(listasismos:list):
    totalsismos = len(listasismos[0])
    for i in listasismos[1:]:
        if len(i) != totalsismos:
            print('Las ciudades no tienen las mismas cantidades de sismos')
            os.system('pause')
            return
    for i,values in enumerate(listasismos):
        print(f'{listasismos[i][0]} : {listasismos[i][1]} ')
        
        

    