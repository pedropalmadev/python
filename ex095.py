from operator import itemgetter
lista = []
c = 0
while True:
    jogador = {'nome': str(input('Nome do Jogador: '))}
    gols = list()
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    tot = 0
    for c in range(part):
        gols.append(int(input(f'Quantos gols fez na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols[:])
    lista.append(jogador.copy())
    c += 1
    opc = str(input('Quer continuar? [S/N]: '))
    if opc in 'Nn':
        break
print(f'{"No.":<4}{"Nome":<12}{"Gols":>9}{"Total":>12}')

print('-'*40)
for k, v in enumerate(lista):
    print(f'{k:<3} ',end='')
    for d in v.values():
        print(f'{str(d):<16}',end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('VOLTE SEMPRE')
