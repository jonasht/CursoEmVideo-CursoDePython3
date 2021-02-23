#Exercício Python 087: 
# Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

#matriz = [[2, 3, 4], [7, 5 , 4], [8, 4, 9]]
def l(ll): print(30*ll)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumPar = terC = 0

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
        sumPar = sumPar+matriz[i][ii] if matriz[i][ii]%2==0 else sumPar # soma de tds os valores pares digitds
        terC = terC + matriz[i][ii] if ii == 2 else terC
    print()
l('_')
print(f'soma dos numeros pares: {sumPar}')
print(f'soma dos valores da terceira coluna: {terC}')#  A soma dos valores da terceira coluna
print(f'maior valor da segunda linha: {max(matriz[1])}')# O maior valor da segunda linha