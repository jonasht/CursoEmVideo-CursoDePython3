from random import choice
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
list = [a1, a2, a3, a4]
escolhid = choice(list)
print("O aluno escolhido {}".format(escolhid))
