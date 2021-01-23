import player_class
import floor_class
import door
import fire
import start
import cube
import flat
import red_button
import green_button
import green_door
import life
import die_player
import pygame


class Level3:
    def __init__(self, screen, col_life):
        self.lis = []
        self.col_life = col_life
        self.lis.append(floor_class.Floor(0, 600, screen))
        self.lis.append(floor_class.Floor(75, 600, screen))
        self.lis.append(floor_class.Floor(150, 600, screen))
        self.lis.append(floor_class.Floor(225, 600, screen))
        self.lis.append(floor_class.Floor(225, 675, screen))
        self.lis.append(floor_class.Floor(225, 750, screen))
        self.lis.append(floor_class.Floor(300, 750, screen))
        x = 300
        for i in range(11):
            self.lis.append(floor_class.Floor(x, 750, screen))
            x += 75
        self.lis.append(floor_class.Floor(x, 750, screen))
        self.lis.append(floor_class.Floor(x, 675, screen))
        self.lis.append(floor_class.Floor(x, 600, screen))
        for i in range(5):
            self.lis.append(floor_class.Floor(x, 600, screen))
            x += 75
        self.lis.append(fire.Fire(300, 717, screen))
        self.lis.append(fire.Fire(381, 717, screen))
        self.lis.append(cube.Cube(462, 664, screen))
        self.lis.append(cube.Cube(548, 664, screen))
        self.lis.append(cube.Cube(773, 664, screen))
        self.lis.append(cube.Cube(859, 664, screen))
        self.lis.append(cube.Cube(945, 664, screen))
        self.lis.append(fire.Fire(945, 635, screen))
        self.lis.append(cube.Cube(859, 578, screen))
        self.lis.append(flat.Flat(640, 430, screen))
        self.lis.append(start.Start(75, 578, screen))
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
        self.lis.append(door.Door(1350, 420, screen))
        self.lis.append(green_button.GreenButton(2000, 2000, screen))
        self.lis.append(red_button.RedButton(670, 381, screen))
        self.lis.append(player_class.Player(100, 415, screen))

    def get_level(self):
        return self.lis
