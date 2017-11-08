import pygame, time
from pygame.transform import scale
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

pygame.display.set_caption('Testscript #001')

car = pygame.image.load('Beispiel.png')
car = pygame.transform.scale(car, (int(492.4), int(206.2)))

Background = pygame.image.load('Beispiel.jpg')
Background = pygame.transform.scale(Background, (int(1280), int(1024)))
#Bild wird an des Format des Bildschirm angepasst

dir_x = 0
dir_y = 0
    

while True:

    pygame.event.poll()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dir_y = dir_y-10
    if keys[pygame.K_s]:
        dir_y = dir_y+10
    if keys[pygame.K_a]:
        dir_x = dir_x-10
    if keys[pygame.K_d]:
        dir_x = dir_x+10
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if dir_x > 850:
        dir_x = 850
    if dir_x > -100:
        dir_x = -100
    if dir_y > 100:
        dir_y = 100
    if dir_y > -2000:
        dir_y = -2000
    screen.blit(Background, (0,0))
    screen.blit(car, (dir_x, dir_y))
    pygame.display.flip()
