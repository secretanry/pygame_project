import unit_class
import pygame
import path_func


class Floor(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.floor = pygame.sprite.Sprite()
        self.floor_group = pygame.sprite.Group()
        self.floor.image = pygame.image.load(path_func.resource_path("res_down.png"))
        self.floor.rect = self.floor.image.get_rect()
        self.floor_group.add(self.floor)
        self.width, self.height = self.floor.rect.size
        self.rect = self.floor.rect
        self.string = 'floor'

    def reDraw(self):
        self.floor.rect.x = self.x
        self.floor.rect.y = self.y
        self.floor_group.draw(self.screen)

    def collision(self):
        return 'collide'
