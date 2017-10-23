import pygame, time
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

pygame.display.set_caption('Testscript #001')

car = pygame.image.load('stickman.png')
screen.blit(car, (50, 100))

dir_x = 0
dir_y = 0

while True:

    pygame.event.poll()


    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_w]:
        dir_y = dir_y-10
    if keys[pygame.K_s]:
        dir_y = dir_y+10
    if keys[pygame.K_a]:
        dir_x = dir_x-10
    if keys[pygame.K_d]:
        dir_x = dir_x+10
    screen.fill((0, 0, 0))
    screen.blit(car, (dir_x, dir_y))
    pygame.display.flip()


