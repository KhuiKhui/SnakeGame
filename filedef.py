import math
import pygame
pygame.init()
def chuyendoitoadoconran(toadotgvatcandoi,toadotgmoccandoi,toadotuongdoimoccandoi):
    kqx = toadotuongdoimoccandoi[0] + (toadotgvatcandoi[0] - toadotgmoccandoi[0])
    kqy = toadotuongdoimoccandoi[1] + (toadotgvatcandoi[1] - toadotgmoccandoi[1])
    return [kqx-25, kqy-25]
def distance(toadotuongdoivatcando,toadotuongdoimoccando):
    return math.sqrt((toadotuongdoivatcando[0]-toadotuongdoimoccando[0])**2+(toadotuongdoivatcando[1]-toadotuongdoimoccando[1])**2)
def rot_center(image, angle, toado):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (toado[0], toado[1])).center)
    return rotated_image, new_rect
