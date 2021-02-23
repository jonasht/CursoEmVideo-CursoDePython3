#Exercício Python 069:
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idadec = sexom = sexof = 0
while True:
    print('--' * 20)
    print('cadastro de pessoa')
    print('--' * 20)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]Sexo:')).strip().upper()[0]
    sair = ' '
    if idade >= 18:
        idadec += 1
    if sexo == 'M':
        sexom += 1
    if sexo == 'F' and idade < 20:
        sexof += 1
    while sair not in 'SN':
        sair = str(input('Quar continuar [S/N]:')).strip().upper()[0]
    if sair == 'N':
        break
print(f'total de pessoas que tem mais de  18 anos: {idadec}')
print(f'há {sexom} homem s cadastrado s')
print(f'há {sexof} mulher s com menos de 20 anos')
