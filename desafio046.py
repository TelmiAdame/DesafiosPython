import emoji
from time import sleep
print('-=' * 20)
print("Aperte o play para iniciar a contagem.")
print(emoji.emojize('{:^51}'.format('\033[1;31;40m :arrow_forward: \033[m'), use_aliases=True))
print('-=' * 20)
for cont in range(10, -1, -1):
    print('{:^26}'.format(cont))
    sleep(1)
sleep(1)
print(emoji.emojize('{:^46}'.format('\033[0;33m:fireworks:\033[m', use_aliases=True)))
sleep(1)
print('{:^30}'.format('FELIZ ANO NOVOOO!!!'))
print('{:^30}'.format('01/01/2022'))



#fogos = pygame.image.load("fogos.jpg")
#print(fogos)