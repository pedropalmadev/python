lista = []
lista_par = []
lista_impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    opc = str(input("Quer continuar? [S/N]: ").strip().upper())
    if opc == "N":
            break
    while opc != "S" and opc != "N":
        opc = str(input("Continuar? [S/N]: ").strip().upper())
        if opc == "N":
            break

lista_par.sort()
lista_impar.sort()
lista.sort()
print(f'Lista PAR: {lista_par}')
print(f'Lista ÍMPAR: {lista_impar}')
print(f'Lista PADRÃO: {lista}')
