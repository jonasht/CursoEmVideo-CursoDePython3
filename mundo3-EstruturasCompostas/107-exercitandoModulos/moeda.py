def aumentar(n, porcentagem):
    n /= 100
    porcentagem += 100
    return f'{(n * porcentagem):.1f}'

def diminuir(n, porcentagem):
    n /= 100
    porcentagem -= 100
    return f'{(n * -porcentagem):.1f}'

def dobro(n):
    return n*2

def metade(n):
    return n/2

