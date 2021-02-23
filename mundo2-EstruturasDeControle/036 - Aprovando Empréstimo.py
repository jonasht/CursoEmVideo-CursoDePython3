#Exercício Python 036:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\33[36m*\33[m'*20)
cvalor = float(input('qual o valor da casa? :'))
svalor = float(input('qual é o seu salario? :'))
anos = int(input('por quantos anos?:'))

mensano = cvalor / (anos * 12)
print('para pagar uma casa de R${:.2f}'.format(cvalor))
print('em {} anos, a prestação será de R${:.2f}'.format(anos, mensano))
minimo = svalor * (30 / 100)

if mensano <= minimo:
    print('Emprestimo \33[36mAprovado')
else:
    print('Emprestimo \033[31mNegado')


