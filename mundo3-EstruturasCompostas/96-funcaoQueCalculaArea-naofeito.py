# Exercício Python 096:
# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e
# mostre a área do terreno.
def calcularArea(largura, comprimento):
    return largura * comprimento


print('=-'*30+'=')
largura = float(input('qual é a largura: '))
comprimento = float(input('qual é o comprimento: '))

resposta = calcularArea(largura, comprimento)
print(f'a area do terreno {largura}X{comprimento} é de {resposta}m²')

