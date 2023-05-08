import pygame
from random import randint
BLACK = (0,0,0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, radius):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface((radius, radius))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball
        self.rect = pygame.draw.circle(self.image, color,(radius/2,radius/2), radius/2 )
        
        self.velocity = [randint(4,8),randint(-4,4)]
        
        # Fetch the rectangle object that has the dimensions of the image.
    
        # self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-4,4)