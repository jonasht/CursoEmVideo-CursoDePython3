r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'

def l():print(g, '\n'+'=-'*30 + '=', f)

ns = [[], []]
n = 0

for i in range(0, 7):

  n = int(input(f'[{1+i}/7]digite um numero: '))
  if n % 2 == 0:
    ns[0].append(n)
  else:
    ns[1].append(n)
  
l()
ns[0].sort()
ns[1].sort()
l()
print(b, 'valores pares:\n')
for i in ns[0]:
    print(' ', i, end='')
l()
print(r, '\nvalores impares:\n')
for i in ns[1]:
    print(' ', i, end='')    

#Exercício Python 085: 
# Crie um programa onde o usuário possa digitar sete valores numéricos e
#  cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
