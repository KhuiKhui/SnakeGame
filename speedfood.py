import pygame
import random
from filedef import *


class speedfood:
    x = 0
    y = 0
    xtuongdoi = 0
    ytuongdoi = 0
    time = 0
    def __init__(self):
        self.x = random.randint(-4000,4000)
        self.y = random.randint(-4000,4000)
    def draw(self,screen,xdraw,ydraw,width,height,obj):
        self.xtuongdoi = xdraw+(self.x-obj.dodai[0][0][0])
        self.ytuongdoi = ydraw+(self.y-obj.dodai[0][0][1])
        if self.xtuongdoi<=width and self.xtuongdoi>=0 and self.ytuongdoi<=height and self.ytuongdoi>=0:             
            pygame.draw.circle(screen, (255,255,0), [self.xtuongdoi,self.ytuongdoi], 8)
    def hoatdong(self,xdraw,ydraw,obj):
        
        if (distance([xdraw,ydraw],[self.xtuongdoi,self.ytuongdoi])<=10):
            obj.speedup = 200
            obj.speed = 25
            return True
        return False
