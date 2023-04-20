import pygame

from paddles import Paddle
from ball import Ball

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

screen_size = (700,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PONG")


# Ball initlaization
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# Paddle initalization
playerPaddle = Paddle(WHITE, 10, 100)
playerPaddle.rect.x = 20
playerPaddle.rect.y = 200

aiPaddle = Paddle(WHITE, 10, 100)
aiPaddle.rect.x = 670
aiPaddle.rect.y = 200

sprite_list = pygame.sprite.Group()

sprite_list.add(playerPaddle)
sprite_list.add(aiPaddle)
sprite_list.add(ball)

gameOn = True

clock = pygame.time.Clock()


while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                carryOn=False
 
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPaddle.moveUp(5)
    if keys[pygame.K_s]:
        playerPaddle.moveDown(5)
    
    if keys[pygame.K_UP]:
        aiPaddle.moveUp(5)
    if keys[pygame.K_DOWN]:
        aiPaddle.moveDown(5)    
 
    # --- Game logic should go here
    sprite_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
    
    screen.fill(BLACK)
    
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    sprite_list.draw(screen)
    
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()