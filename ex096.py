def area (a, b):
    ar = a * b
    linha()
    print(f'A área de um terreno {a}x{b} é de {ar}m².')
def linha():
    print('-'*30)


print('   Controle de Terrenos   ')
linha()
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))

