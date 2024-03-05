import os
def ganancias(inventario:dict):
    for key, value in inventario.items():
        gananciato = inventario[key]['valorventa'] - inventario[key]['valorcompra']
        print(f'La ganancia del producto {inventario[key]["nombre"]} es de : {gananciato}')
        
    