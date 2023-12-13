f = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
termo = f
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Foi mostrado {} termos'.format(total))
print('FIM')
