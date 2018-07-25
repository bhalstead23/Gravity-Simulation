from math import *
import platform
print(platform.python_version())
import pygame
from pygame import draw
G=6.67*10**-11

class planet:
    def __init__(self,posX,posY,velX,velY,mass):
        self.posX=posX
        self.posY=posY
        self.velX=velX
        self.velY=velY
        self.mass=mass

planet1=planet(220,330,0,0,10000000)
planet2=planet(500,400,0,0,10000000)
# planet3=planet(1,2,0,0,50)

crashed=False

def gForce(x1,y1,m1,x2,y2,m2):

    if (x1-x2)<0:
        coefX=-1
    else:
        coefX=1
    if (y1-y2)<0:
        coefY=-1
    else:
        coefY=1
    fX=(1-dF)*f*coefX
    fY=dF*f*coefY
    r=sqrt((x1-x2)**2 + (y1-y2)**2)
    if r<10:
        return 42
    else:
        return (G*m1*m2/r**2,fX,fY)

def physics(fX,fY,m,vX,vY,pX,pY,t):
    aX=fX/m
    aY=fY/m
    return [0.5*aX*t**2+vX*t+pX,0.5*aY*t**2+vY*t+pY,aX*t+vX,aY*t+vY]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = [1000, 700]
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

    force=gForce(planet1.posX,planet1.posY,planet1.mass,planet2.posX,planet2.posY,planet2.mass)
    if force==42:
        break

    direc1=gForceDirec(planet1.posX,planet1.posY,planet1.mass,planet2.posX,planet2.posY,planet2.mass)
    direc2=gForceDirec(planet2.posX,planet2.posY,planet2.mass,planet1.posX,planet1.posY,planet1.mass)
    planet1.posX=physics(gForce[1],,planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[0]
    planet1.posY=physics(force,direc1,planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[1]
    planet1.velX=physics(force,direc1,planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[2]
    planet1.velY=physics(force,direc1,planet1.mass,planet1.velX,planet1.velY,planet1.posX,planet1.posY,sec)[3]


    planet2.posX=physics(force,direc2,planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[0]
    planet2.posY=physics(force,direc2,planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[1]
    planet2.velX=physics(force,direc2,planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[2]
    planet2.velY=physics(force,direc2,planet2.mass,planet2.velX,planet2.velY,planet2.posX,planet2.posY,sec)[3]
    print(planet1.posX, planet1.posY, planet1.velX, planet1.velY)

    sec=sec+1


    screen.fill(WHITE)
    draw.circle(screen, GREEN, [floor(planet1.posX),floor(planet1.posY)], 10, 0)
    draw.circle(screen, RED, [floor(planet2.posX),floor(planet2.posY)], 10, 0)
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
