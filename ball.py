import pygame
from random import randint, randrange
BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, radius, id):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface((radius, radius))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.releaseTime = 0
        self.released = False
        self.id = 0
        self.outOfBounds = False
 
        # Draw the ball
        self.rect = pygame.draw.circle(self.image, color,(radius/2,radius/2), radius/2 )
        
        self.velocity = [0,0]
        
        # Fetch the rectangle object that has the dimensions of the image.
    
        # self.rect = self.image.get_rect()
    
    def setReleased(self, change):
        self.released = change    
    
    def setReleaseTime(self, change):
        self.releaseTime = change
        
    def setVelocity(self):
        self.velocity = [randint(4,6), randint(-4,6)]
    
    def setVelocityZero(self):
        self.velocity = [0,0]
    
    def setOutOfBounds(self, change):
        self.outOfBounds = change
    
    def getReleased(self):
        return self.released
    
    def getReleaseTime(self):
        return self.releaseTime
        
    def getId(self):
        return self.id
    
    def getOutOfBounds(self):
        return self.outOfBounds
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def wallBounce(self, top):
        if top:
            self.velocity[1] = randrange(-4,-1)
        else:
            self.velocity[1] = randrange(1,4)


        print(self.velocity)
        
    def paddleBounce(self, playerCollide):
        self.velocity[0] = -self.velocity[0]
        if playerCollide:
            self.velocity[1] = randint(1,8)
        else:
            self.velocity[1] = randint(-8,-1)