#Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVADO
notaum = float(input('qual é nota um: '))
notadois = float(input('qual é nota dois: '))

media = (notaum + notadois) / 2
print('media de nota é {:.2f}'.format(media))

if media >= 7:
    print('\33[34mAprovado')
elif media < 5:
    print('\33[7;31mReprovado\33[m')
else:
    print('\33[30;4mEm recuperação')