import math
class planet:
    def __init__(self,mass):
        self.mass=mass

    positionX=0
    positionY=0
    velocityX=0
    velocityY=0

planet1=planet(50)
planet2=planet(50)
planet3=planet(50)

planet1.positionX=4
def gAccel(x1,y1,m1,x2,y2,m2):
    r=sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

gAccel(1,1,1,1,1,1)
