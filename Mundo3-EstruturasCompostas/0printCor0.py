r = '\033[31m'
def cprint(cor, frase):
    print(frase)
    print(cor)
    r = '\033[31m'
    print(cor, frase)
    
print(r, 'esta é uma frase' )
print('\033[31m vermelho')