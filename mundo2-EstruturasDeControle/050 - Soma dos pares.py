#Exercício Python 050:
# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = c = 0
for i in range(0, 6):
    n = int(input('{}º Numero par para ser somados:'.format(i+1)))
    if n % 2 == 0:
        soma += + n
        c += 1
print('Quantidade de numeros somados foi {} a soma dos N {}'.format(c, soma))