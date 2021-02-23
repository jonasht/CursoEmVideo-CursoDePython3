# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('primeiro termo:'))
ra = int(input('Razão:'))

decimot = pt + (10 - 1) * ra
termo = pt
i = 1
while i <= 10:
    print(' {} ->'.format(termo), end='')
    termo += ra
    i += 1
print('fim')