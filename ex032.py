import datetime
ano = int(input('Qual ano analisar? (coloque 0 para ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))
