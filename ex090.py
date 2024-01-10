aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
aluno['situação'] = 'Aprovado' if aluno['média'] >= 7 else 'Reprovado'
for v, k in aluno.items():
    print(f'{v.title()} --> {k}')
