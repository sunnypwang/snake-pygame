import pygame
import numpy as np


class Snake:
    def __init__(self,board,x,y,TICK_SPEED):
        self.board = board
        self.body = [np.array((x-i,y), dtype=int) for i in range(3)]
        self.RIGHT = np.array((1,0))
        self.DOWN = np.array((0,1))
        self.LEFT = np.array((-1,0))
        self.UP = np.array((0,-1))
        self.direction = self.RIGHT
        self.alive = True
        self.speed = 1
        self.counter = 0
        self.counter_max = TICK_SPEED - 20
        self.TICK_SPEED = TICK_SPEED
        self.MAX_SPEED = 10
        self.grow_flag = False
        
    def get_x(self):
        return self.body[0][0]
    
    def get_y(self):
        return self.body[0][1]
    
    def get_head(self):
        return self.body[0]
    
    def get_head_pos(self,i): # i is 0 or 1
        return self.body[0][i]
                     
    def draw(self, window, grid_size):
        for piece in self.body:
            pygame.draw.rect(window, "white", (piece[0]*grid_size,piece[1]*grid_size,grid_size,grid_size))        
    
    def update_direction(self, keys):
        if keys[pygame.K_LEFT] and self.direction[0] == 0: #and self.direction == self.UP or self.direction == self.DOWN:
            self.direction = self.LEFT
        elif keys[pygame.K_RIGHT] and self.direction[0] == 0:
            self.direction = self.RIGHT
        elif keys[pygame.K_UP] and self.direction[1] == 0:
            self.direction = self.UP
        elif keys[pygame.K_DOWN] and self.direction[1] == 0:
            self.direction = self.DOWN
               
    def move(self):
        next = self.body[0] + self.direction
        if self.board.is_outside(next):
            self.alive = False
        else:
            self.body.insert(0,next)
            if self.grow_flag: # if grow flag is triggered do not move tail
                self.grow_flag = False
            else:
                self.body.pop()
    
    def update(self):
        self.counter = (self.counter + 1) % (self.TICK_SPEED - 20 - self.speed)
        if self.counter > 0: 
            return
        
        self.move()
        
    def increase_speed(self):
        if self.counter_max <= 1:
            return
        self.counter_max -= 1
        
    def set_speed(self, spd):
        self.speed = min(self.MAX_SPEED,spd)
        
    def grow(self):
        print('grow')
        self.grow_flag = True
        