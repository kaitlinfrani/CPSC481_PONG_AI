import pygame

from paddles import Paddle
from ball import Ball
from random import randrange

BLACK = (0,0,0)
WHITE = (255,255,255)

class Pong():
    def __init__(self, screen_size, screen_width, screen_height, twoPlayer=False):
        self.screen = pygame.display.set_mode(screen_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Ball Variables
        self.ballList = []
        self.numBalls = 1
        
        # Paddle Variables
        self.playerPaddle = Paddle(WHITE, 0, 0, self.screen_height)
        self.aiPaddle = Paddle(WHITE, 0, 0, self.screen_height)
        
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
        self.playerPaddle = Paddle(player_color, x_size, y_size, self.screen_height)
        self.playerPaddle.rect.x = self.screen_width - 1160
        self.playerPaddle.rect.y = self.screen_height / 2

        self.aiPaddle = Paddle(ai_color, x_size, y_size, self.screen_height)
        self.aiPaddle.rect.x = self.screen_width - 40
        self.aiPaddle.rect.y = self.screen_height / 2
        
    def addBall(self, position, ball_color=WHITE, radius = 10):    
        ball = Ball(ball_color, radius, self.level-1)
        ball.rect.x = position[0]
        ball.rect.y = position[1]
        ball.setReleaseTime(pygame.time.get_ticks() + (600 * (self.level - 1)))
        self.ballList.append(ball)
        
    def initializeGame(self):
        self.setDisplays()
                
        self.createPaddles()
        self.addBall(position=[self.screen_width / 2, self.screen_height / 2])
        
        self.sprite_list.add(self.playerPaddle)
        self.sprite_list.add(self.aiPaddle)
        
        for _ in self.ballList:
            self.sprite_list.add(_)
        
    def setDisplays(self):
        pygame.display.set_caption("PONG")
    
    def drawScreen(self):
        self.screen.fill(BLACK)
        
        pygame.draw.line(self.screen, WHITE, [self.screen_width / 2, 0], [self.screen_width / 2, self.screen_height], 5)
            
        self.sprite_list.draw(self.screen)
        
        font = pygame.font.Font(None, 74)
        text = font.render(str(self.playerScore), 1, WHITE)
        self.screen.blit(text, (self.screen_width / 4, 10))
        text = font.render(str(self.aiScore), 1, WHITE)
        self.screen.blit(text, (self.screen_width - (self.screen_width / 4),10))
        
        pygame.display.flip()
        
    def aiPlayer(self):
        follow = randrange(0,2)
        
        if 0 <= self.aiPaddle.rect.y <= self.screen_height - self.aiPaddle.height:
            if follow == 0:
                closest = self.ballList[0]
                for ball in self.ballList:
                    if ball.getOutOfBounds() is False:
                        print("ball", ball, ball.getId(), ball.rect.x, ball.getOutOfBounds())
                        if closest.getOutOfBounds() is True:
                            closest = ball
                        if self.aiPaddle.rect.x - ball.rect.x <= self.aiPaddle.rect.x - closest.rect.x:
                            closest = ball
                    print("closest",closest, closest.getId(), closest.rect.x, closest.getOutOfBounds())
                if self.aiPaddle.rect.y < closest.rect.y:
                    self.aiPaddle.rect.y += 5 + self.level
                elif self.aiPaddle.rect.y > closest.rect.y:
                    self.aiPaddle.rect.y -= 5 + self.level
        elif self.aiPaddle.rect.y < 0 :
            self.aiPaddle.rect.y = 0
        elif self.aiPaddle.rect.y > self.screen_height - self.aiPaddle.height:
            self.aiPaddle.rect.y = self.screen_height - self.aiPaddle.height
        
    def resetGameState(self, scoreTime, nextLevel):
        self.playerPaddle.rect.x = self.screen_width - 1160
        self.playerPaddle.rect.y = self.screen_height / 2
        
        self.aiPaddle.rect.x = self.screen_width - 40
        self.aiPaddle.rect.y = self.screen_height / 2
        
        if nextLevel:
            self.level+=1
            if self.ballList.count(Ball) < 3:
                self.addBall(position=[self.screen_width / 2, 550])            
        
        for idx, ball in enumerate(self.ballList):
            ball.rect.x = self.screen_width / 2
            ball.rect.y = randrange(300, 600)
            ball.setReleaseTime(pygame.time.get_ticks() + (3000 * idx))
            ball.setReleased(False)
            ball.setOutOfBounds(False)
            
        self.sprite_list.add(self.ballList[-1])

        self.countdown(scoreTime)
        
        
    def countdown(self, scoreTime):
        while True:
            currentTime = pygame.time.get_ticks()
            font = pygame.font.Font("freesansbold.ttf", 60)
            
            if currentTime - scoreTime < 700:
                text = font.render("3", True, WHITE)
            
            if 700 < currentTime - scoreTime < 1400:
                text = font.render("2", True, WHITE)
                
            if 1400 < currentTime - scoreTime < 2100:
                text = font.render("1", True, WHITE)

            if currentTime - scoreTime > 2100:
                break
            
            self.screen.fill(BLACK)
            self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
            
            pygame.draw.line(self.screen, WHITE, [self.screen_width / 2, 0], [self.screen_width / 2, self.screen_height], 5)
            
            self.sprite_list.draw(self.screen)
              
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.playerScore), 1, WHITE)
            self.screen.blit(text, (self.screen_width / 4, 10))
            text = font.render(str(self.aiScore), 1, WHITE)
            self.screen.blit(text, (self.screen_width - (self.screen_width / 4),10))

            pygame.display.flip()

    def checkOutOfBounds(self, ball):
        if 0 >= ball.rect.x or ball.rect.x >= self.screen_width:
            return True
        return False
    
    def checkNumPlayBalls(self):
        ballCount = 0
        for _ in self.sprite_list:
            if isinstance(_, Ball) and not self.checkOutOfBounds(_):
                ballCount += 1
        return ballCount
    
    def checkScores(self):
        if self.playerScore > self.aiScore:
            self.resetGameState(pygame.time.get_ticks(), nextLevel=True)
        else:
            self.resetGameState(pygame.time.get_ticks(), nextLevel=False)
     
    def restartPrompt(self):
        pass    
    
    
    def startGame(self):
        self.countdown(pygame.time.get_ticks())
        
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    self.gameOn = False # Flag that we are done so we exit this loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        self.gameOn=False

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
                if pygame.time.get_ticks() >= ball.getReleaseTime() and ball.getReleased() is False:
                    ball.setVelocity()
                    ball.setReleased(True)
            
            for ball in self.ballList:
                
            #Check if the ball is bouncing against any of the 4 walls:
                if ball.rect.x>=self.screen_width and ball.getOutOfBounds() is False:
                    ball.setVelocityZero()
                    ball.setOutOfBounds(True)
                    self.playerScore+=1

                if ball.rect.x<=0 and ball.getOutOfBounds() is False:
                    ball.setVelocityZero()
                    ball.setOutOfBounds(True)
                    self.aiScore+=1
                                             
                if ball.rect.y>=self.screen_height:
                    ball.rect.y = self.screen_height
                    ball.wallBounce(True)
                if ball.rect.y<=0:
                    ball.rect.y = 0
                    ball.wallBounce(False)
                
                playerCollide = pygame.sprite.collide_mask(ball, self.playerPaddle) 
                aiCollide = pygame.sprite.collide_mask(ball, self.aiPaddle)
                if playerCollide or aiCollide:
                    ball.paddleBounce(playerCollide)
                    
            if self.checkNumPlayBalls() <= 0:
                self.checkScores()   

            if self.playerScore >= 6:
                font = pygame.font.Font("freesansbold.ttf", 60)
                text = font.render("Player Wins!", True, WHITE)
                self.screen.fill(BLACK)
                self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
                    
                self.gameOn = False
            elif self.aiScore >= 6:
                font = pygame.font.Font("freesansbold.ttf", 60)
                text = font.render("AI Wins!", True, WHITE)
                self.screen.fill(BLACK)
                self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
                
                self.gameOn = False
            self.drawScreen()
            
            self.clock.tick(60)
            
        pygame.quit()
