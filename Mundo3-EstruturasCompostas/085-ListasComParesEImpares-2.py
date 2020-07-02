def l():print('\n'+'=-'*30 + '=')
ns = [[], []]
n = 0

for i in range(0, 7):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        ns[0].append(n)
    else:
        ns[1].append(n)
l()
ns[0].sort()
ns[1].sort()
l():
print('valores pares:\n')
for i in ns[0]:
    print(' ', i, end='')
l()
print('\nvalores impares:\n')
for i in ns[1]:
    print(' ', i, end='')    

