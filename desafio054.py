from datetime import date
ano = date.today().year
idade = 0
somamaior = 0
somamenor = 0
total = 0
for c in range(0, 7):
    nascimento = int(input('Qual sua data de nascimento?'))
    idade = ano - nascimento
    if idade > 1 >= 21:
        somamaior = somamaior + 1
    if idade > 1 < 21:
        somamenor = somamenor + 1
    else:
        print('Você digitou uma data inválida, tente novamente.')
print('No total foram cadastradas {} pessoas, delas {} são maiores de idade e {} são menores de idade. \n** 21 anos p/ ser maior de idade'.format(somamaior + somamenor, somamaior, somamenor))







