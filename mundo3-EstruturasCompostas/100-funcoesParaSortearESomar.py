#Exercício Python 100: 
# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e 
# vai colocá-los dentro da lista e 
# a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint

def sortear(numeros):
    numeros = [randint(1, 10) for i in range(6)]
    return numeros
    
def somarPar(numeros):
    numeroParSomar=0
    for par in numeros:
        if par % 2 == 0:
            numeroParSomar+= par
    return numeroParSomar

lista = list()
lista = sortear(lista)
print(f'os numeros sorteados são:')
[print(f'{l} ', end='') for l in lista]

print(f'\nsoma dos pares {somarPar(lista)}')