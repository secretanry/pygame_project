import unit_class
import pygame
import path_func


class Start(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.start = pygame.sprite.Sprite()
        self.start_group = pygame.sprite.Group()
        self.start.image = pygame.image.load(path_func.resource_path("res_start.png"))
        self.start.rect = self.start.image.get_rect()
        self.start_group.add(self.start)
        self.width, self.height = self.start.rect.size
        self.rect = self.start.rect
        self.string = 'start'

    def reDraw(self):
        self.start.rect.x = self.x
        self.start.rect.y = self.y
        self.start_group.draw(self.screen)

    def collision(self):
        return 'collide'
