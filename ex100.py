from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores...', end=' ')
    for c in range(5):
        num = randint(1,10)
        sleep(0.3)
        print(f'{num}', end=' ')
        lista.append(num)
    sleep(0.3)
    print('PRONTO!')
def somapar(lista):
    s = 0
    for cont in range(len(lista)):
        if numeros[cont] % 2 == 0:
            s += numeros[cont]
    print(f'Somando os valores pares de {numeros}, temos {s}')

numeros = []
sorteia(numeros)
sleep(0.3)
somapar(numeros)
