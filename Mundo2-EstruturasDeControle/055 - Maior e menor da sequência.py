

maior = menor = 0
for i in range(0, 5):
    peso = float(input('qual é peso da pessoa {}:'.format(i+1)))
    if i == 0:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {}Kg'.format(maior))
print('o menor peso foi {}Kg'.format(menor))
