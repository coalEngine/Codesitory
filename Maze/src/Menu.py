import pygame
from settings import *
from Level import Level

class Menu:
    def __init__(self):
        pygame.init()
        
    def Run():
         play_img = pygame.image.load("Maze/img/play_button.png").convert_alpha()
         play_button = Button(WIDTH // 2 - 147, HEIGHT // 2 - 100, play_img, 0.5)
         level = Level(world_1_level1, screen)

         screen.fill(BLACK)
         screen.blit(menu_text, menu_text_rect)
         clock.tick(60)
         if play_button.draw(screen):
            level.init()