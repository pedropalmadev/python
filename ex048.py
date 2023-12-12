soma = 0
cont = 0
for c in range(1,501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
            cont += 1
print('Soma de {} números impares multiplos de três de 1 a 500 é: {}'.format(cont, soma))
