n = int(input('digite um numero para somar:'))
somar = c = 0
while n != 999:
    somar += n
    c += 1
    n = int(input('digite um numero para somar:'))

print('foram {} digitados, total somados {}'.format(c, somar))