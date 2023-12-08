n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n2 > n1:
    print('O segundo valor é o maior, sendo ele {}'.format(n2))
elif n1 > n2:
    print('O primeiro valor é o maior, sendo ele {}'.format(n1))
elif n1 == n2:
    print('Os dois valores são iguais!')

