import player_class
import floor_class
import door
import start
import red_button
import green_button
import green_door
import life
import fire
import pygame


class Level1:
    def __init__(self, screen):
        x = 0
        y = 770
        self.lis = list()
        for i in range(20):
            self.lis.append(floor_class.Floor(x, y, screen))
            x += 75
        self.lis.append(start.Start(75, 748, screen))
        self.lis.append(life.Life(230, 30, screen))
        self.lis.append(life.Life(130, 30, screen))
        self.lis.append(floor_class.Floor(-75, 697, screen))
        self.lis.append(life.Life(30, 30, screen))
        self.lis.append(green_door.GDoor(2000, 2000, screen))
        self.lis.append(door.Door(1200, 581, screen))
        self.lis.append(green_button.GreenButton(2000, 2000, screen))
        self.lis.append(red_button.RedButton(400, 728, screen))
        self.lis.append(player_class.Player(100, 465, screen))

    def get_level(self):
        return self.lis
