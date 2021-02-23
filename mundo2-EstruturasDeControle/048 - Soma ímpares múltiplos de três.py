#Exercício Python 048:
# Faça um programa que calcule a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.


r = c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        r += i
print('a soma de todos os {} valores são {}'.format(c,r))
