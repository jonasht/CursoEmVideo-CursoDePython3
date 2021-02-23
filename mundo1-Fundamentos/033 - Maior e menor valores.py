#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('qual n 1:'))
n2 = int(input('qual n 2:'))
n3 = int(input('qual n 3:'))
# maior
if n1 > n2 and n1 > n3:
        nm = n1
elif n2 > n3:
        nm = n2
else:
        nm = n3
# N menor
if n1 < n2 and n1 < n3:
        nme = n1
elif n2 < n3:
        nme = n2
else:
        nme = n3
print('\no n maior é {}'.format(nm))
print('o N menor é {}'.format(nme))



