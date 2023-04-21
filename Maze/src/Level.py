import pygame 
from Tiles import Tiles
from settings import *
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)
        
        self.world_shift = 0
    
    
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
        level_border = 0
        
        if player_x < ((WIDTH / 2) - 140) and dir_x < 0:
            self.world_shift = 6
            player.speed = 0
        elif player_x > ((WIDTH / 2) + 140) and dir_x > 0: 
            self.world_shift = -6
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 6
        
    def scroll_y(self):
        pass
        
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
        
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.scroll_y()
        
        # Player
        self.player.update()
        self.horizontal_movement_check()
        self.vertical_movement_check()
        self.player.draw(self.display_surface)