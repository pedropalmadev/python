vel = int(input('Velocidade do carro: '))
muta = (vel - 80) * 7
if vel >= 80:
    print('Você foi mutado no valor de R${}'.format(muta))
else:
    print('Você está percorrendo de acordo com a lei!')
