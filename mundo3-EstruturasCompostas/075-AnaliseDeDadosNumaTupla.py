#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
n = (int(input('digite o numero 1:')),
     int(input('digite o numero 2:')),
     int(input('digite o numero 3:')),
     int(input('digite o numero 4:')))
if 9 in n:
    print(f'o numero 9 apreceu {n.count(9)}')
if 3 in n:
    print(f'o numero 3 foi digitado na posição {n.index(3)}')
print('o valores pares foram:', end=' ')
for i in range(0, 4):
    if n[i] % 2 == 0:
        print(n[i], end=' ')
