lista = []

for i in range(5):
    
    num = int(input('N:'))
    
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print(f'adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'adicionado {posicao} da lista')
                break
            posicao += 1
print('||', '-==' *10, '||')
print(lista)
print('os valores foram: ', end='')
for printar in lista:
    print(printar, end=', ')
    
# Exercício Python 080: 
# Crie um programa onde
# o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.    