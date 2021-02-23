from math import radians, sin, cos, tan
angulo = float(input('angulo: '))
seno = sin(radians(angulo))
print('o Ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))