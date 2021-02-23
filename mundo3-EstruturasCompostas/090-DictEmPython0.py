#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
#  guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('nome:'))
aluno['nota'] = float(input('nota media:'))

if aluno['nota'] < 5:
    aluno['situacao'] = 'reprovado'
elif aluno['nota'] < 6:
    aluno['situacao'] = 'em recuperação'
else:
    aluno['situacao'] = 'aprovado'
    

print(20*'--')
print(f"nome: {aluno['nome']} nota: {aluno['nota']} situação: {aluno['situacao']}")

