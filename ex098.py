from time import sleep
def contador(i, f, p):
    print(f'A contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
        print('FIM!')


contador(1,10,1)
contador(10,0,2)
print('   AGORA PERSONALIZE A CONTAGEM!   ')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
