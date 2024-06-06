# Exercício Python 109: 
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108. 
import moeda as m


preco = float(input('digite preço R$: '))


print(f'a metade de {m.formatar_moeda(preco)} é {m.metade(preco, True)}')
print(f'o dobre de {m.formatar_moeda(preco)} é {m.dobro(preco, True)}')
print(f'aumentando 10% é {m.aumentar(preco, 10, True)}')
print(f'diminuindo 10% é {m.diminuir(preco, 10, True)}')

