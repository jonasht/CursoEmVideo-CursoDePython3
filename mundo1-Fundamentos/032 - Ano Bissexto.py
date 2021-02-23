from datetime import date
ano = int(input('QUAL ANO? use 0 para analisar o ano atual\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto\n'.format(ano))
else:
    print('o ano {} não é bissexto\n'.format(ano))
print('fim\n')


