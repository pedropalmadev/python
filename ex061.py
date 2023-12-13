f = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
termo = f
while c <= 10:
    print(' {} ->'.format(termo), end='')
    termo += r
    c += 1
print(' FIM')

