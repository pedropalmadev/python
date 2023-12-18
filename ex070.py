nome = c = pmenor = ''
preco = q = p = menor = maior = produto_comprado = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    produto_comprado += 1
    c = str(input('Quer continuar? [S/N]: ')).upper()
    p += preco
    if c == 'N':
        break
    if produto_comprado == 1:
        menor = preco
        pmenor = nome
    else:
        if menor > preco:
            menor = preco
            pmenor = nome
    if preco > 1000.0:
        q += 1
print(f'O total de compra foi {p}')
print(f'Temos {q} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pmenor} que custa R${menor}')
