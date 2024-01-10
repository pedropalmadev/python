
todos = []
mulheres = []
idade = c = 0
while True:
    dados = {'nome': str(input('Nome: '))}
    dados['sexo'] = str(input('Sexo [M/F]: '))
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = input('Apenas [M/F]: ')
    dados['idade'] = int(input('Idade: '))
    todos.append(dados)
    idade += dados['idade']
    c += 1
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    opc = str(input('Quer continuar? [S/N]: '))
    if opc in 'Nn':
        break
media = idade/c
print(f'- O grupo tem {c} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- As pessoas que estão acima da média: ', end='')
for cont in range(0,c):
    if todos[cont]['idade'] > media:
            print(f'{todos[cont]["nome"]} ')
print('<-= ENCERRADO =->')
