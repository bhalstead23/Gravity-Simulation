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
print(planet1.positionX)
print(planet2.positionX)
