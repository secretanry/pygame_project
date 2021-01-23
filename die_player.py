import unit_class
import pygame
import path_func


class DPlayer(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.dplayer = pygame.sprite.Sprite()
        self.dplayer_group = pygame.sprite.Group()
        self.dplayer.image = pygame.image.load(path_func.resource_path("res_die.png"))
        self.dplayer.rect = self.dplayer.image.get_rect()
        self.dplayer_group.add(self.dplayer)
        self.width, self.height = self.dplayer.rect.size
        self.rect = self.dplayer.rect
        self.string = 'die player'

    def reDraw(self):
        self.dplayer.rect.x = self.x
        self.dplayer.rect.y = self.y
        self.dplayer_group.draw(self.screen)

    def collision(self):
        return None
