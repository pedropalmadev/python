def aumentar(n, x, format=False):
    t = n + (n * x/100)
    return t if format is False else moeda(t)


def diminuir(n, x, format=False):
    t = n - (n * x/100)
    return t if format is False else moeda(t)


def metade(n, format=False):
    t = str(n).replace('.',',')
    x = n/2
    return x if format is False else moeda(x)


def dobro(n, format=False):
    x = n*2
    return x if format is False else moeda(x)

def moeda(s):
    return f'R$ {s:>.2f}'.replace(".", ",")


def resumo(n = 0, taxaa= 10, taxar = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n,taxaa, True)}')
    print(f'{taxar}% de redução:  \t{diminuir(n,taxar, True)}')
    print('-'*30)
