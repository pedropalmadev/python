geral = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(geral) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:])
    dados.clear()
    opc = str(input('Quer continuar? [S/N] ')).upper()
    if opc == 'N':
        break
print('-=' *30)
print(f'Os dados foram {geral}')
print(f'Ao todo, você cadastrou {len(geral)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in geral:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in geral:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
