import random
pieza=()
movimientos = 0
pieza_sacada=()
lista_4x4 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_3x3 = [0,1,2,3,4,5,6,7,8]

while True:
    lista_escogida_numero = input("Escoja: Matrix de 4x4 (4) o de 3x3 (3)")
    if(lista_escogida_numero == '3'):
        lista_escogida= lista_3x3            
        break;
    elif(lista_escogida_numero == '4'):
        lista_escogida= lista_4x4
        break;
    else:
        print("Escoja 4 o 3 para la dimensión de la matriz")
random.shuffle(lista_escogida)
print('\n'*2)

matrix=[]
while lista_escogida !=[]:
    matrix.append(lista_escogida[:int(lista_escogida_numero)])
    lista_escogida = lista_escogida[int(lista_escogida_numero):]

pieza_sacada = (0,0)
num_pieza_sacada = matrix[0][0]
while True:
    if(lista_escogida_numero == '3'):
        print('\n+----+----+---|')        
    else:
        print('\n+----+----+----+---|')    
    
    for x in range (len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == num_pieza_sacada:
                print('|XX' , end='  ')
            else:
                 print('|' + '{:02d}' .format(matrix[x][y]), end='  ') 
        if(lista_escogida_numero == '3'):
            print('\n+----+----+---|')        
        else:
            print('\n+----+----+----+---|') 
    #ask for the next move
    num = input('\nplease type the number of the piece to move : ( q ) to quit  ')
    if num in ['q','Q']:
        break
    num = int(num)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                pieza = (i,j)
                print(pieza)
    if num > 15:
        print('illegal move  ')
    else:
        if(pieza_sacada==(pieza[0]-1,pieza[1]))\
           or(pieza_sacada==(pieza[0]+1,pieza[1]))\
           or(pieza_sacada==(pieza[0],pieza[1]-1))\
           or(pieza_sacada==(pieza[0],pieza[1]+1)):
            matrix[pieza_sacada[0]][pieza_sacada[1]]=num
            matrix[pieza[0]][pieza[1]]=num_pieza_sacada
            pieza_sacada=(pieza[0],pieza[1])
            movimientos = movimientos +1
            print()
            print('you have made ',movimientos , 'moves so far ')
            print(2*'\n')
        else:
            print('illegal move , try again ')
print('game over  ')