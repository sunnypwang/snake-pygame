import pygame
import numpy as np


class Snake:
    def __init__(self,board,x,y):
        self.board = board
        self.body = [np.array((x-i,y), dtype=int) for i in range(3)]
        self.RIGHT = np.array((1,0))
        self.DOWN = np.array((0,1))
        self.LEFT = np.array((-1,0))
        self.UP = np.array((0,-1))
        self.direction = self.RIGHT
        self.alive = True
        
    def get_x(self):
        return self.body[0][0]
    
    def get_y(self):
        return self.body[0][1]
    
    def get_head(self):
        return self.body[0]
    
    def get_head_pos(self,i): # i is 0 or 1
        return self.body[0][i]
    
    # def moveX(self, i):
    #     self.body.insert(0,(self.get_head_pos(0)+i,self.get_head_pos(1)))
    #     self.body.pop()
        
    # def moveY(self, i):
    #     self.body.insert(0,(self.get_head_pos(0),self.get_head_pos(1) + i))
    #     self.body.pop()
        
    # def move_tails(self):
    #     self.tails.insert(0,(self.head_x,self.head_y))
    #     self.tails.pop()
                     
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
        # if self.direction == self.RIGHT:
        #     self.moveX(1)
        # elif self.direction == self.DOWN:
        #     self.moveY(1)
        # elif self.direction == self.LEFT:
        #     self.moveX(-1)         
        # elif self.direction == self.UP:
        #     self.moveY(-1)
        next = self.body[0] + self.direction
        if self.board.is_outside(next):
            self.alive = False
        else:
            self.body.insert(0,next)
            self.body.pop()
            
    # def set_direction(self,dir):
    #     if self.direction * -1 == dir: # if dir is opposite of current, ignore (cannot 180 degree turn)
    #         return
    #     self.direction = dir
    #     print(self.direction)
        
    # def turn_left(self):
    #     self.direction = (self.direction - 1) % 4
    
    # def turn_right(self):
    #     self.direction = (self.direction + 1) % 4
    
