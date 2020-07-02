from random import randint
print('-='*10 + ' Par/ IMPAR '+'-='*10)
i = 0
pescolha = ' '
while True:
    pc = randint(0, 10)
    n = int(input('escolha um numero:'))
    while pescolha not in ('IMPAR'):
        pescolha = str(input('Par ou Impar [PAR/IMPAR]:')).strip().upper()
    soma = n + pc
    if soma % 2 == 0:
        resposta = 'PAR'
    else:
        resposta = 'IMPAR'
    print(f'voce escolheu {n}, pc {pc}, total {soma}')
    print(f'deu {resposta}')
    if pescolha[0] == resposta[0]:
        print('voce ganhou' )
        i += 1
    else:
        print('pc ganhou')
        break
print(f'Fim de jogo, voce venceu {i} vezes')

#Exercício Python 068:
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.