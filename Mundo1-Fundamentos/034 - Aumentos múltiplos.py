# Exercício Python 034:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('qual é o salario do funcionario? '))
if s > 1250.00:
    rs = (s / 100) * 10
    print('salario {} com o aumente de {} de 10%'.format(rs + s, rs))
else:
    rs = s / 100 * 15
    print('salario {} com o aumente de {} de 15%'.format(rs + s, rs))
