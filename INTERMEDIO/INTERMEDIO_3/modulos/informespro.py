import os
def infpro(inventario:dict):
    os.system('cls')
    encontrado = False
    for key,value in inventario.items():
        if inventario[key]['stock'] < inventario[key]['stockmin']:
            print(f'Codigo :{inventario[key]["codigo"]} ')
            print(f'Nombre :{inventario[key]["nombre"]} ')
            print(f'stock :{inventario[key]["stock"]} ')
            print('-------------------------------------')
            encontrado = True
            
    if not encontrado:
        print('Ningun equipo tiene menos stock que el minimo establecido')
        
    