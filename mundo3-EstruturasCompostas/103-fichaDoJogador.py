#Exercício Python 103:
# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='', gols=0):
    
    if jogador:
        resultado  = f'o jogador {jogador.title()} '
    else:
        resultado = f'o <Jogador> '

    
    if gols:
        resultado +=f'fez {gols} gol.s'
    else: 
        resultado +=f'fez <0> gol.s'  
    return  resultado

print(ficha('ronaldo', 10))
print(ficha(gols=15))
print(ficha(jogador='ferno'))
print(ficha(gols='quize'))
