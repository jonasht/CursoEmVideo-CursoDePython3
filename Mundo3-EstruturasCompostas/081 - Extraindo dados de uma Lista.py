lista = []
print('type s to exit\ndigite s para sair')
while 1:
    num = input('N: ')

    if num == 's': break
    else: lista.append(int(num))

lista.reverse()
print('lista reversa', lista)
print('foram digitados', len(lista), ' numeros')
print('numero 5 foi digitado' if 5 in lista else 'sem 5')

#Exercício Python 081: 
# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.