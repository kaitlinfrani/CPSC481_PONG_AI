import pygame
import pygame_menu

from pong import Pong

class Menu:
    '''Represents the Menu'''
    def __init__(self, screen_size, screen_width, screen_height):
        '''Holds menu variables and elements'''
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        
    def startMenu(self):
        '''Displays and controls Menu'''
        # Sets menu options
        menu = pygame_menu.Menu('PONG', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)
        menu.add.button('Play', self.start_game)
        menu.add.button('Quit', pygame_menu.events.EXIT)
            
        menu.mainloop(self.screen)
    
    def start_game(self):
        '''Starts Game'''
        pong = Pong(self.screen_size, self.screen_width, self.screen_height)
        pong.startGame()

