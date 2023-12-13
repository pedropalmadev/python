sexo = ''
while sexo != 'F' and sexo != 'M' :
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente, aceita-se apenas [M] ou [F]')
print('Pronto! sexo {} registrado com sucesso!'.format(sexo))
