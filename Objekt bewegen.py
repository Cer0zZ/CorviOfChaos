import pygame, time, math
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

pygame.display.set_caption('Testscript #001')

car = pygame.image.load('stickman.png')
car = pygame.transform.scale(car, (20, 30))
screen.blit(car, (50, 100))

dir_x = 1
dir_y = 1
jumpsteps = 50
jumpamplitude = 70

jump = 0
jumpdir = 0
jumpaltitude = 0
while True:

    pygame.event.poll()


    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_w]:
        dir_y = dir_y-2
    if keys[pygame.K_s]:
        dir_y = dir_y+2
    if keys[pygame.K_a]:
        dir_x = dir_x-2
    if keys[pygame.K_d]:
        dir_x = dir_x+2
    if keys[pygame.K_SPACE] and jumpaltitude == 0:
        jump = 1
        print("springen")
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    
    if dir_x > 800:
        dir_x = 800
        print("x+border passed")
    if dir_x < -10:
        dir_x = -10
        print("x-border passed")
    if dir_y > 500:
        dir_y = 500
        print("y+border passed")
    if dir_y < -10:
        dir_y = -10
        print("y-border passed")

    if jump == 1 and jumpdir == 0:
        jumpaltitude = jumpaltitude+1
        if jumpaltitude > 10:
            jumpdir = 1
        dir_y -=jumpaltitude
    if jump == 1 and jumpdir == 1:
        jumpaltitude = jumpaltitude-1
        if jumpaltitude == 0:
            jumpdir = 0
            jump = 0
        dir_y +=jumpaltitude
    if not jumpaltitude ==0:
        print(jumpaltitude)
        
    screen.fill((0, 0, 0))
    screen.blit(car, (dir_x, dir_y))
    pygame.display.flip()



