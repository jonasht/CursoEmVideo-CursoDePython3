import moeda as m
from random import randint

# preco = float(input('digite preço R$: '))
preco = 200


m.resumo(preco, randint(1, 20), randint(1, 20))
