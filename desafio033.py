n1 = int(input('Escreva o primeiro número:'))
n2 = int(input('Escreva o segundo número:'))
n3 = int(input('Escreva o terceiro número:'))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))