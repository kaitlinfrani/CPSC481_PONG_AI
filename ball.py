import pygame
from random import randint, randrange

# Color Values
BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    '''Represents Pong Balls'''
    
    def __init__(self, color, radius, id):
        '''Contains ball variables, constructor'''
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface((radius, radius))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # Release variables
        self.releaseTime = 0
        self.released = False
        
        # Ball ID
        self.id = 0
        
        # Out of Bounds bool
        self.outOfBounds = False
 
        # Draw the ball
        self.rect = pygame.draw.circle(self.image, color,(radius/2,radius/2), radius/2 )
        
        self.velocity = [0,0]
    
    def setReleased(self, change):
        '''Sets Released variable'''
        self.released = change    
    
    def setReleaseTime(self, change):
        '''Sets ReleaseTime variable'''
        self.releaseTime = change
        
    def setVelocity(self):
        '''Sets Velocity variable'''
        self.velocity = [randint(4,6), randint(-4,6)]
    
    def setVelocityZero(self):
        '''Sets Velocity to 0'''
        self.velocity = [0,0]
    
    def setOutOfBounds(self, change):
        '''Sets OutOfBounds variable'''
        self.outOfBounds = change

    def getReleased(self):
        '''Gets Released variable'''
        return self.released
    
    def getReleaseTime(self):
        '''Gets ReleaseTime variable'''
        return self.releaseTime
        
    def getId(self):
        '''Gets ID variable'''
        return self.id
    
    def getOutOfBounds(self):
        '''Gets OutOfBounds variable'''
        return self.outOfBounds
    
    def getVelocity(self):
        '''Gets Velocity variable'''
        return self.velocity
        
    def update(self):
        '''Updates Ball velocities'''
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def wallBounce(self, top):
        '''Allows ball to bounce off walls'''
        if top:
            self.velocity[1] = randrange(-4,-1)
        else:
            self.velocity[1] = randrange(1,4)
        
    def paddleBounce(self, playerCollide):
        '''Allows ball to bounce off paddles'''
        self.velocity[0] = -self.velocity[0]
        if playerCollide:
            self.velocity[1] = randint(1,8)
        else:
            self.velocity[1] = randint(-8,-1)