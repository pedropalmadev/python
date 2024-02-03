def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'"{entrada}" é um preço invalido')
        else:
            valido = True
            return float(entrada)

def leiaint(inp=''):
    while True:
        num = input(inp)
        if num.isnumeric():
            return int(num)
        else:
            print('ERRO! Digite um valor de número inteiro')
