import unit_class
import pygame
import path_func


class Fire(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.fire = pygame.sprite.Sprite()
        self.fire_group = pygame.sprite.Group()
        self.fire.image = pygame.image.load(path_func.resource_path("res_fire.png"))
        self.fire.rect = self.fire.image.get_rect()
        self.fire_group.add(self.fire)
        self.width, self.height = self.fire.rect.size
        self.rect = self.fire.rect
        self.string = 'fire'

    def reDraw(self):
        self.fire.rect.x = self.x
        self.fire.rect.y = self.y
        self.fire_group.draw(self.screen)

    def collision(self):
        return 'minus'
