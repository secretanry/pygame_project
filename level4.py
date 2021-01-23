import floor_class
import start
import player_class
import cube
import red_button
import green_button
import green_door
import door
import shadow_block
import life
import die_player
import fire


class Level4:
    def __init__(self, screen, col_life):
        x = 0
        self.col_life = col_life
        y = 770
        self.lis = list()
        for i in range(16):
            self.lis.append(floor_class.Floor(x, y, screen))
            x += 75
        x -= 75
        self.lis.append(floor_class.Floor(x, 695, screen))
        self.lis.append(floor_class.Floor(x, 620, screen))
        self.lis.append(floor_class.Floor(x, 545, screen))
        for i in range(4):
            x += 75
            self.lis.append(floor_class.Floor(x, 545, screen))
        self.lis.append(fire.Fire(x - 10, 516, screen))
        self.lis.append(cube.Cube(250, 684, screen))
        self.lis.append(cube.Cube(336, 684, screen))
        self.lis.append(cube.Cube(422, 684, screen))
        self.lis.append(cube.Cube(508, 684, screen))
        self.lis.append(cube.Cube(336, 598, screen))
        self.lis.append(cube.Cube(422, 598, screen))
        self.lis.append(fire.Fire(700, 741, screen))
        self.lis.append(fire.Fire(771, 741, screen))
        self.lis.append(fire.Fire(862, 741, screen))
        self.lis.append(fire.Fire(933, 741, screen))
        self.lis.append(fire.Fire(1004, 741, screen))
        self.lis.append(start.Start(75, 748, screen))
        if self.col_life == 3:
            self.lis.append(life.Life(230, 30, screen))
            self.lis.append(life.Life(130, 30, screen))
            self.lis.append(life.Life(30, 30, screen))
        elif self.col_life == 2:
            self.lis.append(life.Life(130, 30, screen))
            self.lis.append(life.Life(30, 30, screen))
        elif self.col_life == 1:
            self.lis.append(life.Life(30, 30, screen))
        self.lis.append(shadow_block.SBlock(600, 500, screen))
        self.lis.append(shadow_block.SBlock(860, 400, screen))
        self.lis.append(die_player.DPlayer(2000, 2000, screen))
        self.lis.append(green_door.GDoor(2000, 2000, screen))
        self.lis.append(door.Door(1300, 356, screen))
        self.lis.append(green_button.GreenButton(2000, 2000, screen))
        self.lis.append(red_button.RedButton(620, 721, screen))
        self.lis.append(player_class.Player(100, 465, screen))

    def get_level(self):
        return self.lis
