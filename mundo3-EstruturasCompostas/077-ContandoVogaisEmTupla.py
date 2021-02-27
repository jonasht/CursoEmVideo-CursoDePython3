words=( 'aprender', 'programar', 'melhor', 'linguagem', 'programacao', 'mundo', 'learning', 'program', 'better', 'programme', 'language', 'world')

for i in words:
    print(f'\nword: {i.upper()} is= ', end='')
    for letter in i:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

# Exercício Python 077:
#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.