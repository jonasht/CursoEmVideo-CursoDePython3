#Exercício Python 043:
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#   30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

altura = float(input('qual é sua altura: '))
peso = float(input('qual é seu peso: '))

re = peso / (altura * altura)
print(re)
if re < 18.5:
    print('abaixo do peso')
elif re <= 25:
    print('peso ideal')
elif re <= 30:
    print('Sobrepeso')
elif re <= 40:
    print('Obesidade')
else:
    print('obesidade morbida')

