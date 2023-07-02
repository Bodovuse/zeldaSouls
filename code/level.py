import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        # get the display surface (self.screen)
        self.display_surface = pygame.display.get_surface()

        # sprite group et up
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        # converting the world map into a position
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                # putting rock sprite on map
                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                #place player on map
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites],self.obstacle_sprites)

    def run(self):
        # update and draw game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
