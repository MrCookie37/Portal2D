import pygame as py

class objet() :
  def __init__(self, x, y, image, direction):
    self.image = py.image.load(image).convert()
    self.image = py.transform.scale(self.image,(120,150))
    self.position = self.image.get_rect().move(x, y)
    self.direction = direction

class Personnage(objet):
  def __init__(self, x, y, image, direction,dx,dy):
    objet.__init__(self, x, y, image, direction)
    self.famille = "personnage"
    self.dx = dx
    self.dy = dy
  
  def viser(self):
    mouse_x,mouse_y=py.mouse.get_pos()
    norme = ((mouse_x-self.x)**2+(mouse_y-self.y)**2)**0.5
    self.direction=(mouse_x-self.x)/norme,mouse_y-self.y/norme

  def move(self, a):
    self.position = self.position.move(a*self.dx, 0)



  def jump(self):#if event.type=KEYDOWN and personnage.dy!=0 : jump()
    self.vitesse+=(0,1)

  def shoot(self):
    pass

  def actionner():
    pass

class cube(objet):

  def __init__(self, x, y, image):
    objet.__init__(x, y, "cube.png", (1, 0))
    self.famille = "cube"
  
class interrupteur(objet):
  def __init__(self, x, y, image):
    objet.__init__(x, y, "interrupteur.png", (1, 0))
    self.famille = "interrupteur"

