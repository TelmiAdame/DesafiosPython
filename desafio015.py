km = float(input('Quantos Km você percorreu com o carro? '))
dias = int(input('Por quantos dias você alugou o carro?'))
valor = dias * 60 + 0.15 * km
print('No total você pagará R${:.2f}'.format(valor))
