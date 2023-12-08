n1 = float(input('Digite um segmento: '))
n2 = float(input('Digite outro segmento: '))
n3 = float(input('Digite outro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel ser um triangulo!')
    if n1 == n2 == n3:
        print('É um triangulo Equilátero!')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('É um triangulo Isósceles!')
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print('É um triangulo Escaleno!')
else:
    print('Não é possivel')
