
c = 1
maior = soma = sn = menor = 0

while sn != 1:
    valor = int(input('Insira um valor: '))
    sn = int(input('[1] Finalizar\n[2] Adicionar mais valores\nQual sua opção?: '))
    soma += valor
    if valor < menor or menor == 0:
        menor = valor
    if valor > maior:
        maior = valor
    media = soma / c
    c += 1
    if sn != 1 and sn != 2:
        errno('Digite valores validos')
print('O maior é {}, sua média {:.2f} e o menor é {}'.format(maior,media, menor))

