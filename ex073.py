brasileirao = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco da Gama','Bahia','Santos','Goiás','Coritiba','América-MG')
print('-=-'*12)
print(f'Os primeiros 5 colocados são: {brasileirao[0:5]}')
print('-=-'*12)
print(f'Os ultimos quatro colocados são: {brasileirao[-4:]}')
print('-=-'*12)
print(f'Time em ordem alfabética: {sorted(brasileirao)}')
print('-=-'*12)
c = brasileirao.index('Athletico-PR')
print(f'O Athletico-PR está na posição {c+1}° da tabela')
print('-=-'*12)
