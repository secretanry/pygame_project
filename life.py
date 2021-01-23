import unit_class
import pygame
import path_func


class Life(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.life = pygame.sprite.Sprite()
        self.life_group = pygame.sprite.Group()
        self.life.image = pygame.image.load(path_func.resource_path("res_life.png"))
        self.life.rect = self.life.image.get_rect()
        self.life_group.add(self.life)
        self.width, self.height = self.life.rect.size
        self.rect = self.life.rect
        self.reserv_x = self.x
        self.reserv_y = self.y
        self.string = 'life'

    def reDraw(self):
        self.life.rect.x = self.x
        self.life.rect.y = self.y
        self.life_group.draw(self.screen)

    def collision(self):
        return None
