d = float(input('Qual a distância da sua viagem em km?'))
if d <= 200:
    print('O preço da sua passagem é R${:.2f}. Tenha uma boa viagem!'.format(d * 0.50))
else:
    print('O preço da sua passagem é R${:.2f}. Tenha uma boa viagem!'.format(d * 0.45))

# modo simplificado: preço = d * 0.50 if distância <= 200 else distância * 0.45