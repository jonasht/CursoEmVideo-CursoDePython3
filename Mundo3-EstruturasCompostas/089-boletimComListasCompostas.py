lista = list()
def l(): print(30*'-')
l()
print('s para sair em nome')
while 1:
    nome = str(input('nome: ').lower())
    if nome =='s': break 
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
l()    
print(f'{"No.":<5}{"nome":<10}{"media":>10}')
for i, p in enumerate(lista):
    print(f'{i:<5}{p[0]:<10}{p[2]:>10}')
l()
print('digite s para sair\n qual aluno quer ver as notas')
while 1:
    op = input('n:') 
    if op == 's':
        break
    l()
    print(f'nome: {lista[int(op)][0].title()}\nnotas: {lista[int(op)][1]}')   