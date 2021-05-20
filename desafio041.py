from datetime import date
print('Confederação Nacional de Natação \nDescubra sua categoria.')
ano = int(input('Qual seu ano de nascimento?'))
idade = date.today().year - ano
if idade <= 9:
    print('Você pertence a categoria MIRIM.')
elif idade <= 14:
    print('Você pertence a categoria INFANTIL.')
elif idade <= 19:
    print('Você pertence a categoria JUNIOR.')
elif idade <= 25:
    print('Você pertence a categoria SÊNIOR.')
else:
    print('Você pertence a categoria MASTER.')
