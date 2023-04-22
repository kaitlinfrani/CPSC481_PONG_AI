import pygame

from pong import Pong

pygame.init()

screen_size = (700,500)

pongGame = Pong(screen_size)
pongGame.startGame()