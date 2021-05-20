nome = input('Qual seu nome completo?').strip()
lista = nome.split()
print('Primeiro nome: {}'.format(lista[0]))
print('Último nome: {}'.format(lista[len(lista)-1]))

# O número -1 é por conta da contagem da lista que começa em zero.