def leiaint(inp):
    while True:
        try:
            num = int(input(inp))
        except (TypeError, ValueError):
            print('\033[31mERRO: porfavor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def leiafloat(inp):
        while True:
            try:
                num = float(input(inp))
            except (TypeError, ValueError):
                print('\033[31mERRO: porfavor, digite um número real válido\033[m')
            except KeyboardInterrupt:
                print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
                return 0
            else:
                return num




n = leiaint('Digite um Inteiro: ')
r = leiafloat('Digite um Real: ')
print(f'Valor inteiro foi {n} e o real foi {r}')
