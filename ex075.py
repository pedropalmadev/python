tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'O valor 9 apareceu {tupla.count(9)} veze(s)')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu na lista')
print(f'Os valores pares são: ', end='')
c = []
for n in tupla:
    if n % 2 == 0:
        print(n, end = ' ')

