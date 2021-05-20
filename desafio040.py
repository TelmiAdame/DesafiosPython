print('Olá querido aluno, escreva suas notas abaixo e saiba seu resultado final do ano letivo:')
portugues = float(input('Português nota:'))
matematica = float(input('Matemática nota:'))
if (portugues + matematica) / 2 < 5:
    print('Lamento, você foi REPROVADO.')
elif ((portugues + matematica) / 2) > 4 and ((portugues + matematica) / 2) < 7:
    print('Você está de RECUPERAÇÃO.')
elif (portugues + matematica) / 2 >= 7:
    print('Parabéns, você foi APROVADO!')

