from math import *

G=6.67*10**-11

class planet:
    def __init__(self,posX,posY,velX,velY,mass):
        self.posX=posX
        self.posY=posY
        self.velX=velX
        self.velY=velY
        self.mass=mass

planet1=planet(1,1,0,0,50)
planet2=planet(1,3,0,0,50)
planet3=planet(1,2,0,0,50)

planet1.positionX=4
def gAccel(x1,y1,m1,x2,y2,m2):
    r=sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    return G*m1*m2/r**2

gAccel(planet1.posX,planet1.posY,planet1.mass,planet2.posX,planet2.posY,planet2.mass)
