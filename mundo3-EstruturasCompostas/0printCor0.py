import colorama
colorama.init() # p/ funcionar no windows, linux funciona normalmente


r = '\033[31m' # red
b = '\033[34m' # blue
g = '\033[32m' # green
f = '\33[m'
    
print('esta é uma frase')
print(r, 'vermelho red', f)
print(b, 'azul blue', f)
print(g, 'verde green', f)
