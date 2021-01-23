import pygame


class Unit:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 0

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def reDraw(self):
        pass

    def get_speed(self):
        return self.speed

    def get_coords(self):
        return (self.x, self.y)

    def get_string(self):
        return self.string
