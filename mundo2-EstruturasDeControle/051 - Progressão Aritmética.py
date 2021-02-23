# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('primeiro termo:'))
ra = int(input('Razão:'))
decimot = pt + (10 - 1) * ra
for i in range(pt, decimot + ra, ra):
    print(i, end=' -> ')
print('fim')