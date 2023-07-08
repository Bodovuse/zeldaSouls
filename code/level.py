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
        self.visible_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

#camera
#sorting sprites by their y coord (this decides sprites being infront/behind)
#offset the world to wherever the player is
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general set up
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100,200)

    def custom_draw(self, player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)