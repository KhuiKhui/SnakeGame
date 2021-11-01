import pygame
from filedef import *
class player:
    x = 0
    y = 0
    eat = 0
    angle = 90
    movetime = 0
    speed = 50
    speedup = 0
    dodai = []
    turnright = False
    turnleft = False
    
    def __init__(self,hoatiethead,hoatietbody,hoatiettail):
        self.angle = 90
        self.hoatiethead = hoatiethead
        self.hoatietbody = hoatietbody
        self.hoatiettail = hoatiettail
        for i in range(0, 100):
            self.dodai.append([[0,i],90])
    def move(self):
        
        self.x += math.cos(self.angle/180*math.pi)
        self.y -= math.sin(self.angle/180*math.pi)

        if (self.eat <= 0):
            self.dodai.pop(-1)
        self.eat -= 1
        self.dodai.insert(0,[[self.x,self.y],self.angle])

    def hoatdong(self):
        if (pygame.time.get_ticks() - self.movetime >= self.speed):
            self.movetime = pygame.time.get_ticks()
            if self.speedup == 0:
                if self.speed == 25:
                    self.speed = 50
            else:
                self.speedup -= 1
            self.move()
        if self.turnleft:
            self.left()
        if self.turnright:
            self.right()
    def left(self):
        if self.angle > 0:
            self.angle -= 1
        else:
            self.angle = 359
    def right(self):
        if self.angle < 360:
            self.angle += 1
        else:
            self.angle = 1
    def draw(self,screen,xdraw,ydraw):
        
        for i in range(1,len(self.dodai)-1):
            hinhanhquay = rot_center(self.hoatietbody,self.dodai[i][1]-90,chuyendoitoadoconran(self.dodai[i][0],self.dodai[0][0],[xdraw,ydraw]))
            screen.blit(hinhanhquay[0],hinhanhquay[1])
        hinhanhquay = rot_center(self.hoatiettail,self.dodai[-1][1]-90,chuyendoitoadoconran(self.dodai[-1][0],self.dodai[0][0],[xdraw,ydraw]))
        screen.blit(hinhanhquay[0],hinhanhquay[1])
        hinhanhquay = rot_center(self.hoatiethead,self.angle-90,[xdraw-25,ydraw-25])
        screen.blit(hinhanhquay[0],hinhanhquay[1])
