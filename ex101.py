import datetime
def voto(age):
    if age >= 65 or 16 <= age < 18:
        return "OPCIONAL"
    elif age < 16:
        return "NEGADO"
    else:
        return "OBRIGATÓRIO"



ano = int(input('Ano de nascimento?: '))
ida = datetime.datetime.today().year - ano
print(f'Com {ida} anos: VOTO {(voto(ida))}')
