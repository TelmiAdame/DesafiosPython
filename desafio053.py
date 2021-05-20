frase = str(input('Qual é a frase?')).strip().upper()
palavras = frase.split()
semespaco = ''.join(palavras)
inverso = ''
for letra in range(len(semespaco) - 1, -1, -1):
    inverso = inverso + semespaco[letra]
if inverso == inverso:
    print('PALÍNDROMO!')
else:
     print('NÃO É UM PALÍNDROMO')


#EM PYTHON O FOR PODE SER SUBSTITUIDO POR
# inverso = semespaco[:: -1]

