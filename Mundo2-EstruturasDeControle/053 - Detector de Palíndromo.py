#Exercício Python 053:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input(' digite uma frase: ')).strip().upper()
palavras = frase.split()
tjunto = ''.join(palavras)

inverso = tjunto[::-1]

if tjunto == inverso:
    print('essa palavra é palidromo')
else:
    print('essa palavra não é palidromo')
print('palavra normal {}, inversa {}'.format(tjunto, inverso))
