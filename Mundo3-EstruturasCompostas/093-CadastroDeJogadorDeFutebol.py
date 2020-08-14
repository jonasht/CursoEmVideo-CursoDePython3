dados = dict()
qtd_gols = []
dados['nome'] = input('nome do jogador: ')

def l(): print('\n'+'=-'*25+'=')

qtd_partida = int(input('quantas partidas:'))

for i in range(qtd_partida):
    qtd_gols.append(int(input(f'quantos gols na {1+i}º partida: ')))
dados['gols'] = qtd_gols[:]
dados['total'] = sum(qtd_gols)

l()
print(dados)
l()
for chave, valor in dados.items():
    print(f'o campo {chave} tem o valor {valor}')
    
    
l()
print(f"o jogador {dados['nome']} jogou {len(dados['gols'])} partidas.")
for i, v in enumerate(dados['gols']):
    print(f"\t=> Na {i+1}º partida, fez {dados['gols'][i]}")
l()