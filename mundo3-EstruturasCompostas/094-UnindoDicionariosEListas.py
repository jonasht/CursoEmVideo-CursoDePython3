#Exercício Python 094:
# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e
#  todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média


def l(): print(20*'=-'+'=')

l()
pessoal = list() # list []
dados = dict() # dictionary {}
idades = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('nome: '))
    while True:    
        print('m = masculino, f feminino, n não está incluso a opcao')
        dados['sexo'] = str(input('sexo M/F/N:').upper()[0])
        if dados['sexo'] in 'MFN':
            break
        print('por digite apenas M F ou N')

    dados['idade'] = int(input('idade:'))
    idades += dados['idade']
    
    pessoal.append(dados.copy()) # p fazer uma copia dos dados p a lista pessoal
    
    sair = str(input(' continuar? S/n: ')).upper()[0]
    if sair == 'N': break
l()
print(f'total de pessoas cadastradas {len(pessoal)}')
print(f'media de idade: {(idades / len(pessoal)):5.2f} anos.')
print(pessoal)
media = idades / len(pessoal)
l()
print(f'as mulheres cadastradas foram: ', end='')
for p in pessoal:
    if p['sexo'] == 'F':
        print(f'{p["nome"], }', end='')
print()
l()

for p in pessoal:
    if p['idade'] >= media:
        
        for key, value in p.items():
            print(f'{key} = {value}: ', end='')
        print('\n')
