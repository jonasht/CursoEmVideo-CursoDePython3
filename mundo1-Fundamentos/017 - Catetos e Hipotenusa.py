'''co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente: '))
hi =(ca ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi))'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa mede {:.2f}'.format(hi))