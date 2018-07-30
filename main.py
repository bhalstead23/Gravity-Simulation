from math import *
import platform
print(platform.python_version())
import pygame
from pygame import draw
G=6.67*10**-11

class planet:
<<<<<<< HEAD
    def __init__(self,posX,posY,posZ,velX,velY,velZ,mass):
=======
    def __init__(self,posX,posY,posZ,velX,velY,mass):
>>>>>>> 374891b25d94a1c517c44d2a35cd180d3b175806
        self.posX=posX
        self.posY=posY
        self.posZ=posZ
        self.velX=velX
        self.velY=velY
        self.velZ=velZ
        self.mass=mass

<<<<<<< HEAD
planet1=planet(220,330,100,0,0,0,1000000000)
planet2=planet(500,400,200,0,0,0,100000000000)
planet3=planet(100,200,50,0,0,0,100000000)
=======
planet1=planet(220,330,0,0,1000000000)
planet2=planet(500,400,0,0,100000000000)
planet3=planet(100,200,0,0,100000000)
>>>>>>> 374891b25d94a1c517c44d2a35cd180d3b175806

crashed=False

def gForce(x1,y1,z1,m1,x2,y2,z2,m2):



    r=sqrt((x1-x2)**2 + (y1-y2)**2)
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
    fX=(x1-x2)*f*coefX/fT
    fY=(y1-y2)*f*coefX/fT
    fZ=(z1-z2)*f*coefX/fT

    if r<10:
        return 42
    else:
        return [G*m1*m2/r**2,fX,fY,fZ]

def physics(fX,fY,fZ,m,vX,vY,vZ,pX,pY,pZ,t):
    aX=fX/m
    aY=fY/m
    aZ=fZ/m
    return [0.5*aX*t**2+vX*t+pX,0.5*aY*t**2+vY*t+pY,0.5*aZ*t**2+vZ*t+pZ,aX*t+vX,aY*t+vY,aZ*t+vZ]


#def physics(fX,fY,m,vX,vY,pX,pY,t):
#    aX=fX/m
#    aY=fY/m
#    return [0.5*aX*t**2+vX*t+pX,0.5*aY*t**2+vY*t+pY,aX*t+vX,aY*t+vY]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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



    _1on2 = gForce(planet1.posX,planet1.posY,planet1.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
<<<<<<< HEAD
    _1on3 = gForce(planet1.posX,planet1.posY,planet1.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    _2on1 = gForce(planet2.posX,planet2.posY,planet1.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    _2on3 = gForce(planet2.posX,planet2.posY,planet2.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    _3on1 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
    _3on2 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet1.mass,planet2.posX,planet2.posY,planet2.posZ,planet2.mass)
=======
    _1on3 = gForce(planet1.posX,planet1.posY,planet1.posZ,planet1.mass,planet3.posX,planet3.posY,planet3.posZ,planet3.mass)
    _2on1 = gForce(planet2.posX,planet2.posY,planet2.posZ,planet2.mass,planet1.posX,planet1.posY,planet1.posZ,planet1.mass)
    _2on3 = gForce(planet2.posX,planet2.posY,planet2.posZ,planet2.mass,planet3.posX,planet3.posY,planet3.posZ,planet3.mass)
    _3on1 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet3.mass,planet1.posX,planet1.posY,planet1.posZ,planet1.mass)
    _3on2 = gForce(planet3.posX,planet3.posY,planet3.posZ,planet3.mass,planet2.posX,planet2.posY,planet3.posZ,planet2.mass)
>>>>>>> 374891b25d94a1c517c44d2a35cd180d3b175806

    planet1.posX = physics(_1on2[1],_1on2[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[0]
    planet1.posY = physics(_1on2[1],_1on2[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[1]
    planet1.velX = physics(_1on2[1],_1on2[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[2]
    planet1.velY = physics(_1on2[1],_1on2[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[3]

    planet1.posX = physics(_1on3[1],_1on3[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[0]
    planet1.posY = physics(_1on3[1],_1on3[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[1]
    planet1.velX = physics(_1on3[1],_1on3[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[2]
    planet1.velY = physics(_1on3[1],_1on3[2],planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[3]

    planet2.posX=physics(_2on1[1],_2on1[2],planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[0]
    planet2.posY=physics(_2on1[1],_2on1[2],planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[1]
    planet2.velX=physics(_2on1[1],_2on1[2],planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[2]
    planet2.velY=physics(_2on1[1],_2on1[2],planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[3]
    print(planet1.posX)
    print(planet1.posY)
    print(planet2.posX)
    print(planet2.posY)
    sec=sec+1


    screen.fill(WHITE)
    draw.circle(screen, GREEN, [floor(planet1.posX),floor(planet1.posY)], 10, 0)
    draw.circle(screen, RED, [floor(planet2.posX),floor(planet2.posY)], 10, 0)
    draw.circle(screen, RED, [floor(planet3.posX),floor(planet3.posY)], 10, 0)
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
