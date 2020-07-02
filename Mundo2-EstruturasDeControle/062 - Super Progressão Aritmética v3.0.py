

pt = int(input('primeiro termo:'))
ra = int(input('Razão:'))

termo = pt
i = v = 1
while v != 0:
    while i <= 10:
        print(' {} ->'.format(termo), end='')
        termo += ra
        i += 1
    print('Pausa')
    v = int(input('\nquantos mais:'))
    i -= v
print('\nFIM')