def maior(*num):
    print('-=-'* 20)
    print('Analisando os valores passados...')
    print(f'{num} foram informados {len(num)} valores ao todo')
    mai = num[0]
    for c in range(len(num)):
        if num[c] > mai:
            mai = num[c]
    print(f'O maior valor informado é o {mai}')
    print('-=-'* 20)

maior(1,4,5,9,10,2,4)
maior(4,5,1,19,4)
maior(1,0,-4,2)

