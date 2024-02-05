from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Arquivo'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        print('\033[33mSaindo do sistema... Até logo!\033[m')
        sleep(1)
        break
    else:
        print('\033[31mERRO: porfavor, escolha uma opção válida!\033[m')
    sleep(2)
