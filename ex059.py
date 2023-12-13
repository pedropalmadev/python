import time
menu = 0
print('\033[1m-'*82)
print('Você ira colocar dois valores e terá um menu de opções para utilizar nos valores!')
print('-\033[m'*82)
valor = int(input('Insira um valor: '))
valor2 = int(input('Insira outro valor: '))
while menu != 5:
    menu = int(input('\n\033[1;32m------ Menu ------\033[m\n[1] Somar \n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n\033[1mQual opção deseja:\033[m '))
    if menu == 1:
        print('\n\033[1;36mPROCESSANDO...\033[m')
        time.sleep(1)
        soma = valor + valor2
        print('\n\033[1;33mA soma dos valores são: {}\033[m '.format(soma))
        sn = int(input('\n[1] Voltar para o menu\n[2] Sair do programa\n\033[1mQual opção:\033[m  '))
        if sn == 2:
            break
        else:
            continue
    if menu == 2:
        print('\n\033[1;36mPROCESSANDO...\033[m')
        time.sleep(1)
        mult = valor * valor2
        print('\n\033[1;33mA multiplicação dos valores são: {}\033[m '.format(mult))
        sn = int(input('\n[1] Voltar para o menu\n[2] Sair do programa\n\033[1mQual opção:\033[m  '))
        if sn == 2:
            break
        else:
            continue
    if menu == 3:
        print('\n\033[1;36mPROCESSANDO...\033[m')
        time.sleep(1)
        maior = valor
        if valor2 > maior:
            maior = valor2
        print('\n\033[1;33mO maior valor é: {}\033[m '.format(maior))
        sn = int(input('\n[1] Voltar para o menu\n[2] Sair do programa\n\033[1mQual opção:\033[m  '))
        if sn == 2:
            break
        else:
            continue
    if menu == 4:
        valor = int(input('Insira um valor: '))
        valor2 = int(input('Insira outro valor: '))
    else:
        print('\033[1;31mOpção invalida\033[m')
print('\033[1;31mPrograma encerrado!\033[m')




