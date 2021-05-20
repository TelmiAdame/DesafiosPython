from datetime import date
sexo = str(input('Qual seu sexo?')).strip().lower()
if sexo =='feminino':
    print('Seu alistamento não é obrigatório.')
if sexo == 'masculino':
  print('No Brasil o alistamente militar é obrigatório para homens, se informe sobre sua data a de alistamento.')
ano = int(input('Ano de nascimento:'))
anoatual = date.today().year
if ano == anoatual - 18:
    print('Não perca tempo, você precisa se alistar esse ano ainda!')
elif ano < anoatual - 18:
    print('Você já excedeu o prazo de alistamento em {} anos, não perca mais tempo, se alista já!'.format(anoatual - ano - 18))
elif ano > anoatual - 18:
    print('Ainda não chegou sua hora, mas prepare-se, você tem {} anos até o seu alistamento!'.format(18 - (anoatual - ano)))

# atual = date.today().year - assim você lê o programa independente do ano.
