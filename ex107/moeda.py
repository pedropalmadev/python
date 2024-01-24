def aumentar(n, x):
    return n + (n * x/100)


def diminuir(n, x):
    return n - (n * x/100)


def metade(n):
    x = n/2
    return x


def dobro(n):
    return n*2

def moeda(s):
    t = str(s).replace('.',',')
    return f'R${t}'

