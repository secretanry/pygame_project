import unit_class
import pygame
import path_func


class GDoor(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.gdoor = pygame.sprite.Sprite()
        self.gdoor_group = pygame.sprite.Group()
        self.gdoor.image = pygame.image.load(path_func.resource_path("res_green_door.png"))
        self.gdoor.rect = self.gdoor.image.get_rect()
        self.gdoor_group.add(self.gdoor)
        self.width, self.height = self.gdoor.rect.size
        self.rect = self.gdoor.rect
        self.string = 'green_door'

    def reDraw(self):
        self.gdoor.rect.x = self.x
        self.gdoor.rect.y = self.y
        self.gdoor_group.draw(self.screen)

    def collision(self):
        return 'next lvl'
