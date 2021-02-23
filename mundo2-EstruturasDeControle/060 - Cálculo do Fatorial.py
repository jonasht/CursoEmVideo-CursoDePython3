#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('fatorial:'))
c = 1
for i in range(n, 0, -1):
    print('{}'.format(i),end='')
    print(' X ' if i > 1 else ' = ', end='')
    c *= i

print(c)