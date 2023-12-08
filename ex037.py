import time
num = int(input('Digite um número: '))
print('-'*10)
print('Você digitou o número \033[1;32m{}\033[m para qual base quer converter?: '.format(num))
print('-'*10)
base = int(input('Digite \033[1;33m1\033[m - Bínario \nDigite \033[1;33m2\033[m - Octal \nDigite \033[1;33m3\033[m - Hexadecimal \n\033[1m------->  : \033[m'))
print('PROCESSANDO...')
time.sleep(2)
print('-' *20)
if base == 1:
   binar = bin(num)[2:]
   print('Convertendo para bínario: {}'.format(binar))
   print('-' *20)
elif base == 2:
    octal = oct(num)[2:]
    print('Convertendo para octal: {}'.format(octal.upper()))
    print('-' *20)
elif base == 3:
    hexad = hex(num)[2:]
    print('Convertendo para hexadecimal: {}'.format(hexad.upper()))
    print('-' *20)
else:
    print('Opção invalida, tente novamente!')
    print('-' *20)
