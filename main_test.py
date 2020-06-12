import pygame as py
from affichage import*
from classes import *
def jeu() :
  size = (1280,720)
  py.init()
  py.display.set_caption("Portal2D")
  screen=py.display.set_mode(size,py.RESIZABLE)
  roger= Personnage(0, 700, "images/Perso_portal.png",(1, 0), 10, 1)
  background = py.Surface(screen.get_size()).convert()
  background.fill((0, 0, 0))
  en_jeu=True
  menu=False
  on = True
  bouge_gauche = False
  bouge_droite=False
  while on :
    if menu:
      affiche_menu(screen)
    for event in py.event.get():
      if event.type == py.QUIT:
        on = False
      if event.type == py.VIDEORESIZE:
                screen = py.display.set_mode((event.w, event.h),py.RESIZABLE)
      if event.type == py.KEYDOWN:
        if en_jeu:
          if event.unicode == "q":
            bouge_gauche=True
          elif event.unicode == 'd':
            bouge_droite=True
      if event.type == py.KEYUP:
        if en_jeu:
          if event.key == py.K_q:
            bouge_gauche=False
          elif event.key == py.K_d:
            bouge_droite=False

    if bouge_gauche:
      screen.blit(background, roger.position, roger.position)
      roger.move(-1)
      screen.blit(roger.image, roger.position)
    if bouge_droite:
      screen.blit(background, roger.position, roger.position)
      roger.move(1)
      screen.blit(roger.image, roger.position)

    py.display.flip()
  pygame.quit()