casa = float(input('Valor da casa: R$ '))
sala = float(input('Seu salário: R$ '))
anos = int(input('Em quantos anos irá pagar: '))
mes = anos * 12
prestacao = casa / mes
print('Para pagar uma casa de R${} em {} anos'.format(casa, anos))
print('Sua prestação é de R${:.2f}'.format(prestacao))
if prestacao > (sala * 0.30):
    print('Empréstimo negado!')
else:
    print('Empréstimo liberado!'.format(prestacao, mes))
