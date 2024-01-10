lista = [[],[]]
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-='*20)
print(f'Os valores pares em ordem crescente são {lista[0]}')
print(f'Os valores impares em ordem crescente são {lista[1]}')
