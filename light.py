import unit_class
import pygame
import path_func


class Light(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.light = pygame.sprite.Sprite()
        self.light_group = pygame.sprite.Group()
        self.light.image = pygame.image.load(path_func.resource_path(path_func.resource_path("res_red_door.png")))
        self.light.rect = self.light.image.get_rect()
        self.light_group.add(self.light)
        self.width, self.height = self.light.rect.size
        self.rect = self.light.rect
        self.string = 'light'

    def reDraw(self):
        self.light.rect.x = self.x
        self.light.rect.y = self.y
        self.light_group.draw(self.screen)

    def collision(self):
        return 'die'
