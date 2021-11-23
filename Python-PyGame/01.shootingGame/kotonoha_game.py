# -*- coding:utf-8 -*-
import pygame,sys,random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #create surfac object 
        #pygame.Surface((w,h))<= use this to create a image.
        self.image=pygame.Surface((60,60))
        self.image.fill("BlACK") # fill the color
        self.rect=self.image.get_rect() #
        self.rect.center=(screen_W/2,screen_H/2)
        self.speed = 20 #moving speed
        
    #method
    def update(self):
        #when keys pressed 
        keyslist=pygame.key.get_pressed()
        if keyslist[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed,0)
        if keyslist[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed,0)
        if keyslist[pygame.K_UP]:
            self.rect.move_ip(0,-self.speed)
        if keyslist[pygame.K_DOWN]:
            self.rect.move_ip(0,self.speed)
        
        # crush the wall
        if self.rect.right > screen_W:
            self.rect.right=screen_W
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > screen_H:
            self.rect.bottom = screen_H

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((1,30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(0, screen_W- self.rect.width)
        #self.rect.y = random.randrange(-100, -40)
        #self.speed_y = random.randint(2, 10)
        #self.speed_x = random.randrange(-3, 3)
        self.changeStatus()
    
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.top>=screen_H:
            self.changeStatus()
            
    def changeStatus(self):
        self.rect.x = random.randrange(0, screen_W- self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randint(2, 10)
        self.speed_x = random.randrange(-3, 3)
        
pygame.init()
screen_W,screen_H=(600,800)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
background = pygame.image.load("cute_girl.png")
screen=pygame.display.set_mode((screen_W,screen_H))
#pygame.display.set_caption("Sprite妖精")
clock=pygame.time.Clock()

player=Player()
#rock=Rock()
#make Sprite group
all_group=pygame.sprite.RenderUpdates(player)
#print(type(all_group)) #type check
#add sprit
all_group.add(player)
for i in range(80):
    rock=Rock()
    all_group.add(rock)

while True:
    screen.blit(background,(screen_W/5,screen_H/4))
    all_group.update()
    all_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
    
    #close windows
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()