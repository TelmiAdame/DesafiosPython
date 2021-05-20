frase = input('Escreva uma frase:').lower().strip()
print('Quantas vezes a letra a aparece?', frase.count('a'))
print('Em que posição aparece o primeiro a ?', frase.find('a')+1)
print('Em quem posição aparece o último a ?', frase.rfind('a')+1)

# O +1 é por conta da contagem que começa em zero.
