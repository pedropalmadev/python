def notas(*n,sit=False):
    nota = dict()
    nota['total'] = len(n)
    f = c = 0
    maior = menor = n[0]
    while c < len(n):
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor =  n[c]
        f += n[c]
        c += 1
    med = f / len(n)
    nota['maior'] = maior
    nota['menor'] = menor
    nota['media'] = med
    if sit:
        if med >= 7:
            nota['situação'] = 'BOA'
        elif 5.5 <= med < 7:
            nota['situação'] = 'RAZOAVEL'
        else:
            nota['situação'] = 'RUIM'
    return nota
# Principal

resp = notas(5.5, 1, 2, 6.5, sit=True)
print(resp)

