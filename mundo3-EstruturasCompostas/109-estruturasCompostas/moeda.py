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
