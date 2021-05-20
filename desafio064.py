print('O programa a baixo lê quantos números você quiser, para parar basta digitar 999. \nNo final você tera o total de números digitados e a soma entre eles.')
n = 0
soma = 0
totaln = 0
while n != 999:
    n = int(input('\nDigite um número inteiro [digite 999 p/ parar:'))
    soma = soma + n
    totaln = totaln + 1
print('Foram digitados {} números e a soma deles é igual a {}.'.format(totaln - 1, soma - 999))


'''
 
 RESOLUÇÃO GUANABARA - ele tirou a gambiara do -1 e - 999, duplicando o input dentro e fora do while:
 
n = 0
n = int(input('\nDigite um número inteiro [digite 999 p/ parar:'))
soma = 0
totaln = 0
while n != 999:
    soma = soma + n
    totaln = totaln + 1
    n = int(input('\nDigite um número inteiro [digite 999 p/ parar:'))
print('Foram digitados {} números e a soma deles é igual a {}.'.format(totaln, soma))

'''
