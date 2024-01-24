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
    t = str(s).replace('.',',')
    return f'R${t}'

