import pygame
import random
import math
from filedef import *
from player import player
from food import food
from speedfood import speedfood
pygame.init()
fs = True
screen = pygame.display.set_mode((1920,1080),pygame.SCALED)
width, height = screen.get_size()
maplimit = 4000
whileCheck = True
bgx = bgy = 0
listfood = []
listspeedfood = []
bg = pygame.image.load("bg1.png")
playerObj = player(pygame.image.load("hoatiet/hoatiet-2/head.png"),pygame.image.load("hoatiet/hoatiet-2/body.png"),pygame.image.load("hoatiet/hoatiet-2/tail.png"))

#
for i in range(101):
    listfood.append(food())
    listspeedfood.append(speedfood())
xdraw = 960
ydraw = 540



def hoatdonggioihan():
    global xdraw, ydraw, width, height
    ### Giới hạn dưới 
    ytuongdoi = ydraw+(4000-playerObj.dodai[0][0][1])
    if ytuongdoi<=height:
        pygame.draw.rect(screen, (0,0,255), (0,ytuongdoi,width,height - ytuongdoi))

    ### Giới hạn trên
    ytuongdoi = ydraw+(-4000-playerObj.dodai[0][0][1])
    if ytuongdoi>=0:
        pygame.draw.rect(screen, (0,0,255), (0,0,width,ytuongdoi))

    ### Giới hạn trái
    xtuongdoi = xdraw+(-4000-playerObj.dodai[0][0][0])
    if xtuongdoi>=0:
        pygame.draw.rect(screen, (0,0,255), (0,0,xtuongdoi,height))

    ### Giới hạn phải
    xtuongdoi = xdraw+(4000-playerObj.dodai[0][0][0])
    if xtuongdoi<=width:
        pygame.draw.rect(screen, (0,0,255), (xtuongdoi,0,width-xtuongdoi,height))
    ### Die
    if (playerObj.dodai[0][0][0]>=4000)or(playerObj.dodai[0][0][0]<=-4000)or(playerObj.dodai[0][0][1]<=-4000)or(playerObj.dodai[0][0][1]>=4000):
        print("HIHI THUA ROI")
    
def fps():
    global bgx, bgy, xdraw,ydraw,width, height
    screen.blit(bg,(bgx, bgy))
    for i in listfood:
        i.draw(screen,xdraw,ydraw,width,height,playerObj)
    for y in listspeedfood:
        y.draw(screen,xdraw,ydraw,width,height,playerObj)
    playerObj.draw(screen,xdraw,ydraw)
    hoatdonggioihan()
    pygame.display.update()
def hoatdongchung():
    global bgx,bgy, width, height
    playerObj.hoatdong()
    bgx = -(playerObj.dodai[0][0][0]%90)
    bgy = -(playerObj.dodai[0][0][1]%88)
    i = 0
    while i < len(listfood):
        if (listfood[i].hoatdong(xdraw,ydraw,playerObj)):
            del listfood[i]
            i -= 1
        i += 1
    i = 0
    while i < len(listspeedfood):
        if (listspeedfood[i].hoatdong(xdraw,ydraw,playerObj)):
            del listspeedfood[i]
            i -= 1
        i += 1
            
            


while whileCheck:
    fps()
    hoatdongchung()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            whileCheck = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerObj.right()
                playerObj.turnright = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerObj.left()
                playerObj.turnleft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerObj.turnright = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerObj.turnleft = False
            if event.key == pygame.K_SPACE:
                pygame.display.quit()
                pygame.display.init()
                if fs:
                    screen = pygame.display.set_mode((960,540))
                    width = 960
                    height = 540
                    xdraw = 480
                    ydraw = 270
                    fs = False
                else:
                    screen = pygame.display.set_mode((1920,1080),pygame.SCALED)
                    width, height = screen.get_size()
                    
                    xdraw = int(width/2)
                    ydraw = int(height/2)
                    fs = True
















                
                
