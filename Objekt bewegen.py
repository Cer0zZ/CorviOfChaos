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
        dir_y = dir_y-2
    if keys[pygame.K_s]:
        dir_y = dir_y+2
    if keys[pygame.K_a]:
        dir_x = dir_x-2
    if keys[pygame.K_d]:
        dir_x = dir_x+2
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
            screen = pygame.display.set_mode((width,height))
            screen_mode += -1
        
#check borders    
#    if dir_x > 900:
#        dir_x = 900
#        print("x+border passed")
#    if dir_x < 100:
#        dir_x = 100
#        print("x-border passed")
#    if dir_y > 600:
#        dir_y = 600
#        print("y+border passed")
#    if dir_y < 100:
#        dir_y = 100
#        print("y-border passed")
if dir_x > 900 and 100 < dir_y < 300 or 400 < dir_y < 600:
        dir_x = 900
        print("x-border passed")
    if dir_x == 900 and 300 < dir_y < 400:
            print("door")
    if dir_x < 100 and 100 < dir_y < 300 or 400 < dir_y < 600:
        dir_x = 100
        print("x-border passed")
    if dir_x == 100 and 300 < dir_y < 400:
            print("door")
    if dir_x < 100 or dir_x > 900:
                print("Next room!")
                pygame.quit()
                quit()
    if dir_y > 600:
        dir_y = 600
    if dir_y < 100:
        dir_y = 100

        
#check door left
    if 300 < dir_y < 400 and dir_x < 150:
        print("door")
#check door right
    if 300 < dir_y < 400 and dir_x > 850:
        print("door")

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
    if not jumpaltitude ==0:
        print(jumpaltitude)

#set Position        
    screen.fill((0, 0, 0))
    screen.blit(stickman, (dir_x, dir_y))
    pygame.display.flip()


