p = float(input('Qual é o preço desse produto? R$'))
comdesconto = p - (p * 5) / 100
print('O valor do produto com desconto de 5% será de R${:.f}'.format(comdesconto))
