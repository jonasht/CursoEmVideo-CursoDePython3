# Exercício Python 101: 
# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date   
def voto(anoDeNascimento, anoAtual= date.today().year):
    idade = anoAtual - anoDeNascimento
    
    return permissaoPvotar(idade)

def permissaoPvotar(idade):
    if idade >= 65:
        return f'pode votar com {idade} de idade,\nmas voto não obrigatorio'
    elif idade >= 18:
        return f'deve votar com {idade} de idade,\n voto obrigatorio'
    elif idade >= 16:
        return f'pode votar com {idade} de idade,\nmas voto não obrigatorio'
    else:
        return f'nao pode votar com {idade} de idade\nvoce tem que esperar mais {16-idade} anos'

def l(): print('=-'*30 + '=')

variavel = int(input('que voce nasceu:'))
l()
print(f'voce {voto(variavel)}')
l()


