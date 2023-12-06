from random import randint
from time import sleep
rdm = randint(0,5)
print('\033[1;33m-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=-' * 20 )
num = int(input('\033[mDigite um número de 0 a 5: '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(3)
print('O número da máquina foi: \033[1m{}\033[m'.format(rdm))
if num == rdm:
    print('Você \033[1;32mGANHOU\033[m, acertou o número da maquina!')
else:
    print('Você \033[1;31mPERDEU\033[m, errou o número da maquina!')


