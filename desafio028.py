from random import randint
n = int(input('Escreva um número de 0 a 5:'))
s = randint(0, 5)
if n == s:
    print('Parabéns! Você acertou. O número sorteado foi: {}'.format(s))
else:
    print('Ahh que triste! Você errou. O número sorteado foi: {}'.format(s))
