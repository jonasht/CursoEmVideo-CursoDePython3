from random import randint
from time import sleep
import colorama
colorama.init()
cr = '\033[31m' # red
cb = '\033[34m' # blue
cg = '\033[32m' # green
f = '\33[m'

ms = []
tms = []
def l(lc): print(cb + 40*lc + f)
qtd = 5

l('=')

print(f'\t {cg}Gerador De MegaSena{f}')
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
    if i % 2 == 0:
        print(cr, end='')
    else:
        print(cg, end='')
    print(f'jogo {i+1:<3}: ', end='')
    for lista_numero in lista:
        print(f'{lista_numero:>2} ', end='')
    print(f)

    sleep(.1)

l('=')
l('¨')