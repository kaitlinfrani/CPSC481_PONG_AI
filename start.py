import pygame

from menu import Menu

WIDTH = 1200
HEIGHT = 800

pygame.init()

screen_size = (WIDTH, HEIGHT)

pongMenu = Menu(screen_size, WIDTH, HEIGHT)
pongMenu.startMenu()

# pongGame = Pong(screen_size)
# pongGame.startGame()