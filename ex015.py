d = float(input('Quantos dias alugados?: ' ))
k = float(input('Quantos Km rodados?: '))
p = (60*d) + (0.15*k)
print('O valor com {:.0f} dias alugados e {}km rodados fica R${:.2f}'.format(d, k , p))
