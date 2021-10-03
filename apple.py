import random

import pygame

class AppleControl:
    def __init__(self, board):
        self.pos = None

    def spawn_apple(self,free):
        if free:
            idx = random.randint(0, len(free)-1)
            pos = free[idx]
            self.pos = pos
            return pos
        
    def locate_apple(self):
        return self.pos
    
    def draw(self, window, grid_size,x, y):
        if self.pos:
            pygame.draw.rect(window, "red", (x+self.pos[0]*grid_size,y+self.pos[1]*grid_size,grid_size,grid_size))  
        
    def destroy_apple(self):
        self.pos = None