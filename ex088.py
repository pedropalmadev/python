from random import randint
import time
lista = list()
jogos = list()
tot = 1
print('-='*30)
qnt = int(input('Quantos jogos você quer sortear?: '))
print('-=-' *5 +'  SORTEANDO  ' + '-=-'*5)
time.sleep(0.5)
while tot <= qnt:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.5)
print('-='*30)
