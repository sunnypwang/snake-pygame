import numpy as np
from apple import AppleControl
from snake import Snake
import pygame 

class Board:
    def __init__(self,rows,cols,size,TICK_SPEED, x, y):
        self.board = np.zeros((rows,cols), dtype=int)
        self.grid_size = size
        self.player_pos = None
        self.player = Snake(self, rows/2, cols/2, TICK_SPEED)
        self.apple_control = AppleControl(self.board)
        self.score = 0
        self.TICK_SPEED = TICK_SPEED
        self.x = x
        self.y = y
        
    def nrows(self):
        return self.board.shape[0]
        
    def ncols(self):
        return self.board.shape[1]
    
    def get_value(self,x,y):
        return self.board[x,y]
    
    def get_player_pos(self):
        return self.player_pos
    
    def set_player_pos(self,x,y):
        if self.player():
            self.board[self.player.get_pos()] = 0
        self.player_pos = (x,y)
        self.board[x,y] = 1
        
    def draw(self, window):
        self.player.draw(window, self.grid_size, self.x, self.y)
        self.apple_control.draw(window, self.grid_size, self.x, self.y)
        
    def is_player_alive(self):
        return self.player.alive
    
    def update_board(self,keys):
        self.board.fill(0)
        
        apple_pos = self.apple_control.locate_apple()
        if not apple_pos:
            free = self.get_available_grid()
            apple_pos = self.apple_control.spawn_apple(free)
        self.board[apple_pos] = 2
        
        self.player.update_direction(keys)
        self.player.update()
        self.check_eat()
        
        for piece in self.player.body:
            # print(piece)
            self.board[tuple(piece)] = 1
        # print(self.board)
        # print(self.score, self.player.speed)
        print(self.player.body)
        
        self.set_speed_by_score()
    
    def is_outside(self,pos):
        (x,y) = pos
        return x < 0 or x >= self.nrows() or y < 0 or y >= self.ncols()
    
    def get_available_grid(self):
        free = []
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i,j] == 0:
                    free.append((i,j))
        return free
        
    def check_eat(self):
        if tuple(self.player.body[0]) == tuple(self.apple_control.pos):
            self.apple_control.destroy_apple()
            self.score += 1
            self.player.grow()
            
    def set_speed_by_score(self):
        spd = self.score // 5 + 1
        self.player.set_speed(spd)