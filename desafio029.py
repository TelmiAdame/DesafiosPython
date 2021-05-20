velocidade = float(input('Qual a velocidade do carro?'))
if velocidade < 80:
    print('Você está dirigindo com segurança, parabéns!')
else:
    print('Você exedeu o limite de velocidade que é de 80km/h, sua multa será de R${:.2f}'.format((velocidade -80) * 7))
