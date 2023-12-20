valores = []
a = ''
while True:
    temp = int(input('Digite um número: '))
    if temp in valores:
        print('Valor duplicado, não vou adicionar...')
    else:
        valores.append(temp)
        print('Valor adicionado com sucesso...')
    a = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if a == 'N':
        break
    while a not in 'SN':
        a = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if a in 'S':
            a = ''
        else:
            break
valores.sort()
print(f'Os valores em ordem crescente são {valores}')

