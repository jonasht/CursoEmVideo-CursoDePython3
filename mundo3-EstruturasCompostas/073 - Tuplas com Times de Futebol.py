# Exercício Python 073:
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

time = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG',
        'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
        'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print('-='* 20)
print(f'lista de times do Brasileirão: {time}')
print('-='* 20)
print(f'os 5 primeiros times são: {time[0:5]}')
print('-='* 20)
print(f'os 4 Ultimos times são: {time[-4:]}')
print('-='* 20)
print(f'Times em ordem alfabetica:{sorted(time)}')
print('-='* 20)
print(f'o time Chapecoemse está na posição: {time.index("Chapecoense") + 1}ª')
print('-='* 20)
