import colorama 
colorama.init()

#Exercício Python 037:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#  1 para binário,
# 2 para octal e
# 3 para hexadecimal.
print('\33[7;32m  ')
valor = int(input('Qual é o valor decimal para converter? :'))
op = int(input('''\t1-binario
        2-octal
        3-hexadecimal
opção:'''))
if op == 1:
    print('Binario {}'.format(bin(valor)[2:]))
elif op == 2:
    print('octal {}'.format(oct(valor)[2:]))
elif op == 3:
    print('hexadecimal {}'.format(hex(valor)[2:]))
else:
    print('opção invalida')

