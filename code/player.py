import pygame
from settings import *

#making player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('zeldaSouls\graphics\Test\Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #moving the player
        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.obstacle_sprites = obstacle_sprites

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self,speed):
        #have to make movemnet vector of 1 so when moving at angle 
        #the player doesnt move faster
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        #times direction by speed
        self.rect.center += self.direction * speed

    def collision(self,direction):
        if direction == 'horizontal':
            #checking the rectangle (rect) of the player against the obsticle sprites
            for sprite in self.obstacle_sprites:
                #and which sides of sprites rect to check
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            #checking the rectangle (rect) of the player against the obsticle sprites
            for sprite in self.obstacle_sprites:
                #which sides of sprites rect to check
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)
