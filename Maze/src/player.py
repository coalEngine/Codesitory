import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((24, 24))
        self.image.fill('Green')
        self.rect = self.image.get_rect(topleft=pos)
        self.dir = pygame.Vector2