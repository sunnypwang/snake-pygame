from sys import exit
import numpy as np
import pygame
from board import Board
from snake import Snake
from status import Status

GRID_ROWS = 30
GRID_COLS = 30
GRID_SIZE = 30

STATUS_BAR_HEIGHT = 50

GAME_WIDTH = GRID_COLS * GRID_SIZE 
GAME_HEIGHT = GRID_ROWS * GRID_SIZE

TICK_SPEED = 30

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT + STATUS_BAR_HEIGHT))
clock = pygame.time.Clock()

board = Board(GRID_ROWS,GRID_COLS,GRID_SIZE,TICK_SPEED, 0, STATUS_BAR_HEIGHT)
status = Status(board, 0, 0, GAME_WIDTH, STATUS_BAR_HEIGHT)

running = True
while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if not board.is_player_alive():
        print('game over')
        pass
    else:
        window.fill((0,0,0))
        
        keys = pygame.key.get_pressed()
        board.update_board(keys)
        board.draw(window)
        status.draw(window)
    pygame.display.flip()
    clock.tick(TICK_SPEED)