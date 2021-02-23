km = int(input('Km: '))
if km > 80:
    pre = 7 * (km - 80)
    print('multa de R${}'.format(pre))
else:
    print('sem multa')
