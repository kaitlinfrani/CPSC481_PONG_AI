import pygame
import pygame_menu

from pong import Pong

class Menu:
    def __init__(self, screen_size, screen_width, screen_height):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def startMenu(self):
        menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)

        # menu.add.text_input('Name :', default='John Doe')
        # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
        menu.add.button('Play', self.startGame)
        menu.add.button('Quit', pygame_menu.events.EXIT)
            
        menu.mainloop(self.screen)


    
    def set_difficulty(value, difficulty):
        # Do the job here !
        pass
    
    def start_game(self):
        pong = Pong(self.screen_size, self.screen_width, self.screen_height)
        pong.startGame()

