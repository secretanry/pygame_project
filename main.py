import player_class
import floor_class
import pygame
import physics
import level1
import level2
import level3
import level4
import shadow_flat_phys
import sys
import os
import path_func


class Game:
    def __init__(self, screen, fps):
        self.screen = screen
        self.fps = fps
        self.col_life = 3
        self.phys_list = []
        self.list_level = [self.create_level1, self.create_level2, self.create_level3, self.create_level4]
        self.curr_level = 0
        self.list_level[self.curr_level]()
        self.flag = False
        self.minus_life = False
        self.game_over = False
        self.win = False

    def die(self):
        self.unit.reserv_x = self.unit.x
        self.unit.reserv_y = self.unit.y
        res_y = self.unit.reserv_y + self.unit.height
        self.unit.set_coords(3000, 3000)
        for i in self.object_list:
            if i.string == 'die player':
                self.d = i
                i.set_coords(self.unit.reserv_x, res_y - self.d.height)
        self.phys.die()

    def create_level1(self):
        self.minus_life = False
        level = level1.Level1(self.screen)
        self.phys_list = []
        self.object_list = level.get_level()
        self.phys = physics.Physics(self.object_list[-1], self.fps)
        self.phys_list.append(self.phys)
        for i in self.object_list:
            if i.get_string() == 'shadow block':
                self.phys_list.append(shadow_flat_phys.ShadowFlatPhys(i, self.fps))
        self.unit = self.object_list[-1]

    def create_level2(self):
        self.minus_life = False
        level = level2.Level2(self.screen, self.col_life)
        self.phys_list = []
        self.object_list = level.get_level()
        self.phys = physics.Physics(self.object_list[-1], self.fps)
        self.phys_list.append(self.phys)
        for i in self.object_list:
            if i.get_string() == 'shadow block':
                self.phys_list.append(shadow_flat_phys.ShadowFlatPhys(i, self.fps))
        self.unit = self.object_list[-1]

    def create_level3(self):
        self.minus_life = False
        level = level3.Level3(self.screen, self.col_life)
        self.phys_list = []
        self.object_list = level.get_level()
        self.phys = physics.Physics(self.object_list[-1], self.fps)
        self.phys_list.append(self.phys)
        for i in self.object_list:
            if i.get_string() == 'shadow block':
                self.phys_list.append(shadow_flat_phys.ShadowFlatPhys(i, self.fps))
        self.unit = self.object_list[-1]

    def create_level4(self):
        self.minus_life = False
        level = level4.Level4(self.screen, self.col_life)
        self.phys_list = []
        self.object_list = level.get_level()
        self.phys = physics.Physics(self.object_list[-1], self.fps)
        self.phys_list.append(self.phys)
        for i in self.object_list:
            if i.get_string() == 'shadow block':
                self.phys_list.append(shadow_flat_phys.ShadowFlatPhys(i, self.fps))
        self.unit = self.object_list[-1]

    def process(self):
        if self.phys.flag:
            self.d.set_coords(3000, 3000)
            self.list_level[self.curr_level]()
            self.phys.refr_flag()
        for i in self.phys_list:
            i.process()
        self.detect_collision()
        for u in self.object_list:
            if u.string == 'life' and u.x == 2000:
                pass
            else:
                u.reDraw()

    def collide_rect(self, s1, s2):
        if s1 == s2:
            return False
        x1 = s1.x
        x2 = s2.x
        if x2 <= x1:
            resx = x1 - x2 <= s2.width
        else:
            resx = x2 - x1 <= s1.width
        y1 = s1.y
        y2 = s2.y
        if y2 < y1:
            resy = y1 - y2 <= s2.height
        else:
            resy = y2 - y1 <= s1.height
        return resx and resy

    def full_collision(self, s1, s2):
        return s2.x <= s1.x and s1.x + s1.width <= s2.x + s2.width

    def process_collide(self, item):
        dx = self.unit.x + self.unit.width - item.x
        if dx > self.unit.width or dx < 0:
            dx = self.unit.x - item.x - item.width
            if abs(dx) > self.unit.width or dx > 0:
                dx = 0
            else:
                dx -= 1
        else:
            dx += 1
        dy = self.unit.y + self.unit.height - item.y
        if dy > self.unit.height / 2 or dy < 0:
            dy = self.unit.y - item.y - item.height
            if abs(dy) > self.unit.height / 2 or dy > 0:
                dy = 0
            else:
                dy -= 1
        else:
            dy += 1
        if dx * dy != 0:
            if abs(dx) < abs(dy):
                self.phys.block_horiz(dx)
            else:
                self.phys.block_vert(dy)
        else:
            if dx != 0:
                self.phys.block_horiz(dx)
            elif dy != 0:
                self.phys.block_vert(dy)

    def detect_collision(self):
        for i in self.object_list:
            if self.collide_rect(self.unit, i):
                act = i.collision()
                if act == 'collide':
                    self.process_collide(i)
                elif act == 'push button':
                    x = self.object_list[-2].x
                    y = self.object_list[-2].y
                    self.object_list[-2].set_coords(self.object_list[-3].x, self.object_list[-3].y)
                    self.object_list[-3].set_coords(x, y)
                    x = self.object_list[-4].x
                    y = self.object_list[-4].y
                    self.object_list[-4].set_coords(self.object_list[-5].x, self.object_list[-5].y)
                    self.object_list[-5].set_coords(x, y)
                elif act == 'next lvl':
                    if self.full_collision(self.unit, self.object_list[-5]):
                        self.curr_level += 1
                        if self.curr_level == 4:
                            self.win = True
                        self.col_life = 3
                        if self.curr_level != 4:
                            self.list_level[self.curr_level]()
                elif act == 'collide and go out':
                    self.process_collide(i)
                    for u in self.phys_list:
                        if u.get_unit() == i:
                            u.nast()
                elif act == 'minus':
                    for u in self.object_list:
                        if u.string == 'life':
                            if u.x != 2000 and not self.minus_life:
                                self.die()
                                self.minus_life = True
                                u.x = 2000
                                u.y = 2000
                                self.col_life -= 1
                                if self.col_life == 0:
                                    self.game_over = True

    def go_left(self):
        self.phys.go_back()

    def go_right(self):
        self.phys.go_forward()

    def jump(self):
        self.phys.jump()

    def stop(self):
        self.phys.stop()


if __name__ == '__main__':
    size = width, height = 1500, 980
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    counter = 30
    pygame.init()
    pygame.display.set_caption('30 seconds to escape')
    text = '30'.rjust(3)
    font = pygame.font.SysFont('serif', 60)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    background = pygame.image.load(path_func.resource_path("back.png")).convert()
    win = pygame.image.load(path_func.resource_path("you_win.png")).convert()
    ma = Game(screen, fps)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3)
                if counter == 0 and not ma.win:
                    ma.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ma.go_left()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ma.go_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ma.stop()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ma.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ma.jump()
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        if not ma.game_over and not ma.win:
            screen.blit(background, [0, 135])
            screen.blit(font.render(text, True, (255, 255, 255)), (1280, 35))
            ma.process()
            clock.tick(fps)
            pygame.display.flip()
        elif ma.game_over:
            text = 'Game over!'
            font = pygame.font.SysFont('consolas', 100)
            screen.blit(font.render(text, True, (255, 255, 255)), (500, 400))
            pygame.display.flip()
        elif ma.win:
            screen.fill((0, 0, 0))
            screen.blit(win, [520, 300])
            pygame.display.flip()
    pygame.quit()

