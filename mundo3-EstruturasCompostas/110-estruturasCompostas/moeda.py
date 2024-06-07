def aumentar(n, porcentagem, formatar=False):
    '''
    :param n é preço
    :param porcentagem
    :param formatar
    :return
    '''
    n = n + (n * porcentagem/100)
    return formatar_moeda(n) if formatar else n

def diminuir(n, porcentagem, formatar=False):
    n = n - (n * porcentagem / 100)
    return formatar_moeda(n) if formatar else n

def dobro(n, formatar=False):
    n = n*2
    return formatar_moeda(n) if formatar else n


def metade(n,formatar=False):
    n = n/2
    return formatar_moeda(n) if formatar else n

def formatar_moeda(preco, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaA=10, taxar=5 ):
    print('-'*32)
    print('RESUMO DO VALOR'.center(31))
    print('-'*32)
    print(f'preço analisado:\t{formatar_moeda(preco)}')
    print(f'dobro do preço:\t\t{dobro(preco, True)}')
    print(f'metade do preço:\t{metade(preco, True)}')
    print(f'{taxaA}% de aumento:\t\t{aumentar(preco, taxaA, True)}')
    print(f'{taxar}% de redução:\t\t{diminuir(preco, taxar, True)}')
    
    print('-'*32)
