import pygame, time, math
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen = pygame.display.set_mode((1000,800))
screen_mode = 0 #toggle fullscreen
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

pygame.display.set_caption('Testscript #001')

stickman = pygame.image.load('stickman.png')
stickman = pygame.transform.scale(stickman, (20, 30))
screen.blit(stickman, (50, 100))





dir_x = 500
dir_y = 350

jump = 0
jumpdir = 0
jumpaltitude = 0


while True:

    pygame.event.poll()

#check keys
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_w]:
        dir_y = dir_y-0.3
    if keys[pygame.K_s]:
        dir_y = dir_y+0.3
    if keys[pygame.K_a]:
        dir_x = dir_x-0.3
    if keys[pygame.K_d]:
        dir_x = dir_x+0.3
    if keys[pygame.K_SPACE] and jumpaltitude == 0:
        jump = 1
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
#toggle fullscreen        
    if keys[pygame.K_F11]:
        if screen_mode == 0:
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            screen_mode += 1
        else:
            screen = pygame.display.set_mode((1000,800))
            screen_mode += -1
        
#check borders left right   
    if dir_x > 900 and dir_y < 240 or dir_x > 900 and dir_y > 360:
        dir_x = 900
        print("x+border passed")
    if dir_x < 100 and dir_y < 240 or dir_x < 100 and dir_y > 360:
        dir_x = 100
        print("x-border passed")
        
#check door borders left right  
    if dir_x > 950 and dir_y > 250 or dir_x > 950 and dir_y < 350:
        dir_x = 950
        print("x+border passed")
    if dir_x < 50 and dir_y > 250 or dir_x < 50 and dir_y < 350:
        dir_x = 50
        print("x-border passed")
        
#check borders top bottom          
    if dir_y > 600:
        dir_y = 600
        print("y+border passed")
    if dir_y < 100:
        dir_y = 100
        print("y-border passed")

    if dir_x < 100 and dir_y > 350 or dir_x > 900 and dir_y > 350:
        dir_y = 350
        print("y+border passed")
    if dir_x < 100 and dir_y < 250 or dir_x > 900 and dir_y < 250:
        dir_y = 250
        print("y-border passed")
        
#    print(dir_y,dir_x)

        

#do jump cycle
    if jump == 1 and jumpdir == 0:
        jumpaltitude = jumpaltitude + 1
        if jumpaltitude > 10:
            jumpdir = 1
        dir_y -=jumpaltitude
    if jump == 1 and jumpdir == 1:
        jumpaltitude = jumpaltitude - 1
        if jumpaltitude == 0:
            jumpdir = 0
            jump = 0
        dir_y +=jumpaltitude + 1
    if not jumpaltitude == 0:
        print(jumpaltitude)

#set Position        
    screen.fill((0, 0, 0))
    screen.blit(stickman, (dir_x, dir_y))
    pygame.display.flip()


