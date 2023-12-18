v = c = r = 0
while True:
    print('-'* 20)
    v = int(input('Quer ver a tabuada de qual valor? (digite valor negativo para parar): '))
    print('-'* 20)
    if v < 0:
        break
    for c in range (1,11):
        print(f'{v} x {c} = {v*c}')

print('PROGRAMA ENCERRADO!')

