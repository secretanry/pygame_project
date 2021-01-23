import unit_class
import pygame
import path_func


class Flat(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.flat = pygame.sprite.Sprite()
        self.flat_group = pygame.sprite.Group()
        self.flat.image = pygame.image.load(path_func.resource_path("res_flat.png"))
        self.flat.rect = self.flat.image.get_rect()
        self.flat_group.add(self.flat)
        self.width, self.height = self.flat.rect.size
        self.rect = self.flat.rect
        self.string = 'flat'

    def reDraw(self):
        self.flat.rect.x = self.x
        self.flat.rect.y = self.y
        self.flat_group.draw(self.screen)

    def collision(self):
        return 'collide'
