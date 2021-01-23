import unit_class
import pygame
import path_func


class Door(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.door = pygame.sprite.Sprite()
        self.door_group = pygame.sprite.Group()
        self.door.image = pygame.image.load(path_func.resource_path("res_red_door.png"))
        self.door.rect = self.door.image.get_rect()
        self.door_group.add(self.door)
        self.width, self.height = self.door.rect.size
        self.rect = self.door.rect
        self.string = 'red door'

    def reDraw(self):
        self.door.rect.x = self.x
        self.door.rect.y = self.y
        self.door_group.draw(self.screen)

    def collision(self):
        return None
