verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
fim = '\033[m'
def leiaInt(mensagem):

    while True:
        l()
        n = input(amarelo + mensagem + fim)
        if n.isnumeric():
            ninteiro = int(n)
            break
        else:
            print(vermelho, 'erro, valor digitado não é inteiro\n'
                  'por favor digite um numero inteiro', fim)
    l() 
    return ninteiro
def l(): print(azul+'=-'*30+'='+fim)

n = leiaInt('digite um valor: ')
print(verde, f'voce digitou o valor {n} numero inteiro')