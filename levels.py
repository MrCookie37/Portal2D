import sys, pygame
from obstacles import Plateforme_haute 

class level1():
    def __init__(self):
        self.all_plateform=pygame.sprite.Group()
        
    def coord(self,X,Y):
        self.rect.x= X
        self.rect.y= Y
        
    def add_plateform(self):
        self.all_plateform.add(Plateforme_haute(self))
        Plateforme_haute.coord(Plateforme_haute,60,360)