import time
ano_atual = time.localtime().tm_year
dados = {'nome': str(input('Nome: ')),
        'idade': int(input('Data de nascimento: '))}
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
dados['idade'] = ano_atual - dados['idade']
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['apostentadoria'] = ((dados['contratação'] + 35) - ano_atual + dados['idade'])
for e, k in dados.items():
    print(f'{e.title()} = {k}')

