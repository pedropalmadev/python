peso = float(input('Peso (kg): '))
alt = float(input('Altura (m): '))
imc = peso / (alt**2)
print('O imc é de {:.2f}\n'.format(imc))
if imc < 18.5:
    print('Você está baixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está no sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')

