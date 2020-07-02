#Exercício Python 054:
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
ma = me = 0
from datetime import date
for i in range(0, 7):
    anop = int(input('Em ano que pessoa {} nasceu: '.format(i+1)))
    if date.today().year - anop < 18:
        me += 1
    else:
        ma += 1
print('há {} pessoas menores de idade e {} pessoas maiores de idade'.format(me, ma))