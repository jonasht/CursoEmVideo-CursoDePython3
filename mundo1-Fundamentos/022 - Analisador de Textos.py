nome = str(input('Nome?: ')).strip()
print('tudo maiusculo {}'.format(nome.upper()))
print('tudo minusculo {}'.format(nome.lower()))
nses = nome.replace(' ', '')
print('QTD de letras sem espaço {}'.format(len(nses)))
nd = nome.split()
qtdpn = len(nd[0])
print('QTD de letras do primeiro nome {}'.format(qtdpn))