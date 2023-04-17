import pygame
from settings import *

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = screen
        self.clock = clock

    
    def Run():
         screen.fill("Black")
         screen.blit(menu_text, menu_text_rect)
         clock.tick(60)