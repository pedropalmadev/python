frase = str(input('Digite um frase: ')).replace(' ',"").upper()
pal = frase[::-1]
print('O inverso de {} é {}'.format(frase, pal))
if frase == pal:
    print('É um palindromo!')
else:
    print('NÃO é um palindromo!')
