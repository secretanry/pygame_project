import unit_class
import pygame
import path_func


class Cube(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.cube = pygame.sprite.Sprite()
        self.cube_group = pygame.sprite.Group()
        self.cube.image = pygame.image.load(path_func.resource_path("res_cube.png"))
        self.cube.rect = self.cube.image.get_rect()
        self.cube_group.add(self.cube)
        self.width, self.height = self.cube.rect.size
        self.rect = self.cube.rect
        self.string = 'cube'

    def reDraw(self):
        self.cube.rect.x = self.x
        self.cube.rect.y = self.y
        self.cube_group.draw(self.screen)

    def collision(self):
        return 'collide'
