#Exercício Python 039:
# Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou
#  se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoatual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = anoatual - nascimento
print('quem nasceu {} tem {} anos em {}'.format(nascimento,idade,anoatual))

if idade == 18:
    print('voce precisa de alistar')
elif idade < 18:
    print('voce tem que se alistar em {} anos no ano de {}'.format(18 - idade, anoatual + (18 - idade)))
else:
    print('voce deveria ter se alistado em {} há {} anos atrás'.format((18 - idade) + anoatual, idade - 18))

