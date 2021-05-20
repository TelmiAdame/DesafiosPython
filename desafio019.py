import random
n1 = str(input("Qual o nome do primeiro aluno?"))
n2 = str(input('Qual o nome do segundo aluno?'))
n3 = str(input('Qual o nome do terceiro aluno?'))
n4 = str(input('Qual o nome do quarto aluno?'))
lista = [n1, n2, n3, n4]
sorteado = random.choice(lista)
print('O professor tem 4 alunos: {}, {}, {} e {}. Hoje quem irá apagar o quadro é {}'.format(n1, n2, n3, n4, sorteado))


