import datetime
ano = datetime.date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano - nasc
if idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade == 20:
    print('Categoria: SÊNIOR')
elif idade > 20:
    print('Categoria: MASTER')

