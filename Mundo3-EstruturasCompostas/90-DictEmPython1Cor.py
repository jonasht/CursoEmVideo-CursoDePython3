#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
#  guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

import colorama
colorama.init() # p/ funcionar no windows

r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'

aluno = dict()

aluno['nome'] = str(input('nome:'))
aluno['nota'] = float(input('nota media:'))

if aluno['nota'] < 5:
    aluno['situacao'] = r + 'reprovado' + f
elif aluno['nota'] < 6:
    aluno['situacao'] = g + 'em recuperação' + f
else:
    aluno['situacao'] = b + 'aprovado' + f
    

print(20*'--')
print(f"nome: {aluno['nome']}, nota: {aluno['nota']} situação: {aluno['situacao']}")

