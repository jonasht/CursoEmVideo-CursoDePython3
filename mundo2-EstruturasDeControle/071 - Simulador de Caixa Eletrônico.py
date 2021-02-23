#Exercício Python 071:
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
# o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
c50 = c20 = c10 = c1 = 0
print('\33[36m==' * 25)
print('{: ^50}'.format(' Good Bank '))
print('==' * 25 + '\33[m')
saque = int(input('Quantidade a ser sacada R$:'))
while True:
    if saque >= 50:
        saque -= 50
        c50 += 1
    elif saque >= 20:
        saque -= 20
        c20 += 1
    elif saque >= 10:
        saque -= 10
        c10 += 1
    elif saque >= 1:
        saque -= 1
        c1 += 1
    else:
        break
print('\33[36m¨¨' * 25)
if c50 > 0:
    print(f'{c50} cedula s de 50 reais ')
if c20 > 0:
    print(f'{c20} cedula s de 20 reais ')
if c10 > 0:
    print(f'{c10} cedula s de 10 reais ')
if c1 > 0:
    print(f'{c1} cedula s de 1 real ')
print('¨¨' * 25 + '\33[m')