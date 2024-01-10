from operator import itemgetter
jogador = {'nome': str(input('Nome do Jogador: '))}
gols = list()
part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
tot = 0
for c in range(part):
    jogador['gols'] = int(input(f'Quantos gols fez na partida {c+1}: '))
    gols.append(jogador['gols'])
    tot += jogador['gols']
jogador['gols'] = gols
jogador['total'] = tot
print('-=-'*15)
print(jogador)
print('-=-'*15)
for k, v in jogador.items():
    print(f'{k.title()} = {v}')
print('-=-'*15)
for c in range(part):
    print(f' ==> Na partida {c+1}, fez {gols[c]}')
print(f'Foi um total de {jogador["total"]} gols')
print('-=-'*15)
