#Exercício Python 052:
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('N:'))
total = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\33[34m',end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')
    print(i,end=' ')
print('\n\33[35mO numero {} foi divisivel por {}X'.format(n, total))
if total == 2:
    print('e por isso o N é Primo')
else:
    print('E por isso o N não é Primo')
