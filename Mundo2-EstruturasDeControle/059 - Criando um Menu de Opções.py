from time import sleep

n1 = int(input('valor um:'))

n2 = int(input('valor dois:'))
op = int(input('''[1] Somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
opção:'''))

while op != 5:


    if op == 1:
        print('somar {} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('multiplicar {} X {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O {} é maior'.format(n1))
        elif n1 == n2:
            print('o {} e {} são iguais'.format(n1, n2))
        else:
            print('O {} é maior'.format(n2))
    elif op == 4:
        n1 = int(input('valor um:'))
        n2 = int(input('valor dois:'))
    else:
        print('numero invalido')
    sleep(2)
    op = int(input('''    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    opção:'''))