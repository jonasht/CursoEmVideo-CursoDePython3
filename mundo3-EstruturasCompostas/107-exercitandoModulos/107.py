import moeda as m


preco = float(input('digite preco: '))


print(f'a metade de R${preco} eh {m.metade(preco)}')
print(f'o dobre de R${preco} eh {m.dobro(preco)}')
print(f'aumentando 10%, eh {m.aumentar(preco, 10)}')
print(f'diminuindo 10% eh {m.diminuir(preco, 10)}')

