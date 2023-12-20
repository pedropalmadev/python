lista = []
c = 1
while True:
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    opc = str(input("Quer continuar? [S/N]: ").strip().upper())
    if opc == "N":
            break
    while opc != "S" and opc != "N":
        opc = str(input("Continuar? [S/N]: ").strip().upper())
        if opc == "N":
            break
    c += 1

lista.sort(reverse=True)
print(f'Foram digitados {c} elementos')
print(f'A lista em ordem descrescente {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
