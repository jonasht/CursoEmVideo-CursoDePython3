
print(13*'-=-')

print(f'{"LISTAGEM DE PRODUTOS":^40}')

print(13*'-=-')

list = ('Lapis', 2.50,

            'Borracha', 1.00,

            'Caneta', 1.25,

            'Apontador', 1.20,

            'Estojo', 2.50,

            'Caderno', 10.40,

            'Lapiseira', 7.95,

            'Mochila', 120)

for i in range(0, len(list)):
    if i % 2 == 0:
        print(f'{list[i]:.<30}', end='')
    else:
        print(f'R${list[i]:>7.2f}')




print(13*'-=-')

#Exercício Python 076:
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.