import pygame 
from Tiles import Tiles
from settings import *
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)
        
        self.world_shift_x = 0
        self.world_shift_y = 0
    
    
    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x, y = (col_index * tile_size), (row_index * tile_size)
                if col == 'X':
                    tile = Tiles((x, y), tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        dir_x = player.dir.x
        
        if player_x < ((WIDTH / 2) - 140) and dir_x < 0:
            self.world_shift_x = 6
            player.speed = 0
        elif player_x > ((WIDTH / 2) + 140) and dir_x > 0: 
            self.world_shift_x = -6
            player.speed = 0
        else: 
            self.world_shift_x = 0
            player.speed = 6
        
    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        dir_y = player.dir.y
        
        if player_y < ((HEIGHT / 2)) and dir_y < 0:
            self.world_shift_y = 6
        elif player_y > ((HEIGHT / 2)) and dir_y > 0:
            self.world_shift_y = -6
        else:
            self.world_shift_y = 0
            
    def horizontal_movement_check(self):
        player = self.player.sprite
        player.rect.x += player.dir.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.dir.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.dir.x > 0:
                    player.rect.right = sprite.rect.left
                    
    def vertical_movement_check(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.dir.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.dir.y = 0
                elif player.dir.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.dir.y = 0
                    
    def init(self):
        
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        # Player
        self.player.update()
        self.horizontal_movement_check()
        self.vertical_movement_check()
        self.player.draw(self.display_surface)