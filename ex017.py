import math
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
hy = math.hypot(co, ca)
print('Hipotenusa é {:.2f}'.format(hy))
