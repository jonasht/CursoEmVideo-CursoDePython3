#Exercício Python 102: 
# Crie um programa que tenha uma função fatorial() 
# que receba dois parâmetros:
# o primeiro que indique o número a calcular e
# outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de
# cálculo do fatorial.

def fatorial(n, show=False):
    '''
    -> calcula um fatorial de um numero
    :para n: o numero para ser calculado
    :para show: (opcional) mostrar ou não aconta (False/True)
    :return: o valor do fatorial 'numero'
    '''
    fatorial = [i for i in range(1, 1+n)]
    soma = 1
    resposta = ''
    for i in fatorial:
        soma *= i
    if show:
        for i in fatorial:
            resposta += f'{i} X '
    
    return f'{resposta[:-2] }= {soma}' if resposta else soma
            
print(fatorial(5, True))
print(fatorial(9))
help(fatorial)
