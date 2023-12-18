import random
p = v = c = s = q = 0
r = ''
print('-=-'*20)
print('Vamos jogar PAR OU ÍMPAR?')
while True:
    print('-=-'*20)
    v = int(input('Diga um valor: '))
    p = str(input('Par ou Ímpar? [P/I]: ')).upper()
    c = random.randint(1,10)
    s = v + c
    if s % 2 == 0:
        r = 'DEU PAR'
    else:
        r = 'DEU ÍMPAR'
    print('-'*20)
    print(f'Você jogou {v} e o computador {c}, total de {s} logo {r}')
    print('-'*20)
    if p == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            q += 1
        else:
            print('Você PERDEU!')
            break
    if p == 'I':
        if s % 2 == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            q += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {q} vezes')

