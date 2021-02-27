# Exercício Python 099: 
# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e
# dizer qual deles é o maior.
def l(qtd=30): print('=-'*qtd + '=')
def maior(*numeros):
    l()
    print(f'foram informados os valores:\n{numeros}, {len(numeros)} valores')
    print(f'o maior valor{max(numeros)}')
    l()


maior(2,3,5,6,7,9,4,4,8)
maior(2,3,6,9,8)
maior(2,3,3,9,4,4,8)