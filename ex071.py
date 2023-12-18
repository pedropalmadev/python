print('='*20)
print('BANCO')
print('='*20)
saque = int(input('Qual valor você quer sacar?: '))
print('='*20)
n50 = n20 = n10 = n1 = 0
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
                if saque == 0:
                    break
print(f'Você receberá\n{n50} notas de R$50\n{n20} notas de R$20\n{n10} notas de R$10\n{n1} notas de R$1')
print('='*20)
