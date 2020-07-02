n = int(input('N: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando Nº {}'.format(n))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

