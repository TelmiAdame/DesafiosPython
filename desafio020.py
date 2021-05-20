import random
n1 = input("Qual o nome do primeiro aluno?")
n2 = input('Qual o nome do segundo aluno?')
n3 = input('Qual o nome do terceiro aluno?')
n4 = input('Qual o nome do quarto aluno?')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('O professor tem 4 alunos: {}, {}, {} e {}. A ordem de apresentação será:{}'.format(n1, n2, n3, n4, lista))


