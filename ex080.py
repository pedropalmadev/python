num = []
maior = menor = 0
for cont in range(0,5):
    v = (int(input('Digite um número: ')))
    if cont == 0 or v > num[-1]:
        num.append(v)
    else:
        pos = 0
        while pos < len(num):
            if v <= num[pos]:
                num.insert(pos, v)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {num}')
