#Exercício Python 044:
#Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

pr = float(input('Qual é o valor R$:'))
op = int(input('1 à vista em dinheiro \n2 à vista no cartão\n3 em até 2x no cartão\n4 3x ou mais no cartão\nopção: '))

if op == 1:
    re = pr - (pr * 10 / 100)
elif op == 2:
    re = pr - (pr * 5 / 100)
elif op == 3:
    re = pr
    print('será em 2X de R${}:'.format(re / 2))
elif op == 4:
    re = pr + (pr * 20 / 100)
    par = int(input('quantas parcelas:'))
    print('será em {}X de R${:.2f} com juros:'.format(par, re / par))
else:
    print('opção incorreta')

print('De R${:.2f} por R${:.2f}'.format(pr, re))