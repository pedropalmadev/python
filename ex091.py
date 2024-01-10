from random import randint
from time import sleep
from operator import itemgetter
maior = 0
jogadores = {'jogador1': randint(1,6),
             'jogador2': randint(1,6),
             'jogador3': randint(1,6),
             'jogador4': randint(1,6)
             }
ranking = list()
for e, k in jogadores.items():
    print(f'O {e} tirou {k}')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'Em {i+1}° lugar: {v[0]} com {v[1]}')

