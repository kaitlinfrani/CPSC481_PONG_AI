import pygame

from paddles import Paddle
from ball import Ball
from random import randrange

# Color Values
BLACK = (0,0,0)
WHITE = (255,255,255)

class Pong():
    '''Pong class, holding game rules and system'''
    def __init__(self, screen_size, screen_width, screen_height, twoPlayer=False):
        '''Contains Pong Variables and elements'''
        # Screen Variables
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
        '''Adds a ball to the field''' 
        ball = Ball(ball_color, radius, self.level-1)
        ball.rect.x = position[0]
        ball.rect.y = position[1]
        ball.setReleaseTime(pygame.time.get_ticks() + (600 * (self.level - 1)))
        self.ballList.append(ball)
        
    def initializeGame(self):
        '''Initializes the game's starting state'''
        self.setDisplays()
                
        self.createPaddles()
        self.addBall(position=[self.screen_width / 2, self.screen_height / 2])
        
        self.sprite_list.add(self.playerPaddle)
        self.sprite_list.add(self.aiPaddle)
        
        for _ in self.ballList:
            self.sprite_list.add(_)
        
    def setDisplays(self):
        '''Sets the pygame window display name'''
        pygame.display.set_caption("PONG")
    
    def drawScreen(self):
        '''Draws the field screen'''
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
        '''AI Algorithm'''
        # Variable indicating whether the AI moves or not
        follow = randrange(0,2)
        
        # Ensures that the AI Paddle is within the screen boundaries
        if 0 <= self.aiPaddle.rect.y <= self.screen_height - self.aiPaddle.height:
            if follow == 0:
                closest = self.ballList[0]
                
                # Finds the closest ball to the AI Paddle
                for ball in self.ballList:
                    if ball.getOutOfBounds() is False:  # do not check balls that are out of bounds
                        if closest.getOutOfBounds() is True:
                            closest = ball
                        if self.aiPaddle.rect.x - ball.rect.x <= self.aiPaddle.rect.x - closest.rect.x:
                            closest = ball
                
                # Move AI Paddle according to the y-axis distance from the closest ball            
                if self.aiPaddle.rect.y < closest.rect.y:
                    self.aiPaddle.rect.y += 5 + self.level
                elif self.aiPaddle.rect.y > closest.rect.y:
                    self.aiPaddle.rect.y -= 5 + self.level
                    
        elif self.aiPaddle.rect.y < 0 :
            self.aiPaddle.rect.y = 0
        elif self.aiPaddle.rect.y > self.screen_height - self.aiPaddle.height:
            self.aiPaddle.rect.y = self.screen_height - self.aiPaddle.height
        
    def resetGameState(self, scoreTime, nextLevel):
        '''Resets Game State'''
        self.playerPaddle.rect.x = self.screen_width - 1160
        self.playerPaddle.rect.y = self.screen_height / 2
        
        self.aiPaddle.rect.x = self.screen_width - 40
        self.aiPaddle.rect.y = self.screen_height / 2
        
        # If the it is the next level, add a ball to the field
        if nextLevel:
            self.level+=1
            if self.ballList.count(Ball) < 3:
                self.addBall(position=[self.screen_width / 2, 550])            
        
        # Set release times and starting positions of each ball
        for idx, ball in enumerate(self.ballList):
            ball.rect.x = self.screen_width / 2
            ball.rect.y = randrange(300, 600)
            ball.setReleaseTime(pygame.time.get_ticks() + (3000 * idx))
            ball.setReleased(False)
            ball.setOutOfBounds(False)
            
        # Add ball to sprite list
        self.sprite_list.add(self.ballList[-1])

        self.countdown(scoreTime)
        
        
    def countdown(self, scoreTime):
        '''Begins countdown'''
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
            
            # Draw numbers and display
            
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
        '''Check is a ball is out of bounds'''
        if 0 >= ball.rect.x or ball.rect.x >= self.screen_width:
            return True
        return False
    
    def checkNumPlayBalls(self):
        '''Check the if there are still balls on the field'''
        ballCount = 0
        for _ in self.sprite_list:
            if isinstance(_, Ball) and not self.checkOutOfBounds(_):
                ballCount += 1
        return ballCount
    
    def checkScores(self):
        '''Check Player and AI scores'''
        if self.playerScore > self.aiScore:
            self.resetGameState(pygame.time.get_ticks(), nextLevel=True)
        else:
            self.resetGameState(pygame.time.get_ticks(), nextLevel=False)
    
    def startGame(self):
        '''Runs game loop'''
        
        self.countdown(pygame.time.get_ticks())
        
        while self.gameOn:
            keys = pygame.key.get_pressed()
            
            # If "quit" or the "x" key is pressed, exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    self.gameOn = False # Flag that we are done so we exit this loop
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        self.gameOn=False

            # Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player 2) 
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

            # Updates sprite_list
            self.sprite_list.update()
        
            # Releases balls from their start position according to their ReleaseTime
            for ball in self.ballList:      
                if pygame.time.get_ticks() >= ball.getReleaseTime() and ball.getReleased() is False:
                    ball.setVelocity()
                    ball.setReleased(True)
            
            # Checks for ball bounces
            for ball in self.ballList:
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
                
                # Checks if the balls collides with paddles
                playerCollide = pygame.sprite.collide_mask(ball, self.playerPaddle) 
                aiCollide = pygame.sprite.collide_mask(ball, self.aiPaddle)
                if playerCollide or aiCollide:
                    ball.paddleBounce(playerCollide)
                    
            # Checks balls on field           
            if self.checkNumPlayBalls() <= 0:
                self.checkScores()   
            
            # Checks if the Player or AI have won, show end screens
            if self.playerScore >= 6 and self.aiScore != self.playerScore:
                print("player win")
                while self.gameOn:
                    print("picking")
                    font = pygame.font.Font("freesansbold.ttf", 30)
                    text = font.render("Player Wins!", True, WHITE)
                    self.screen.fill(BLACK)
                    self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                            self.gameOn = False # Flag that we are done so we exit this loop
                        elif event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                                self.gameOn=False
                                
                    self.clock.tick(60)
            elif self.aiScore >= 6 and self.aiScore != self.playerScore:
                print("ai win")

                while self.gameOn:
                    print("picking")

                    font = pygame.font.Font("freesansbold.ttf", 30)
                    text = font.render("AI Wins!", True, WHITE)
                    self.screen.fill(BLACK)
                    self.screen.blit(text, (self.screen_width / 2, self.screen_height / 2))
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                            self.gameOn = False # Flag that we are done so we exit this loop
                        elif event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                                self.gameOn=False
            
                    self.clock.tick(60)
        
            self.drawScreen()
            
            self.clock.tick(60)
            
        pygame.quit()
