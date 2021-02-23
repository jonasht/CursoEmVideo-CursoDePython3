dados = dict()
time = list()
qtd_gols = list()

while True:
    dados.clear()
    
    dados['nome'] = input('nome do jogador: ')

    def l(): print('\n'+'=-'*25+'=')

    qtd_partida = int(input('quantas partidas:'))
    qtd_gols.clear()
    for i in range(qtd_partida):
        qtd_gols.append(int(input(f'quantos gols na {1+i}º partida: ')))
    dados['gols'] = qtd_gols[:]
    dados['total'] = sum(qtd_gols)
    time.append(dados.copy())
    
    while True:
        sair = str(input('escreva s para sair e n para não: S/N').lower().strip()[0])
        if sair in 'sn':
            break
        print('"erro", responda apenas s para sair e n para não')
    if sair == 's':
        break

l()
print('dados ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
l()

for key, v in enumerate(time):
    print(f'{key:>3} ', end='')
    for i in v.values():
        print(f' {str(i):<15}', end='')
    print()
    
l()