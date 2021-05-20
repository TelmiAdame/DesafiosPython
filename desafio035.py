print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Escreva o comprimento da primeira reta:'))
r2 = float(input('Escreva o comprimento da segunda reta:'))
r3 = float(input('Escreva o comprimento da terceira reta:'))
if r1 + r2 <= r3 and r2 + r3 <= r1 and r1 + r3 <= r2:
    print('Com essas três retas é possível construir um triângulo')
else:
    print('Com essas três retas, NÃO é possível construir um triângulo')
