#Exercício Python 057:
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo ='sa'

sexo = str(input('Sexo [M/F/N]: ')).strip().upper()[0]

while sexo not in 'MFN':
    print('Sexo invalido')
    sexo = str(input('Sexo>\nMasculino\nFeminino\nNeutro\nopção [M/F/N]: ')).strip().upper()[0]
print('Sexo {} valido'.format(sexo))
