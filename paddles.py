import pygame

# Color Values
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    '''Represents Paddle Class'''
        
    def __init__(self, color, width, height, screen_height):
        '''Contains paddle elements'''
        super().__init__()
        
        # Screen Variables
        self.screen_height = screen_height
        
        # Paddle Dimensions
        self.width = width
        self.height = height
        
        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
    
        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object
        self.rect = self.image.get_rect()
    
    def moveUp(self, pixels):
        '''Moves paddles up'''
        self.rect.y -= pixels
		#Check that you are not going off the screen
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        '''Moves paddle down'''
        self.rect.y += pixels
	    #Check that you are not going off the screen
        if self.rect.y > self.screen_height - self.height:
          self.rect.y = self.screen_height - self.height