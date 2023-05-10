import pygame

from menu import Menu

pygame.init()

screen_size = (700,500)

pongMenu = Menu(screen_size)
pongMenu.startMenu()

# pongGame = Pong(screen_size)
# pongGame.startGame()