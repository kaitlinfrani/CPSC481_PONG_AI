import pygame

from paddles import Paddle

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

screen_size = (700,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PONG")


gameOn = True

clock = pygame.time.Clock()


# Paddle initalization
playerPaddle = Paddle(WHITE, 10, 100)
playerPaddle.rect.x = 20
playerPaddle.rect.y = 200

aiPaddle = Paddle(WHITE, 10, 100)
aiPaddle.rect.x = 670
aiPaddle.rect.y = 200

paddle_sprite_list = pygame.sprite.Group()

paddle_sprite_list.add(playerPaddle)
paddle_sprite_list.add(aiPaddle)

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
            
    screen.fill(BLACK)
    
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()