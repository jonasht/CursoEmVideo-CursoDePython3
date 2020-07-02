#Exercício Python 042:
# Refaça o DESAFIO 035 dos triângulos,
#acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes


print('\33[32m - -'*30)
print('analisador de triangulos')
print(' - - '*30 + '\33[m')

r1 = float(input('primeiro segmento:'))
r2 = float(input('segundo segmento:'))
r3 = float(input('terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos {}, {} e {}, formam um triangulo '.format(r1, r2, r3), end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('os segmentos {}, {} e {}, NÂO formam um triangulo'.format(r1, r2, r3))

