import pygame
from settings import *

class Button:
    def __init__(self, x, y, image, scale):
        pygame.init()
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, screen_ref):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)

        screen_ref.blit(self.image, (self.x, self.y))
        return action