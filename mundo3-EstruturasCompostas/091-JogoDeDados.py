# Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
#  sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
ranking = list()

for i in range(4):
    nome = f'jogador{i + 1}'
    jogadores[nome] = randint(1, 6)
    sleep(.2)
    print(f"{nome} tirou {jogadores[nome]} no dado")
    
#key=itemgetter(1): 1 eh o valor e se fosse o 0 seria o nome que estah dentro do dicionario
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(20*'=-'+'=')
print('=-=-= ranking players =-=-=')
for i, jogador in enumerate(ranking):
    print(f'{i+1}º lugar: {jogador[0]} com {jogador[1]}')
print(20*'=-'+'=')    