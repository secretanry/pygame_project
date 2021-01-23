import unit_class
import pygame
import path_func


class SBlock(unit_class.Unit):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.sblock = pygame.sprite.Sprite()
        self.sblock_group = pygame.sprite.Group()
        self.reserv_x = self.x
        self.reserv_y = self.y
        self.counter = 0
        self.sblock.image = pygame.image.load(path_func.resource_path("res_shadow_block.png"))
        self.sblock.rect = self.sblock.image.get_rect()
        self.sblock_group.add(self.sblock)
        self.width, self.height = self.sblock.rect.size
        self.rect = self.sblock.rect
        self.string = 'shadow block'

    def reDraw(self):
        self.sblock.rect.x = self.x
        self.sblock.rect.y = self.y
        self.sblock_group.draw(self.screen)

    def collision(self):
        return 'collide and go out'
