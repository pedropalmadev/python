n = 0
qnt = 0
num = 0
n = int(input('Digite valores (pare digitando 999): '))
while n != 999:
        qnt += 1
        num += n
        n = int(input('Digite valores (pare digitando 999): '))
print('Foram digitados {} números com uma soma no total de {}'.format(qnt, num))
