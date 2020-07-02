import os
from random import randint
print('\33[34m-='*22 + '\njogo de adivinhar numero\n' + '-='*22)
p = randint(0, 10)
r = int(input('\33[mde 0 a 10 um Numero: '))
os.system(cls)
palpite = 1
while not(r == p):
    print('incorreto')
    palpite += 1
    if r < p:
        print('N {}> '.format(r))
    else:
        print('N <{}'.format(r))
    r = int(input('Numero: '))
print('N correto, {} palpite s'.format(palpite))

#Exercício Python 058:
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
