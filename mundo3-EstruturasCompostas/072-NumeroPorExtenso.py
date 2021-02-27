#Exercício Python 072:
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
n = -1
numero = ('Zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('digite um numero [0:20]:'))
    if 0 <= n <=20:
        break
    print('o numero deve ser de 0 a vinte somente')
print('=-'*25)
print(f'O Numero digitado foi {numero[n]}')

