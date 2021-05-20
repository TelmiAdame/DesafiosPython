salario = float(input('Qual o valor do seu salário atual?'))
if salario >= 1250:
    print('Seu salário com o aumento será de R${:.2f}'.format(salario * 0.10 + salario))
else:
    print('Seu salário com aumento será de R${:.2f}'.format(salario * 0.15 + salario))
