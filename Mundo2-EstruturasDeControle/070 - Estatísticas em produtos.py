#Exercício Python 070:
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('\33[34m--' * 25)
print('{:-^50}'.format('Loja de Produtos Naturais'))
print('--' * 25 + '\33[m')
maiorp = preço = totalcompra = i = 0
baratop = 0
while True:
    nomedoproduto = str(input('Nome do produto:'))
    preço = float(input('Preço:'))
    totalcompra += preço
    i += 1
    if preço >= 1000:
         maiorp += 1
    if i == 1 or preço < baratop:
        baratop = preço
        baratonome = nomedoproduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'o total da compra foi R${totalcompra:.2f}')
print(f'temos {maiorp} produto s custando mais de 1000,00 ')
print(f'o produto mais barato foi {baratonome}, custando R${baratop:.2f} ')

