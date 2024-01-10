matriz = [[0,0,0], [0,0,0], [0,0,0]]
ter_col = maior = par = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {[l,c]}: '))

        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            ter_col += matriz[l][c]
        if l == 2:
            maior = matriz[1][0]
            if matriz[1][1] > maior:
                maior = matriz[1][1]
            elif matriz[1][2] > maior:
                maior = matriz[1][2]

print('-=' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[  {matriz[l][c]}  ]', end='')

    print()
print(f'A soma de todos os pares é {par}')
print(f'A soma da terceira coluna é {ter_col}')
print(f'O maior valor da segunda linha é {maior}')
