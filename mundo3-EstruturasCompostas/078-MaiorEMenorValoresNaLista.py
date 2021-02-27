lista = []

for i in range(5):
    lista.append(int(input(f'numero {i}: ')))
    
    if i == 0:
        maior_valor = menor_valor = lista[i] 
    
    if lista[i] > maior_valor:
        maior_valor = lista[i]
    elif lista[i] < menor_valor:
        menor_valor = lista[i]

print('=-'*30)
print(f'maior valor digitado:{maior_valor} nas posições:', end='')
for posicao, valores in enumerate(lista):
    if valores == maior_valor:
        print(f'{posicao}...', end='')
print()
print(f'menor valor digitado:{menor_valor} nas posições:', end='')
for posicao, valores in enumerate(lista):        
    if valores == menor_valor:
        print(f'{posicao}...', end='')

#Exercício Python 078:
# Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi 
# o maior e o menor valor digitado e 
# as suas respectivas posições na lista. 
        