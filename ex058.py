from random import randint
from time import sleep
rdm = randint(0,10)
print('\033[1;33m-=-' * 20)
print('Vou pensar em um número entre 0 e 10 tente adivinhar...')
print('-=-' * 20 )
num = int
tent = 0
while num != rdm:
    num = int(input('\033[mDigite um número de 0 a 10: '))
    if num != rdm:
        print('Tente novamente você não acertou!')
        tent += 1
print('Você acertou o número da maquina, era {}'.format(rdm))
if num == rdm:
    print('Após {} jogadas você venceu!'.format(tent))

