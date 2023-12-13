n = int(input('Fatorial de: '))
res = 1
cont = 1
while cont <= n:
     res *= cont
     cont += 1
print('O fatorial de {}! é igual a {}'.format(n, res))

'''res = 1
n = int(input('Fatorial: '))
for c in range (1,n+1):
    res *= c
print(res)'''

'''from math import factorial
n = int(input('Fatorial de: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''
