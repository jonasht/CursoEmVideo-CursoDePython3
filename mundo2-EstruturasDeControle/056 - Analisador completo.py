#Exercício Python 056:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.
mulher20 = 0
midade = 0
sidade = 0
maioridadeh = 0
nomevelho = ''
for i in range(0, 4):
    print('------| Pessoa {} |--------'.format(i+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: '))
    sidade += idade
    if i == 0 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print('A media de idade: {}'.format(sidade / 4))
print('O homem mais velho tem {} anos e o nome: {}'.format(maioridadeh, nomevelho))
print('são {} mulher s com menos de 20 anos'.format(mulher20))