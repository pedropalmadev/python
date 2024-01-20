def ficha(n='<desconhecido>',g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


print('-'*30)
jog = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(g=gol)
else:
    ficha(jog,gol)
