totalidade = 0
mediaidade = 0
homens = 0
homemmaisvelho = 0
nomevelho = ''
mulheres = 0
mulheresjovens = 0
for c in range(0, 4):
    nome = str(input('Qual seu nome?'))
    idade = int(input('Qual a sua idade?'))
    print('Qual seu sexo? (F) Feminino (M) Masculino')
    sexo = str(input('')).strip()
    totalidade = totalidade + idade
    mediaidade = totalidade / 4
    if c == 0 and sexo == 'M':
        homemmaisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    if sexo == 'F':
        sexo = mulheres
        if idade < 20:
            mulheresjovens = mulheres + 1
print('A média de idade de grupo é {}. \nA idade do homem mais velhor é {}. \n{} mulheres possuem menos de 20 anos.'.format(mediaidade, nomevelho, mulheresjovens))

#if sexo in 'Mm'