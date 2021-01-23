import unit_class


class Physics:
    def __init__(self, unit, fps):
        self.unit = unit
        self.fps = fps
        self.direction = 0
        self.initialization_v = 1000
        self.a = 50
        self.x, self.y = self.unit.get_coords()
        self.v = 0
        self.flag = False
        self.dead = False
        self.counter_started = False

    def go_forward(self):
        if not self.counter_started:
            self.direction = 1

    def go_back(self):
        if not self.counter_started:
            self.direction = -1

    def stop(self):
        self.direction = 0

    # def block_down(self, px):
    #     if self.v <= 0:
    #         self.v = 0
    #     self.y += px
    #     self.unit.set_coords(round(self.x), round(self.y))
    #
    # def block_up(self, px):
    #     if self.v >= 0:
    #         self.v = 0
    #     self.y += px
    #     self.unit.set_coords(round(self.x), round(self.y))

    def block_vert(self, px):
        if px > 0:
            if self.v <= 0:
                self.v = 0
            px -= 1
        else:
            if self.v >= 0:
                self.v = 0
            px += 1
        self.y -= px
        self.unit.set_coords(round(self.x), round(self.y))

    def block_horiz(self, px):
        self.stop()
        if px > 0:
            px -= 1
        else:
            px += 1
        self.x -= px
        self.unit.set_coords(round(self.x), round(self.y))

    # def block_right(self, px):
    #     self.stop()
    #     self.x += px
    #     self.unit.set_coords(round(self.x), round(self.y))
    #
    # def block_left(self, px):
    #     self.stop()
    #     self.x += px
    #     self.unit.set_coords(round(self.x), round(self.y))

    def jump(self):
        if not self.flag:
            if self.v == 0:
                self.v = self.initialization_v

    def process(self):
        self.unit.counter += 1
        if not self.dead:
            v = self.unit.get_speed()
            s = v / self.fps * self.direction
            self.x += s
            self.y -= self.v / self.fps
            self.v -= self.a
            self.unit.set_coords(round(self.x), round(self.y))
        if self.unit.counter == 2 * self.fps and self.counter_started:
            self.flag = True
            self.dead = False

    def get_unit(self):
        return self.unit

    def die(self):
        self.counter_started = True
        self.flag = False
        self.dead = True
        self.unit.counter = 0

    def refr_flag(self):
        self.flag = False
        self.counter_started = False
