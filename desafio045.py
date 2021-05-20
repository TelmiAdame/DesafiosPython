import random
print('Jokempô')
ppt = str(input('Escolha seu elemento:'))
lista = ['pedra', 'papel', 'tesoura']
elemento = random.choice(lista)
if ppt == 'papel' and elemento == 'tesoura':
    print('Aahh você perdeu, {} perde de {}!'.format(ppt, elemento))
elif ppt == 'papel' and elemento == 'pedra':
    print('Aahh você ganhou, {} ganha de {}!'.format(ppt, elemento))
elif ppt == 'papel' and elemento == 'papel':
    print('Aahh empatamos, {} empata com {}!'.format(ppt, elemento))
elif ppt == 'pedra' and elemento == 'papel':
    print('Aahh você perdeu, {} perde de {}!'.format(ppt, elemento))
elif ppt == 'pedra' and elemento == 'tesoura':
    print('Aahh você ganhou, {} ganha de {}!'.format(ppt, elemento))
elif ppt == 'pedra' and elemento == 'pedra':
    print('Aahh empatamos, {} empata com {}!'.format(ppt, elemento))
elif ppt == 'tesoura' and elemento == 'pedra':
    print('Aahh você perdeu, {} perde de {}!'.format(ppt, elemento))
elif ppt == 'tesoura' and elemento == 'papel':
    print('Aahh você ganhou, {} ganha de {}!'.format(ppt, elemento))
elif ppt == 'tesoura' and elemento == 'tesoura':
    print('Aahh empatamos, {} empata com {}!'.format(ppt, elemento))

 # ''' from random import randint
 #intens = ('Pedra', 'Papel', 'Tesoura')
 #computador = randint (0,2)
 #pirnt('''Suas opções:
 #[0] PEDRA
 #[1] PAPEL
 #[2] TESOURA
 #Jogador = int(input('Qual é a sua jogada?'))
 #print('Computador jogou {}'.intens [jogador] ')
 #if computador == 0: #computador jogou PEDRA
    #if jogador == 0
        #print('EMPATOU')
    #elif jogador == 1
        #print('Jogador VENCE')
    #elif jogador == 2
        #print('COMPUTADOR VENDE')
    #else:
        #print('JOGADA INVÁLIDA')
 ##else computador == 1: #computador jogou PAPEL
    # if jogador == 0
        #print('COMPUTADOR VENDE')
    # elif jogador == 1
        #print('EMPATOU')
    # elif jogador == 2
        #print('Jogador VENCE')
    # else:
        #print('JOGADA INVÁLIDA')
 #else computador == 2: #computador jogou TESOURA
    # if jogador == 0
        #print('Jogador VENCE')
    # elif jogador == 1
        #print('COMPUTADOR VENDE')
    # elif jogador == 2
        #print('EMPATOU')
    # else:
        #print('JOGADA INVÁLIDA')