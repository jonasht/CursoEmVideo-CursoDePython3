km = float(input('quantos km: '))
if km > 200:
    pre = km * 0.45
else:
    pre = km * 0.50
print('preço da pssagem: R${}'.format(pre))