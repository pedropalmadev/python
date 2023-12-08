casa = float(input('Valor da casa: '))
sala = float(input('Seu salário: '))
anos = int(input('Em quantos anos irá pagar: '))
mes = anos * 12
prestacao = casa / mes

if prestacao > (sala * 0.30):
    print('Empréstimo negado!')
else:
    print('Empréstimo liberado! você pagará parcelas de {:.2f} R$ por {} meses'.format(prestacao, mes))
