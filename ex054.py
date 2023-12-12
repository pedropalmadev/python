import datetime
maiores = 0
menores = 0
for c in range (0,7):
    data = int(input('Data de nascimento da pessoa:  '))
    hoje = datetime.datetime.today().year
    idade = hoje - data
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas atingiram a MAIORIDADE'.format(maiores))
print('{} pessoas ainda não antigiram a MAIORIDADE'.format(menores))
