import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 48))
        self.image.fill('Green')
        self.rect = self.image.get_rect(topleft=pos)
        
        self.dir = pygame.math.Vector2(0,0)
        
        # Player Stats
        self.speed = 6 
        self.gravity = 0.7
        self.jump_speed = -14
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.dir.x = 1
        elif keys[pygame.K_a]:
            self.dir.x = -1
        else:
             self.dir.x = 0
             
        if keys[pygame.K_w]:
            self.jump()
    
    def apply_gravity(self):
        self.dir.y += self.gravity
        self.rect.y += self.dir.y
        
    def jump(self):
        self.dir.y = self.jump_speed
        
        
    def update(self):
        self.get_input()