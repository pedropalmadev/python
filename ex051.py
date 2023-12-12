f = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for c in range (0,10):
    num = f + (r*c)
    print(' {} ->'.format(num), end='')
print(' FIM')
