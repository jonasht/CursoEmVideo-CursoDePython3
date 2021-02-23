numeros = []
impar = []
par = []
def l():
    print('=-'*30 + '=')
print('escreva s para sair')
l()
print('digite s p/ sair')
for i in range(0, 7):
    entrada = input(f'[{i}] num:')
    if entrada == 's':
        break
    else:
        numeros.append(int(entrada))
        if int(entrada) % 2 == 0:
            par.append(int(entrada))
        else:
            impar.append(int(entrada))
l()
print('numeros digitados:')
for i in numeros:
    print(i, ' ', end='')
print('\nnumeros par.es')
for i in par:
    print(i, ' ', end='')
print('\nnumeros impar.es')
for i in impar:
    print(i, ' ', end='')    
l()

#Exercício Python 085: 
# Crie um programa onde o usuário possa digitar sete valores numéricos e
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
