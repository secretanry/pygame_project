import unit_class
import pygame
import path_func


class RedButton(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.rbutton = pygame.sprite.Sprite()
        self.rbutton_group = pygame.sprite.Group()
        self.rbutton.image = pygame.image.load(
            path_func.resource_path("res_red_button.png"))
        self.rbutton.rect = self.rbutton.image.get_rect()
        self.rbutton_group.add(self.rbutton)
        self.width, self.height = self.rbutton.rect.size
        self.rect = self.rbutton.rect
        self.string = 'red button'

    def reDraw(self):
        self.rbutton.rect.x = self.x
        self.rbutton.rect.y = self.y
        self.rbutton_group.draw(self.screen)

    def collision(self):
        return 'push button'
