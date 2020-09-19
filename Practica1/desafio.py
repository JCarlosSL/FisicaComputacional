import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

class Rectangle:
    def __init__(self,x,y,w,h):
        self.x = x    #0
        self.y = y    #0
        self.w = w    #20
        self.h = h    #10
    def contains(self,point):
        return (self.x <point.x < self.w and
                self.y < point.y < self.h)

    def reflexion(self,point,point_v):
        """reflexion especular"""
        if self.x > point.x or point.x > self.w:
            point_v.setX(-point_v.x)
        if self.y > point.y or point.y > self.h:
            point_v.setY(-point_v.y)

                
h = 0.1
velocidad = Point(10,40)
particula = Point()
rec = Rectangle(0,0,200,100)

old_point = Point()
i=0

images = []
color_1 = (0,0,0)
color_2 = (255,255,255)

while(i<10000):
    
    im = Image.new('RGB',(200,100),color_1)
    draw = ImageDraw.Draw(im)
    draw.point((old_point.x,old_point.y),fill=color_1)
    draw.point((particula.x,particula.y),fill=color_2)
    images.append(im)

    old_point.x = particula.x
    old_point.y = particula.y
    particula.setX(particula.x + velocidad.x*h)
    particula.setY(particula.y + velocidad.y*h)
    if(rec.contains(particula)!=True):
        rec.reflexion(particula,velocidad) 
    i+=1

images[0].save('desafio.gif',save_all=True, append_images=images[1:],
        optimize=False,duration=40,loop=0)



