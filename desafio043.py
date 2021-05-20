print('Cálcule seu IMC')
peso = float(input('Qual seu peso atual?'))
altura = float(input('Qual sua altura?'))
IMC = peso / (altura * altura)
print('Seu IMC atual é {}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso ideal.')
elif IMC >= 18.5 and IMC <= 25:
    print('Você está no seu peso ideal.')
elif IMC > 25 and IMC <= 30:
    print('Você está com sobrepeso.')
elif IMC > 30 and IMC <= 40:
    print('Você está com obesidade.')
else:
    print('Obesidade mórbida.')
