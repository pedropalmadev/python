n1 = float(input('Digite um segmento: '))
n2 = float(input('Digite outro segmento: '))
n3 = float(input('Digite outro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel ser um triangulo!')
else:
    print('Não é possivel')
