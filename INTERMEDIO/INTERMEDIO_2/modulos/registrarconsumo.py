import os
def registrarcos(C02:dict):
    nombre = input('Ingrese el nombre de la dependencia de la cual desea regitrar su consumo : ')
    encontrado = False
    for key in C02:
        if nombre == key:
            oficinass = C02[key]['oficinas']
            km = int(input('Ingrese la cantidad de kilometros recorridos por la dependencia en total : '))
            for i in range(0,oficinass):
                kwhsh = 0
                kwhhh = 0
                co2kkm = 0
                co2total = 0
                for i in range(C02[key]['oficinas']):
                    kwh = float(input(f'ingrese la cantidad de kWh(kilovatios-hora) consumidos por la oficina numero {i+1} '))
                    kwhmmt = int(input('Ingresa el periodo de facturacion en meses : '))
                    kwhsh += kwh
                    kwhmm = kwhsh/kwhmmt
                    kwhhh += kwhmm
                


                co2kkm = km * 0.34
                co2kwhmm = kwhhh * 0.34
                co2total = co2kkm + co2kwhmm
                C02[key]['co2km'] = co2kkm
                C02[key]['co2kwhmm'] = co2kwhmm
                C02[key]['co2total'] = co2total
                encontrado = True
                break

    if not encontrado:
        print('La dependencia que ingresaste no se encuentra registrada')



                
                
        