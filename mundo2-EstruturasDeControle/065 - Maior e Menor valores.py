n = int(input('Digite um numero:'))
print('digite 0 para parar')
c = 0

somar = menor = maior = n
while n != 0:
    n = int(input('Digite um numero:'))
    somar += n
    c += 1
    print('C:' + str(c))
    print(somar)
    if n > maior:
        maior = n
    elif n < menor and n != 0:
        menor = n

print('foi digitado {} e a media {:.2}'.format(c, somar / c))
print('O N maior foi {} e o menor {}'.format(maior, menor))
# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.