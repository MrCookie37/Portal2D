import pygame as py

def affiche_menu(screen):
  font=py.font.SysFont("Arial",40,True,False)
  text=font.render("options",1,(255,255,255))
  screen.blit(text, (screen.get_width()//2-50,screen.get_height()//2))

def affiche_niveau(screen):
  pass