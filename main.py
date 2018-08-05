from math import *
import platform
print(platform.python_version())
import pygame
from pygame import draw
G=6.67*10**-11


class planet:
    def __init__(self,posX,posY,posZ,velX,velY,velZ,mass):
        self.posX=posX
        self.posY=posY
        self.posZ=posZ
        self.velX=velX
        self.velY=velY
        self.velZ=velZ
        self.mass=mass

#data=open("data.txt", "r")
#print(data.readline())

planet1=planet(300,330,100,0,0,0.01,1.989*10**10)
planet2=planet(500,500,200,0,-0.15,0,5.972*10**10)
planet3=planet(100,200,50,0.05,0,0,7.34767*10**10)

def gForce(x1,y1,z1,m1,x2,y2,z2,m2):

    r=sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    #print("gForce:",x1,x2,y1,y2,z1,z2,"gives:",r)
    f=G*m1*m2/r**2
    if (x2-x1)<0:
        coefX=-1
    else:
        coefX=1
    if (y2-y1)<0:
        coefY=-1
    else:
        coefY=1
    if (z2-z1)<0:
        coefZ=-1
    else:
        coefZ=1

    fT=abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
    fX=abs(x1-x2)*f*coefX/fT
    fY=abs(y1-y2)*f*coefY/fT
    fZ=abs(z1-z2)*f*coefZ/fT

    if r<10:
        return 42
    else:
        return [G*m1*m2/r**2,fX,fY,fZ]

def physics(fX1,fY1,fZ1,fX2,fY2,fZ2,m,vX,vY,vZ,pX,pY,pZ,t):
    aX=(fX1+fX2)/m
    aY=(fY1+fY2)/m
    aZ=(fZ1+fZ2)/m
    return [0.5*aX*t**2+vX*t+pX,0.5*aY*t**2+vY*t+pY,0.5*aZ*t**2+vZ*t+pZ,aX*t+vX,aY*t+vY,aZ*t+vZ]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()

# Set the width and height of the screen [width, height]
size = [1300, 900]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("Gravity Simulation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
sec=0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    #print("Planet1:",planet1.posX,planet1.posY,planet1.posZ)
    #print("Planet2:",planet2.posX,planet2.posY,planet2.posZ)
    #print("Planet3:",planet3.posX,planet3.posY,planet3.posZ)

    _1on2 = gForce(planet1.posX,planet1.posY,planet1.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    #print("^^^_1on2")
    _1on3 = gForce(planet1.posX,planet1.posY,planet1.posZ,planet1.mass,planet3.posX,planet3.posY,planet3.posZ,planet3.mass)
    #print("^^^_1on3")
    _2on1 = gForce(planet2.posX,planet2.posY,planet2.posZ,planet2.mass,planet1.posX,planet1.posY,planet1.posZ,planet1.mass)
    #print("^^^_2on1")
    _2on3 = gForce(planet2.posX,planet2.posY,planet2.posZ,planet2.mass,planet3.posX,planet3.posY,planet3.posZ,planet3.mass)
    #print("^^^_2on3")
    _3on1 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet3.mass,planet1.posX,planet1.posY,planet1.posZ,planet1.mass)
    #print("^^^_3on1")
    _3on2 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet3.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    #print("^^^_3on2")

    if 42 in [_1on2,_1on3,_2on1,_2on3,_3on1,_3on2]:
        print("Crashed")
        break


    planet1.posX=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[0]
    planet1.posY=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[1]
    planet1.posZ=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[2]
    planet1.velX=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[3]
    planet1.velY=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[4]
    planet1.velZ=physics(_1on2[1],_1on2[2],_1on2[3],_1on3[1],_1on3[2],_1on3[3],planet1.mass,planet1.velX,planet1.velY,planet1.velZ,planet1.posX,planet1.posY,planet1.posZ,sec)[5]

    planet2.posX=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[0]
    planet2.posY=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[1]
    planet2.posZ=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[2]
    planet2.velX=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[3]
    planet2.velY=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[4]
    planet2.velZ=physics(_2on1[1],_2on1[2],_2on1[3],_2on3[1],_2on3[2],_2on3[3],planet2.mass,planet2.velX,planet2.velY,planet2.velZ,planet2.posX,planet2.posY,planet2.posZ,sec)[5]

    planet3.posX=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[0]
    planet3.posY=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[1]
    planet3.posZ=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[2]
    planet3.velX=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[3]
    planet3.velY=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[4]
    planet3.velZ=physics(_3on1[1],_3on1[2],_3on1[3],_3on2[1],_3on2[2],_3on2[3],planet3.mass,planet3.velX,planet3.velY,planet3.velZ,planet3.posX,planet3.posY,planet3.posZ,sec)[5]


    screen.fill(WHITE)
    draw.circle(screen, RED, [floor(planet1.posX),floor(planet1.posY)], 10, 0)
    draw.circle(screen, GREEN, [floor(planet2.posX),floor(planet2.posY)], 10, 0)
    draw.circle(screen, BLUE, [floor(planet3.posX),floor(planet3.posY)], 10, 0)
    # --- Drawing code should go here
    #print(sec)

    sec=sec+(1/60)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
