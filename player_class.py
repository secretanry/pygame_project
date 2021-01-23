import unit_class
import pygame
import os
import path_func

class Player(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.speed = 240
        self.player = pygame.sprite.Sprite()
        self.player_group = pygame.sprite.Group()
        self.player.image = pygame.image.load(path_func.resource_path('res_unit.png'))
        self.player.rect = self.player.image.get_rect()
        self.player_group.add(self.player)
        self.height = self.player.rect.height
        self.width = self.player.rect.width
        self.rect = self.player.rect
        self.string = 'player'
        self.counter = 0
        self.reserv_x = 0
        self.reserv_y = 0

    def reDraw(self):
        self.player.rect.x = self.x
        self.player.rect.y = self.y
        self.player_group.draw(self.screen)

    def collision(self):
        return None
