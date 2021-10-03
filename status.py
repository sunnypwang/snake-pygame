import pygame


class Status:
    def __init__(self,board,x,y,width, height):
        self.board = board
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, window):
        pygame.draw.rect(window, "gray", (self.x,self.y,self.width,self.height))
        
        #score
        score = self.board.score
        myfont = pygame.font.Font('assets/upheavtt.ttf', 40)
        textsurface = myfont.render(str(score), False, (0, 0, 0))
        window.blit(textsurface,(self.x + self.width/2,self.y + self.height/4))
        