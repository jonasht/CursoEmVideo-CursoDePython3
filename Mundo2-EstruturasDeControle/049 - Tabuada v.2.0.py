#Exercício Python 049:
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from time import sleep

print('\33[36m-='*11)
print('TABUADA')
print('-='*11)
n = int(input('Tabuada do:\33[m'))

for i in range(0, 10 +1):
    print('\033[33m{} X {} = {}'.format(n, i, n * i))
    sleep(.1)
