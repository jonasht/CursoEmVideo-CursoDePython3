
from datetime import datetime
dados = dict()

print('\n=-=-=-= cadastro de trabalho =-=-=')
dados['nome'] = str(input('nome:'))
dados['ano_nascimento'] = int(input('ano de nascimento:'))
dados['idade'] = datetime.now().year - dados['ano_nascimento']
cpts = input('nº da carteira de trabalho: ')
if cpts:
    dados['cpts'] = cpts

    dados['contratacao'] = int(input('ano de contração: '))
    dados['salario'] = float(input('salario R$: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('\n'+'=-'*25+'=')

for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')
print(dados)