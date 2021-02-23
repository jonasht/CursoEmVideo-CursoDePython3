#Exercício Python 097: 
# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.

def escrever(mensagem):
    print('~'*30)    
    print(mensagem)
    print('~'*30)
    
msg = input('mensagem: ')
escrever(msg)