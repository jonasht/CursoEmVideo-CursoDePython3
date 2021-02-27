# Exercício Python 101: 
# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anoDeNascimento, anoAtual=2021):
    
    idade = anoAtual - anoDeNascimento
    
    return permissaoPvotar(idade)

def permissaoPvotar(idade):
    if idade >= 18:
        return f'pode vorar com {idade} de idade'
    else:
        return f'nao pode votar com {idade} de idade'

variavel = int(input('que voce nasceu:'))
print(f'voce {voto(variavel)}')

