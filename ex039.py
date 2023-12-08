import datetime
ano = datetime.date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano - nasc
if idade < 18:
    print('Você faz {} anos em {}, ainda precisa esperar para se alistar'.format(idade, ano))
elif idade == 18:
    print('Você faz 18 anos em {}, está na hora de se alistar!'.format(ano))
elif idade > 18:
    print('Você faz {} anos em {}, já passou o tempo de se alistar!'.format(idade, ano))

