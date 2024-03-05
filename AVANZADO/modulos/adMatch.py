import os
def admatch(partidoss:dict):
    print('---------------')
    print('-Novato')
    print('-Intermedio')
    print('-Avanzado')
    print('---------------')
    opc = input('Ingrese La categorica a la cual registrara un partido : ').lower().capitalize()

    
    if opc == 'Novato':
        if len(partidoss['Novato']) >= 5 :  
                os.system('cls')
                print('Ingrese El id de los jugadores del cual deseas registrar el partido')
                jugador1= int(input('Ingrese el ID del jugador 1 : '))
                jugador2 = int(input('Ingrese el ID del jugador 2 : '))
                if jugador1 in partidoss['Novato'] and jugador2 in partidoss['Novato']:
                    ptst22 = 0
                    ptst11 = 0
                    sets1 = 0
                    sets2 = 0
                    for i in range(0,5):
                        os.system('cls')
                        pts1 = int(input(f'Ingrese los puntos que metio el jugador {jugador1} en el set {i+1} : '))       
                        pts2 = int(input(f'Ingrese los puntos que metio el jugador {jugador2} en el set {i+1} : '))    
                        if pts1 > pts2:
                            sets1 += 1
                        if pts2 > pts1:
                            sets2 += 1

                        ptst1 = pts1 - pts2
                        ptst11 += ptst1
                        ptst2 = pts2 - pts1
                        ptst22 += ptst2
                        if sets1 == 3:
                            partidoss['Novato'][jugador2]['TP'] += 0
                            partidoss['Novato'][jugador2]['PA'] += ptst22
                            partidoss['Novato'][jugador2]['PP'] += 1
                            partidoss['Novato'][jugador2]['PJ'] += 1
                            partidoss['Novato'][jugador1]['PJ'] += 1
                            partidoss['Novato'][jugador1]['PG'] += 1
                            partidoss['Novato'][jugador1]['TP'] += 2
                            partidoss['Novato'][jugador1]['PA'] += ptst11
                            break
                        elif sets2 == 3:
                            partidoss['Novato'][jugador1]['TP'] += 0
                            partidoss['Novato'][jugador1]['PA'] += ptst11
                            partidoss['Novato'][jugador1]['PP'] += 1
                            partidoss['Novato'][jugador1]['PJ'] += 1
                            partidoss['Novato'][jugador2]['PJ'] += 1
                            partidoss['Novato'][jugador2]['PG'] += 1
                            partidoss['Novato'][jugador2]['TP'] += 2
                            partidoss['Novato'][jugador2]['PA'] += ptst22
                            break
                                
        else:
            print('El numero de estudiante registrados en esta categoria es menor del permitido para empezar el torneo')
            os.system('pause') 
            os.system('cls')
            admatch(partidoss)   
    elif opc == 'Intermedio':
        if len(partidoss['Intermedio']) >= 2 :  
                print('Ingrese El id de los jugadores del cual deseas registrar el partido')
                jugador1= int(input('Ingrese el ID del jugador 1 : '))
                jugador2 = int(input('Ingrese el ID del jugador 2 : '))
                if jugador1 in partidoss['Intermedio'] and jugador2 in partidoss['Intermedio']:
                    ptst22 = 0
                    ptst11 = 0
                    sets1 = 0
                    sets2 = 0
                    for i in range(0,5):
                        pts1 = int(input(f'Ingrese los puntos que metio el jugador {jugador1} en el set {i+1} : '))       
                        pts2 = int(input(f'Ingrese los puntos que metio el jugador {jugador2} en el set {i+1} : '))    
                        if pts1 > pts2:
                            sets1 += 1
                        if pts2 > pts1:
                            sets2 += 1

                        ptst1 = pts1 - pts2
                        ptst11 += ptst1
                        ptst2 = pts2 - pts1
                        ptst22 += ptst2
                        if sets1 == 3:
                            partidoss['Intermedio'][jugador2]['TP'] += 0
                            partidoss['Intermedio'][jugador2]['PA'] += ptst22
                            partidoss['Intermedio'][jugador2]['PP'] += 1
                            partidoss['Intermedio'][jugador2]['PJ'] += 1
                            partidoss['Intermedio'][jugador1]['PJ'] += 1
                            partidoss['Intermedio'][jugador1]['PG'] += 1
                            partidoss['Intermedio'][jugador1]['TP'] += 2
                            partidoss['Intermedio'][jugador1]['PA'] += ptst11
                            break
                        elif sets2 == 3:
                            partidoss['Intermedio'][jugador1]['TP'] += 0
                            partidoss['Intermedio'][jugador1]['PA'] += ptst11
                            partidoss['Intermedio'][jugador1]['PP'] += 1
                            partidoss['Intermedio'][jugador1]['PJ'] += 1
                            partidoss['Intermedio'][jugador2]['PJ'] += 1
                            partidoss['Intermedio'][jugador2]['PG'] += 1
                            partidoss['Intermedio'][jugador2]['TP'] += 2
                            partidoss['Intermedio'][jugador2]['PA'] += ptst22
                            break
                                
        else:
            print('El numero de estudiante registrados en esta categoria es menor del permitido para empezar el torneo')
            os.system('pause') 
            os.system('cls')
            admatch(partidoss)   
    elif opc == 'Avanzado':
        if len(partidoss['Avanzado']) >= 2 :  
                print('Ingrese El id de los jugadores del cual deseas registrar el partido')
                jugador1= int(input('Ingrese el ID del jugador 1 : '))
                jugador2 = int(input('Ingrese el ID del jugador 2 : '))
                if jugador1 in partidoss['Avanzado'] and jugador2 in partidoss['Avanzado']:
                    ptst22 = 0
                    ptst11 = 0
                    sets1 = 0
                    sets2 = 0
                    for i in range(0,5):
                        pts1 = int(input(f'Ingrese los puntos que metio el jugador {jugador1} en el set {i+1} : '))       
                        pts2 = int(input(f'Ingrese los puntos que metio el jugador {jugador2} en el set {i+1} : '))    
                        if pts1 > pts2:
                            sets1 += 1
                        if pts2 > pts1:
                            sets2 += 1

                        ptst1 = pts1 - pts2
                        ptst11 += ptst1
                        ptst2 = pts2 - pts1
                        ptst22 += ptst2
                        if sets1 == 3:
                            partidoss['Avanzado'][jugador2]['TP'] += 0
                            partidoss['Avanzado'][jugador2]['PA'] += ptst22
                            partidoss['Avanzado'][jugador2]['PP'] += 1
                            partidoss['Avanzado'][jugador2]['PJ'] += 1
                            partidoss['Avanzado'][jugador1]['PJ'] += 1
                            partidoss['Avanzado'][jugador1]['PG'] += 1
                            partidoss['Avanzado'][jugador1]['TP'] += 2
                            partidoss['Avanzado'][jugador1]['PA'] += ptst11
                            break
                        elif sets2 == 3:
                            partidoss['Avanzado'][jugador1]['TP'] += 0
                            partidoss['Avanzado'][jugador1]['PA'] += ptst11
                            partidoss['Avanzado'][jugador1]['PP'] += 1
                            partidoss['Avanzado'][jugador1]['PJ'] += 1
                            partidoss['Avanzado'][jugador2]['PJ'] += 1
                            partidoss['Avanzado'][jugador2]['PG'] += 1
                            partidoss['Avanzado'][jugador2]['TP'] += 2
                            partidoss['Avanzado'][jugador2]['PA'] += ptst22
                            break
                                
        else:
            print('El numero de estudiante registrados en esta categoria es menor del permitido para empezar el torneo')
            os.system('pause') 
            os.system('cls')
            admatch(partidoss) 
    else:
        print('Ingresaste una categoria no valida intentalo otra vez')
        os.system('pause') 
        os.system('cls')
        admatch(partidoss)
        


    