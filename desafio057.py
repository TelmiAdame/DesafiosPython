sexo = str(input('Qual seu sexo? Responda M(masculino) ou F(feminino)?')).upper().strip()[0]
while sexo != 'M' and sexo != 'F': #while seco not in 'MmFf'
    sexo = str(input('Resposta não classificada, responda novamente:')).upper().strip()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso, obrigada!')
elif sexo == 'F':
    print('Sexo Feminino registrado com sucesso, obrigada!')


