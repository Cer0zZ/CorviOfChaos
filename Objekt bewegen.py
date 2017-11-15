import pygame, time, math
hight = 1000
width = 800
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen = pygame.display.set_mode((hight,width))
screen_mode = 0 #toggle fullscreen
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
deltat = clock.tick(FRAMES_PER_SECOND)

pygame.display.set_caption('Testscript #001')

stickman = pygame.image.load('stickman.png')
stickman = pygame.transform.scale(stickman, (20, 30))
screen.blit(stickman, (50, 100))

background = pygame.image.load('klassenzimmer_test.png')
screen.blit(background, [0, 0])


dir_x = 500
dir_y = 350

jump = 0
jumpdir = 0
jumpaltitude = 0

topborder = 100
bottomborder = 610
leftborder = 100
rightborder = 870

doordepht = 50
doortop = 350
doorbottom = 380


while True:

    pygame.event.poll()


    
##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Check keys of the Keyboard
################################################################################################## 
#check keys
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_w]:
        dir_y = dir_y-3
    if keys[pygame.K_s]:
        dir_y = dir_y+3
    if keys[pygame.K_a]:
        dir_x = dir_x-3
    if keys[pygame.K_d]:
        dir_x = dir_x+3
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
            screen = pygame.display.set_mode((hight,width))
            screen_mode += -1
            
##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Check Borders of the Room
##################################################################################################        
#check borders left right   
    if dir_x > rightborder and dir_y < (doortop-10) or dir_x > rightborder and dir_y > (doorbottom+10):
        dir_x = rightborder
        print("x+border passed")
    if dir_x < leftborder and dir_y < (doortop-10) or dir_x < leftborder and dir_y > (doorbottom+10):
        dir_x = leftborder
        print("x-border passed")
        
#check door borders left right  
    if dir_x > (rightborder+doordepht) and dir_y > doortop or dir_x > (rightborder+doordepht) and dir_y < doorbottom:
        dir_x = (rightborder+doordepht)
        print("x+border passed: Next Room")
    if dir_x < (leftborder-doordepht) and dir_y > doortop or dir_x < (leftborder-doordepht) and dir_y < doorbottom:
        dir_x = (leftborder-doordepht)
        print("x-border passed: Next Room")
        
#check borders top bottom          
    if dir_y > bottomborder:
        dir_y = bottomborder
        print("y+border passed")
    if dir_y < topborder:
        dir_y = topborder
        print("y-border passed")
#check door borders top bottom  
    if dir_x < leftborder and dir_y > doorbottom or dir_x > rightborder and dir_y > doorbottom:
        dir_y = doorbottom
        print("y+border passed")
    if dir_x < leftborder and dir_y < doortop or dir_x > rightborder and dir_y < doortop:
        dir_y = doortop
        print("y-border passed")
        
#    print(dir_y,dir_x)

##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Check if Jump --> if yes, jump
##################################################################################################        

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
    screen.blit(background, [0, 0])
    screen.blit(stickman, (dir_x, dir_y))
    pygame.display.flip()


