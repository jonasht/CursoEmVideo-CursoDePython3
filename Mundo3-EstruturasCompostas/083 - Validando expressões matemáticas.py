simbolos = []
c1 = c2 = 0
simbolos = input('\nexpressao:')
for i in simbolos:

    if i == '(':
        c1 = c1 + 1
    elif c1 >= 1 and i == ')':
        c2 = c2 - 1
print('empressão correta' if c1 + c2 == 0 else 'expressão incorreta')


# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.
