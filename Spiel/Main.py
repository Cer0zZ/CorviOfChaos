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


background = pygame.image.load('Rooms/klassenzimmer_test.png')
screen.blit(background, [0, 0])




jump = 0
jumpdir = 0
jumpaltitude = 0


##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Player Class
##################################################################################################
topborder = 100
bottomborder = 610
leftborder = 100
rightborder = 870

doordepht = 50
doortop = 350
doorbottom = 380
class Player:
    def __init__(self,skin,x,y):
        self.object = pygame.image.load(skin)
        self.object = pygame.transform.scale(self.object, (20, 30))
        self.dir_x = x
        self.dir_y = y
    def setPosition(self,x,y):
        self.dir_x = x
        self.dir_y = y
    def MoveRight(self,amount):
        self.dir_x += amount
    def MoveLeft(self,amount):
        self.dir_x -= amount
    def MoveUp(self,amount):
        self.dir_y -= amount
    def MoveDown(self,amount):
        self.dir_y += amount
    def Display(self):
        screen.blit(self.object, (self.dir_x, self.dir_y))
        
    def DenyPosition(self):
    #check borders left right
        if self.dir_x > rightborder and self.dir_y < (doortop-10) or self.dir_x > rightborder and self.dir_y > (doorbottom+10):
            self.dir_x = rightborder
            print("x+border passed")
        if self.dir_x < leftborder and self.dir_y < (doortop-10) or self.dir_x < leftborder and self.dir_y > (doorbottom+10):
            self.dir_x = leftborder
            print("x-border passed")
            
    #check door borders left right  
        if self.dir_x > (rightborder+doordepht) and self.dir_y > doortop or self.dir_x > (rightborder+doordepht) and self.dir_y < doorbottom:
            self.dir_x = (rightborder+doordepht)
            print("x+border passed: Next Room")
        if self.dir_x < (leftborder-doordepht) and self.dir_y > doortop or self.dir_x < (leftborder-doordepht) and self.dir_y < doorbottom:
            self.dir_x = (leftborder-doordepht)
            print("x-border passed: Next Room")
            
    #check borders top bottom          
        if self.dir_y > bottomborder:
            self.dir_y = bottomborder
            print("y+border passed")
        if self.dir_y < topborder:
            self.dir_y = topborder
            print("y-border passed")
    #check door borders top bottom  
        if self.dir_x < leftborder and self.dir_y > doorbottom or self.dir_x > rightborder and self.dir_y > doorbottom:
            self.dir_y = doorbottom
            print("y+border passed")
        if self.dir_x < leftborder and self.dir_y < doortop or self.dir_x > rightborder and self.dir_y < doortop:
            self.dir_y = doortop
            print("y-border passed")

##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Check keys of the Keyboard
################################################################################################## 

def CheckKeys():
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_w]:
        Spieler.MoveUp(3)
    if keys[pygame.K_s]:
        Spieler.MoveDown(3)
    if keys[pygame.K_a]:
        Spieler.MoveLeft(3)
    if keys[pygame.K_d]:
        Spieler.MoveRight(3)
    if keys[pygame.K_SPACE] and jumpaltitude == 0:
        jump = 1
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()       
    if keys[pygame.K_F11]:
        if screen_mode == 0:
            screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            screen_mode += 1
        else:
            screen = pygame.display.set_mode((hight,width))
            screen_mode += -1
##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Display on Screen, what will be visible
##################################################################################################   

def DisplayOnScreen():
    pygame.event.poll()
    screen.blit(background, [0, 0])
    Spieler.DenyPosition()
    Spieler.Display()
    pygame.display.flip()

##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---While true Loop
##################################################################################################  

Spieler = Player("Skins/stickman.png",200,200)

while True:
    DisplayOnScreen()
    CheckKeys()



##################################################################################################
#§§§§§§§§§§§§§§§§§§§§§---Things to make new (think about better solutions)
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

    


