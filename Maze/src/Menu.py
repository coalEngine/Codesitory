import pygame
from settings import *
from Level import Level

class Menu:
    def __init__(self):
        pygame.init()
        
    def Run():
         screen.fill(BLACK)
         screen.blit(menu_text, menu_text_rect)
         clock.tick(60)