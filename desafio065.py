n = int(input('Digite um valor:'))
p = str(input('Deseja parar?').upper())
soma = n
total = 1
maior = n
menor = n
media = 0
while p != 'SIM':
    n = int(input('Digite um valor:'))
    p = str(input('Deseja parar?').upper())
    soma = soma + n
    total = total + 1
    if n > maior:
        maior = n
    else:
        maior = maior
    if n < menor:
        menor = n
    else:
        menor = menor
media = soma / total
print('A média dos valores foi de {}. O maior número digitado foi {} e o menor número digitado foi {}.'.format(media, maior, menor))
print('END')

# Guanabara fez se um jeito bem mais simples, mas não consegui compreender muito bem então mantive o meu mesmo. Seguimos o baile...