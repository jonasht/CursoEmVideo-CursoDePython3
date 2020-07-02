pessoas = list()
obter = list()
qtdp = maior = menor = 0
def l():
    print('=-'*30 + '=')
while 1:
    l()
    qtdp += 1
    obter.append(str(input(f'{qtdp} nome:')))
    obter.append(float(input(f'{qtdp} peso:')))
    
    if len(pessoas) == 0:
        maior = menor = obter[1]
    else:
        if obter[1] > maior:
            maior = obter[1]
        if obter[1] < menor:
            menor = obter[1]
            
    pessoas.append(obter[:])
    obter.clear()
    sair = input('quer continuar [S/n]:')
    if sair in 'nN':
        break


l()
print(f'quandidade de pessoas {qtdp} ')

print(f'maior peso foi de {maior}kg. o peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print(f'\nmenor peso foi de {menor}kg. o peso de ', end='')

for p in pessoas:
    if p[1] == menor:
        print(f' {p[0]}')
        
    
# Exercício Python 084: 
# Faça um programa que leia nome e peso de várias pessoas,
#  guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.