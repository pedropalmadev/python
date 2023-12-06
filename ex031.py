dis = float(input('Digite a distância de sua viagem: '))
if dis <= 200:
    pre = dis * 0.5
else:
    pre = dis * 0.45
print('Percorrendo {:.0f}km o valor da sua viagem fica R${}'.format(dis, pre))
