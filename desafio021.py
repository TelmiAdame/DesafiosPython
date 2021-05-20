import pygame
pygame.init()
pygame.mixer.init()
tempo = pygame.time.Clock()
pygame.mixer.music.load('house_lo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    print("tocando...")
    tempo.tick(1000)



