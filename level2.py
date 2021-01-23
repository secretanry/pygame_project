import player_class
import floor_class
import door
import start
import red_button
import green_button
import fire
import green_door
import cube
import flat
import life
import die_player
import pygame


class Level2:
    def __init__(self, screen, col_life):
        x = 0
        y = 770
        self.col_life = col_life
        self.lis = list()
        for i in range(20):
            self.lis.append(floor_class.Floor(x, y, screen))
            x += 75
        self.lis.append(start.Start(75, 748, screen))
        self.lis.append(fire.Fire(200, 737, screen))
        self.lis.append(fire.Fire(900, 737, screen))
        self.lis.append(fire.Fire(981, 737, screen))
        self.lis.append(cube.Cube(500, 684, screen))
        self.lis.append(cube.Cube(586, 684, screen))
        self.lis.append(cube.Cube(586, 598, screen))
        self.lis.append(cube.Cube(672, 684, screen))
        self.lis.append(cube.Cube(672, 598, screen))
        self.lis.append(cube.Cube(758, 684, screen))
        self.lis.append(fire.Fire(758, 655, screen))
        self.lis.append(flat.Flat(930, 500, screen))
        if self.col_life == 3:
            self.lis.append(life.Life(230, 30, screen))
            self.lis.append(life.Life(130, 30, screen))
            self.lis.append(life.Life(30, 30, screen))
        elif self.col_life == 2:
            self.lis.append(life.Life(130, 30, screen))
            self.lis.append(life.Life(30, 30, screen))
        elif self.col_life == 1:
            self.lis.append(life.Life(30, 30, screen))
        self.lis.append(die_player.DPlayer(2000, 2000, screen))
        self.lis.append(green_door.GDoor(2000, 2000, screen))
        self.lis.append(door.Door(1300, 581, screen))
        self.lis.append(green_button.GreenButton(2000, 2000, screen))
        self.lis.append(red_button.RedButton(1005, 452, screen))
        self.lis.append(player_class.Player(100, 465, screen))

    def get_level(self):
        return self.lis