palavras = ('Comida','Fome','Vontade','Sexo',
            'Estudar','Praticar','Python','Aprender')
for p in palavras:
    print(f'\nNa palavras {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(),end=' ')

