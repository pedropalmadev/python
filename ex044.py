preco = float(input('Digite o preço: R$ '))
cond = int(input('Condição de pagamento:\nDigite 1 - Cheque/Dinheiro (10% de desconto)\nDigite 2 - Cartão à vista (5% de desconto)\nDigite 3 - 2x no cartão (preço normal)\nDigite 4 - 3x ou mais no cartão (20% de juros)\nQual sua opção: '))
if cond == 1:
    desc = preco - (preco*0.10)
elif cond == 2:
    desc = preco - (preco*0.05)
elif cond == 3:
    desc = preco
elif cond == 4:
    desc = preco + (preco*0.20)
    vezes = int(input('Em quantas vezes?: '))
    precof = desc / vezes
    print('Você pagará {}x parcelas de R${:.0f}'.format(vezes, precof, desc))
else:
    desc = 0
    print('Invalido, tente novamente!')
print('Sua compra de {} vai ter um  valor final é de R${}'.format(preco, desc))
