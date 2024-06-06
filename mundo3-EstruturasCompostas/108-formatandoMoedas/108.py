
import moeda as m


preco = float(input('digite preço R$: '))


print(f'a metade de R${preco} é {m.metade(preco)}')
print(f'o dobre de R${preco} é {m.dobro(preco)}')
print(f'aumentando 10% é {m.aumentar(preco, 10)}')
print(f'diminuindo 10% é {m.diminuir(preco, 10)}')

