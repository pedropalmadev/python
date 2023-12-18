h = m = i = s = q = 0
c = ''
while True:
    print('-'*21)
    print(' CADASTRE UMA PESSOA ')
    print('-'*21)
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    if s not in 'MF':
        while s not in 'MF':
            s = str(input('Sexo [M/F]: ')).upper()
    print('-'*20)
    c = str(input('Quer continuar? [S/N]: ')).upper()
    if c == 'N':
        break
    elif c != 'S':
        break
    if i > 18:
        q += 1
    if s == 'M':
        h += 1
    if i < 20 and s == 'F':
        m += 1
print('-=- FIM DO PROGRAMA -=-')
print(f'Total de pessoas com mais de 18 anos: {q}')
print(f'Temos ao todo {h} homen(s) cadastrados')
print(f'Temos {m} mulher(res) com menos de 20 anos')
