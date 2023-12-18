t = ('Pão', 2, 'Café', 3.5,'Misto',5,'Suco',5,'Refri',6,'Batata',8)
print('-'*40)
print(' '*10,'LISTAGEM DE PREÇO',' '*8)
print('-'*40)
for pos in range(0,len(t)):
    if pos % 2 == 0:
        print(f'{t[pos]:.<30}', end='')
    else:
        print(f'{t[pos]:>6.2f} R$')
print('-'* 40)
