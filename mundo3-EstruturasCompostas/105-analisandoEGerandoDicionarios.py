# Exercício Python 105:
# Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situações(opcional) de alunos.
    :param notas: n notas dos alunos
    :param situacao: situacao do aluno (False/True)
    :return: dicionario com informações 
    """
    dic = {}
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = sum(notas)/dic['total']
    
    if situacao:
        if dic['media'] > 7:
            dic['situacao'] = 'boa'
        elif dic['media'] > 5:
            dic['situacao'] = 'razoavel'
        else:
            dic['situacao'] = 'ruim'
    return dic

#notas = notas(6.5, 9.2, 1)
#print(notas)

n = notas(5.1, 9.5, 5.6, 4,5, 4.0, situacao=True)
print('\033[33m'+'=-'*30+'=')
for key, value in n.items():
    print(f'=\t\033[34m{key}: {value}\033[m')
print('\033[33m'+'=-'*30+'=\033[m')