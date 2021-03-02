# Exercício Python 106:
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.




vermelho = '\033[41m'
verde = '\033[42m'
amarelo = '\033[43m'
azul = '\033[44m'
f = '\033[m'


def ajudar(ajuda):
    print(azul)
    help(ajuda)
    print(f)
    
def l(char='', fim=''):
    print(char+'=-'*30+'=', fim)
    
def começar():
    while True:
        l(amarelo)
        print('sistema de ajuda Pyhelp')
        l()
        palavra = input('[digite sair p sair]\nfuncao ou biblioteca: ')
        l(fim=f)
        if palavra.upper() == 'SAIR': 
            print(f)
            break
        else:
            print(azul, f'acessando o comando {palavra}', f)
            ajudar(palavra)

começar()