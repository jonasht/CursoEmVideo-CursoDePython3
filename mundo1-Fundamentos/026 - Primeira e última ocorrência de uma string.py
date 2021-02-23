fr = str(input('frase: ')).upper().strip()
print('a letra A aparece {} vezes'.format(fr.count('A')))
print('a primeira letra A aparece na posição {}'.format(fr.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(fr.rfind('A')+1))
