numeros = []
def limpar(): print("\n" * 100)

def l():print('\n'+'=-'*30 + '=')
print('escreva s para sair')
limpar()
l()
for i range(0, 7):
    l()
    entrada = input(f'[{i+1}] num:')
    limpar()
    if entrada == 's': break
    numeros.append(int(entrada))
limpar()
l()
print('numero.s digitado.s:')
for i in numeros:
    print(i, ' ', end='')
print('\nnumeros par.es')
for i in numeros:
    if i % 2 == 0:
        print(i, ' ', end='')
print('\nnumeros impar.es')
for i in numeros:
    if not(i % 2 == 0):
        print(i, ' ', end='')   
l()
#Exercício Python 085: 
# Crie um programa onde o usuário possa digitar sete valores numéricos e
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
