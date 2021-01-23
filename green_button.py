import unit_class
import pygame
import path_func


class GreenButton(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.gbutton = pygame.sprite.Sprite()
        self.gbutton_group = pygame.sprite.Group()
        self.gbutton.image = pygame.image.load(path_func.resource_path("res_green_button.png"))
        self.gbutton.rect = self.gbutton.image.get_rect()
        self.gbutton_group.add(self.gbutton)
        self.width, self.height = self.gbutton.rect.size
        self.rect = self.gbutton.rect
        self.string = 'green button'

    def reDraw(self):
        self.gbutton.rect.x = self.x
        self.gbutton.rect.y = self.y
        self.gbutton_group.draw(self.screen)

    def collision(self):
        return None
