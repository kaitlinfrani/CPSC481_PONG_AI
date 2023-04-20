import pygame
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

screen_size = (700,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PONG")


gameOn = True

clock = pygame.time.Clock()

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
            
    screen.fill(BLACK)
    
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()