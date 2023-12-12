soma = 0
cont = 0
for c in range (1,7):
    n = int(input('Número: '))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('Soma apenas dos {} números pares digitados é {}'.format(cont, soma))
