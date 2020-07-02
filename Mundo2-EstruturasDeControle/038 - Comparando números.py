#Exercício Python 038:
#  Escreva um programa que leia dois números inteiros e compare-os.
#  mostrando na tela uma mensagem:
#  - O primeiro valor é maior
# - O segundo valor é maior
#  - Não existe valor maior, os dois são iguais

num = int(input('N um:'))
ndois = int(input('N dois:'))
if num > ndois:
    print('o primeiro valor é maior')
elif ndois > num:
    print('o segundo valor é maior')
else:
    print('os dois valores são iguais')
print('fim de programa')