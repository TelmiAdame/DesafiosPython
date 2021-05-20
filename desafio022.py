nome = str(input('Qual seu nome completo?'))
print('Seu nome escrito em maiúsculo:', nome.upper())
print('Seu nome escrito em minusculo:', nome.lower())
semespaço = nome.replace(' ', '')
print('Seu nome completo tem:', len(semespaço), 'letras')
# OU print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
lista = nome.split()
print('Seu primeiro nome tem:', len(lista[0]), 'letras')






