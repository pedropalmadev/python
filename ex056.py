velho = 0
menos = 0
idades = 0
nome_mais_velho = ''

for c in range(1, 5):
    nome = input('Nome da {} pessoa: '.format(c))
    idade = int(input('Idade da {} pessoa: '.format(c)))
    sexo = input('Sexo da {} pessoa (masculino/feminino): '.format(c)).lower()

    idades += idade
    mediat = idades / c

    if c == 1 and sexo == 'masculino':
        velho = idade
        nome_mais_velho = nome
    elif sexo == 'masculino':
        if idade > velho:
            velho = idade
            nome_mais_velho = nome
    if sexo == 'feminino' and idade < 20:
        menos += 1

print('A média de idade do grupo é {:.2f}'.format(mediat))  # Ajustei para mostrar a média com duas casas decimais
print('O nome do mais velho do grupo é {}'.format(nome_mais_velho).upper())
print('No total, abaixo de 20 anos, há {} mulher(es)'.format(menos))
