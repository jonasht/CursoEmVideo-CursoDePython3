from random import randint
from time import sleep
ms = []
tms = []
def l(lc): print(40*lc)
qtd = 5

l('=')

print('\t Gerador De MegaSena')
l('=')
for i in range(qtd):
    while len(ms) != 6:
        r = randint(1, 60)
        if r not in ms and r not in tms:
            ms.append(r)
    ms.sort()
    tms.append(ms[:])
    ms.clear()

for i, lista in enumerate(tms):
    print(f'jogo {i+1:<2}: ', end='')
    for lista_numero in lista:
        print(f'{lista_numero:>2} ', end='')
    print()
    sleep(.1)

l('=')
l('¨')