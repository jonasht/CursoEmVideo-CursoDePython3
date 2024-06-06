def aumentar(n, porcentagem):
    n /= 100
    porcentagem += 100
    return f'{(n * porcentagem):.2f}'.replace('.',',')

def diminuir(n, porcentagem):
    n /= 100
    porcentagem -= 100
    return f'{(n * -porcentagem):.2f}'.replace('.',',')

def dobro(n):
    return f'{(n*2):.2f}'.replace('.',',')

def metade(n):
    return n/2

