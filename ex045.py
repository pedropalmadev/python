import random
import time
print('-'*20)
print('Vamos jogar pedra, papel e tesoura!')
print('-'*20)
player = str(input('Qual você quer? ')).upper()
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista).upper()
print('\n\033[1;34mPROCESSANDO...\033[m\n')
time.sleep(2)
print('-=-'*10)
comput = ('Computador escolheu: \033[1;7;40m {} \033[m'.format(pc))
if player == pc:
    print(comput)
    print('<'+'-'*20+'>')
    print('Você e o computador \033[1;33mEMPATARAM!\033[m ')
elif pc == 'PEDRA' and player == 'TESOURA' or pc == 'TESOURA' and player == 'PAPEL' or pc == 'PAPEL' and player == 'PEDRA':
    print(comput)
    print('<'+'-'*20+'>')
    print('Você \033[1;31mPERDEU\033[m para o computador!')
elif player == 'PEDRA' and pc == 'TESOURA' or player == 'TESOURA' and pc == 'PAPEL' or player == 'PAPEL' and pc == 'PEDRA':
    print(comput)
    print('<'+'-'*20+'>')
    print('Você \033[1;32mVENCEU\033[m do computador!')
else:
    print('\033[1;31mERROR: não foi reconhecido, insira apenas "pedra", "papel" ou "tesoura"\033[m')
print('-=-'*10)
