import emoji
from random import randint
npc = randint(0, 10)
njogador = int(input('Escolha um número de 0 a 10:'))
totaltentativas = 1
while npc > njogador:
    njogador = int(input('Não foi dessa vez, tente novamente... para mais dessa vez:'))
    totaltentativas = totaltentativas + 1
while npc < njogador:
    njogador = int(input('Não foi dessa vez, tente novamente ...para menos dessa vez:'))
    totaltentativas = totaltentativas + 1
if npc == njogador:
    print('Computador: \033[1;33m{}\033[m \nJogador: \033[1;33m{}\033[m \nParabéns! Você acertou!'.format(npc, njogador))
    print('Foram feitas um total de {} tentativas.'.format(totaltentativas))
    print(emoji.emojize('{:^46}'.format(':fireworks:', use_aliases=True)))
