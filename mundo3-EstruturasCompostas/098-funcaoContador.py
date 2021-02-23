#Exercício Python 098: 
# Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através
# da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

import time
inicio = fim = passo = 0
def contador(inicio, fim, passo=1):
    print('=-'*30+'=')
    print(f'contagem de {inicio} até {fim} com o passo {passo}')
    
    # o proprio FOR evita loop infinito caso a regra não seja dada
    for i in range(inicio, fim, passo):
        print(f'{i} ', flush=True, end='')
        time.sleep(.1)
    print()
    print('=-'*30+'=')

contador(1, 10)
contador(10, 0, -2)

inicio = int(input('(inicio) DE:'))
fim = int(input('     (fim) até: '))
passo = int(input('         passo: '))

contador(inicio, fim, passo)
