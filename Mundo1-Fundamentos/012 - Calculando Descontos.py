pe = float(input('preço?: '))
des = pe - (pe*5/100)
print('desconte de 5% de R${:.2f}, são {:.2f} reais '.format(pe,des))