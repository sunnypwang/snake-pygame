from sys import exit
import numpy as np
import pygame
from board import Board
from snake import Snake

pygame.init()

GRID_ROWS = 20
GRID_COLS = 20
GRID_SIZE = 50

GAME_WIDTH = GRID_COLS * GRID_SIZE 
GAME_HEIGHT = GRID_ROWS * GRID_SIZE


window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))

board = Board(GRID_ROWS,GRID_COLS,GRID_SIZE)

running = True
while running:
    pygame.time.delay(100)
    window.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    if not board.update_board(keys):
        print('game over')
        break
    board.draw(window)
    pygame.display.update()