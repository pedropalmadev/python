sal = float(input('Digite seu salário: '))
if sal > 1250.0:
    aum = sal * 0.10
else:
    aum = sal * 0.15
qnt = sal + aum
print('Você teve um aumento de R${} e seu salário atual é de R${:.1f}'.format(aum, qnt))
