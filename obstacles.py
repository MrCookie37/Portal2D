import sys, pygame

class Plateforme(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load("plateforme.jpg")
        self.rect= self.image.get_rect()
        self.rect.x= 600
        self.rect.y= 590
        
class Plateforme_sol():
    def __init__(self):
        self.image= pygame.image.load("wall3.jpg")
        self.image= pygame.transform.scale(self.image,(1080,30))
        self.rect= self.image.get_rect()
        self.rect.x= 0
        self.rect.y= 690
        self.cord_taille_x=(self.rect.x,self.rect.x+self.rect.width)
        self.cord_taille_y=(self.rect.y,self.rect.y+self.rect.height)
    def coord(self,X,Y):
        self.rect.x= X
        self.rect.y= Y
        
class Plateforme_haute(pygame.sprite.Sprite):
    def __init__(self):
        self.image= pygame.image.load("wall3.jpg")
        self.image= pygame.transform.scale(self.image,(30,500))
        self.rect= self.image.get_rect()
        self.rect.x= 0
        self.rect.y= 690
        self.cord_taille_x=(self.rect.x,self.rect.x+self.rect.width)
        self.cord_taille_y=(self.rect.y,self.rect.y+self.rect.height)
    def coord(self,X,Y):
        self.rect.x= X
        self.rect.y= Y