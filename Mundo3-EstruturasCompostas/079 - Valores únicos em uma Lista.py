lista = []
print('=-='*20)
print('type s to exit')
print('digite s para sair')
while True:
    valor_Digitado = str(input('digite um valor:'))
    
    if 's' == valor_Digitado:
        break

    if valor_Digitado in lista:
        print('number was already typed\nnumero já foi digitado')
    else:
        lista.append(valor_Digitado)

lista.sort()
print('=-='*20)
print('it was typed the number s:')
print('foi digitado os numero s:')
for i in lista:
    print(i, ' ', end='')
#Exercício Python 079: 
#Crie um programa onde o usuário possa
#  digitar vários valores numéricos e
#  cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, 
# em ordem crescente. 