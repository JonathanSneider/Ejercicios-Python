import os 
def imc():
    nombre = input('Ingrese el nombre del Estudiante :')
    edad = input(f'Ingrese la edad de {nombre} :')
    peso = input(f'Ingrese el peso del estudiante {nombre} en kg :')
    altura = input(f'Ingrese la altura del estudiante {nombre} en M :')
    
    if edad.isdigit and peso.isdigit and altura.isdigit:
        peso = float(peso)
        altura = float(altura)
        immc = peso *1000 //  altura**2 / 1000
        if ((immc >= 18.5)and(immc <= 24.9)):
            categoria = 'NORMAL'
        elif ((immc >= 25)and(immc <= 29.9)):
            categoria = 'SOBREPESO'
        elif ((immc >= 30)and(immc <= 34.9)):
            categoria = 'OSBESIDAD I'    
        elif ((immc >= 35)and(immc <= 39.9)):
            categoria = 'OBESIDAD II'
        elif (immc >= 40):
            categoria = 'OBSIDAD III'
        else:
            categoria = 'DESNUTRIDO'        
        print(f'Nombre : {nombre}')
        print(f'edad : {edad}')
        print(f'IMC : {immc}')
        print(f'Categoria : {categoria}')
    else:
        print('ERROR Ingresaste algun dato invalido intentalo otra vez')
        os.system('pause')
        os.system('cls')
        imc()
        
imc()
        
    
