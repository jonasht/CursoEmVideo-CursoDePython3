i = 0
while True:
    n = int(input('Qual tabuada:'))
    if n < 0: break
    while True:
        if i == 10: break
        i += 1
        print(f'{n} X {i} = {n*i}')
print('fim de programa')

#Exercício Python 067:
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.