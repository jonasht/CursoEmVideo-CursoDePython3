numeros = []
par = []
impar = []

print('"s" for finishing //"s" para sair')
while 1:
    n = input('num: ')
    if n == 's':
        break
    elif int(n) % 2 == 0:
        par.append(int(n))
    else:
        impar.append(int(n))
        
    numeros.append(int(n))    
print('foram digitados:')
for i in numeros:
    print(i, ' ', end='')

print('\neven number.s// par.es:')
for ii in par:
    print(ii, ' ', end='')
print('\n odd number.s// impar.es:')    
for iii in impar:
    print(iii, ' ', end='')    

    