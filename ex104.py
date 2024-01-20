def leiaint(inp=''):
    while True:
        num = input(inp)
        if num.isnumeric():
            return int(num)
        else:
            print('ERRO! Digite um valor de número inteiro')




n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
