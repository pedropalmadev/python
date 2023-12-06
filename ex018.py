import math
ang = float(input('Digite um angulo: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o SENO igual a {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o COSSENO igual a {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem a TANGENTE igual a {:.2f}'.format(ang, tan))
