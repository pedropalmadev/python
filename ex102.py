def fato(num=1,show=False):
    """

    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    if show == True:
        print('Veja a conta com resolução!')
    else:
        print('Conta sem resolução (para ver, coloque o parâmetro SHOW = True).')
    for c in range(num,0,-1):
        f *= c
        if show == True:
            print(f'{c} = ' if c==1 else f'{c} x ', end='')
    return f



n = int(input('Número: '))
print(fato(n))
help(fato)
