import time

while True:
    print('\033[42;30m~'*26)
    print(' SISTEMA DE AJUDA PyHELP  ')
    print('~'*26)
    com = str(input('\033[m Função ou Biblioteca (FIM para acabar) --> \033[40;7m')).lower()
    time.sleep(1)
    help(com)
    print('\033[m')
    if com == 'fim':
        break
print('\033[32;1mOBRIGADO POR USAR O PyHELP\033[m')
