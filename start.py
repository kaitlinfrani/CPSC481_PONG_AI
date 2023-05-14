import pygame

from menu import Menu

# Dimension Values
WIDTH = 1200
HEIGHT = 800

pygame.init()

screen_size = (WIDTH, HEIGHT)

# Intializes and starts menu
pongMenu = Menu(screen_size, WIDTH, HEIGHT)
pongMenu.startMenu()
