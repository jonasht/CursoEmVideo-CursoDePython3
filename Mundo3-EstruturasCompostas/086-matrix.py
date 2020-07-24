# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3x3 e
#  preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

#matriz = [[2, 3, 4], [7, 5 , 4], [8, 4, 9]]
def l(ll): print(30*ll)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
l('=')
print('valores de matriz a serem adionados')
for i in range(len(matriz)):
    for ii in range(len(matriz)):
        matriz[i][ii] = int(input(f'[{i}|{ii}]numero: '))
        
l('_')
print('Valores de matriz:')
for i in range(3):
    for ii in range(3):
        print(f'{matriz[i][ii]:^10} ', end='')

    print()
l('-')