import pygame

from paddles import Paddle
from ball import Ball
from time import sleep
from random import randrange

BLACK = (0,0,0)
WHITE = (255,255,255)

class Pong():
    def __init__(self, screen_size, twoPlayer=True):
        self.screen = pygame.display.set_mode(screen_size)
        
        # Ball Variables
        self.ballList = []
        self.numBalls = 1
        
        # Paddle Variables
        self.playerPaddle = Paddle(WHITE, 0, 0)
        self.aiPaddle = Paddle(WHITE, 0, 0)
        
        # Sprite list containing Balls, Paddle, and other sprites
        self.sprite_list = pygame.sprite.Group()
        
        # Game Variables 
        self.twoPlayer = twoPlayer
        self.gameOn = True
        self.nextLevel = False
        self.clock = pygame.time.Clock()
        self.playerScore = 0
        self.aiScore = 0
        self.level = 1
        
        self.initializeGame()
        

    def createPaddles(self, player_color=WHITE, ai_color=WHITE, x_size=10, y_size=100):
        ''' Creates the player and ai paddles'''
        self.playerPaddle = Paddle(player_color, x_size, y_size)
        self.playerPaddle.rect.x = 20
        self.playerPaddle.rect.y = 200

        self.aiPaddle = Paddle(ai_color, x_size, y_size)
        self.aiPaddle.rect.x = 670
        self.aiPaddle.rect.y = 200
        
    def addBall(self, position, ball_color=WHITE, x_size=10, y_size=10):
        ball = Ball(ball_color, x_size, y_size)
        ball.rect.x = position[0]
        ball.rect.y = position[1]
        self.ballList.append(ball)
        
    def initializeGame(self):
        self.setDisplays()
                
        self.createPaddles()
        self.addBall(position=[345, 195])
        
        self.sprite_list.add(self.playerPaddle)
        self.sprite_list.add(self.aiPaddle)
        
        for _ in self.ballList:
            self.sprite_list.add(_)
        
    def setDisplays(self):
        pygame.display.set_caption("PONG")
        
    def aiPlayer(self):
        closest = self.ballList[0]
        for ball in self.ballList:
            if self.aiPaddle.rect.y - ball.rect.y <= 0:
                 closest = ball
        self.aiPaddle.rect.y = closest.rect.y
        
    def resetGameState(self):
        self.playerPaddle.rect.x = 20
        self.playerPaddle.rect.y = 200
        
        self.aiPaddle.rect.x = 670
        self.aiPaddle.rect.y = 200
        
        for ball in self.ballList:
            ball.rect.x = 345
            ball.rect.y = randrange(155, 235)
            
        for _ in self.ballList:
            self.sprite_list.add(_)
        

    def startGame(self):  
        nextLevel=False
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    self.gameOn = False # Flag that we are done so we exit this loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        self.gameOn=False
            if nextLevel:
                self.resetGameState()
                self.addBall(position=[345, randrange(155, 235)])
                print(self.ballList)
                # ADD NEXT LEVEL TXT
                self.level+=1
                nextLevel = False
                        
            #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.playerPaddle.moveUp(5)
            if keys[pygame.K_s]:
                self.playerPaddle.moveDown(5)
            
            if self.twoPlayer:
                if keys[pygame.K_UP]:
                    self.aiPaddle.moveUp(5)
                if keys[pygame.K_DOWN]:
                    self.aiPaddle.moveDown(5) 
            else:
                self.aiPlayer()   
        
            # --- Game logic should go here
            self.sprite_list.update()
            
            for ball in self.ballList:
            #Check if the ball is bouncing against any of the 4 walls:
                if ball.rect.x>=690:
                    self.playerScore+=1
                    nextLevel = True
                    # ball.rect.x=690 
                    # ball.bounce()
                if ball.rect.x<=0:
                    # ball.rect.x=0
                    self.aiScore+=1
                    # ball.bounce()
                if ball.rect.y>490:
                    ball.rect.y=490 
                    ball.bounce()
                if ball.rect.y<0:
                    ball.rect.y=0 
                    ball.bounce()       
                if pygame.sprite.collide_mask(ball, self.playerPaddle) or pygame.sprite.collide_mask(ball, self.aiPaddle):
                    ball.bounce()

                self.screen.fill(BLACK)
                
                pygame.draw.line(self.screen, WHITE, [349, 0], [349, 500], 5)
            
                self.sprite_list.draw(self.screen)
            
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.playerScore), 1, WHITE)
            self.screen.blit(text, (250,10))
            text = font.render(str(self.aiScore), 1, WHITE)
            self.screen.blit(text, (420,10))
            
            pygame.display.flip()
            
            self.clock.tick(60)
            
        
        pygame.quit()
