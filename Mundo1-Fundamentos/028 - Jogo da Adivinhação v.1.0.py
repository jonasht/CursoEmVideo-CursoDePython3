import random
p = random.randint(1, 6)
print(p) # para saber o n correto antes
r = int(input('N: '))
while not(r == p):
    print ('incorreto' if not(r == p) else 'correto')
    r = int(input('N: '))
