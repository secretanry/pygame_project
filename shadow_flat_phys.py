class ShadowFlatPhys:
    def __init__(self, unit, fps):
        self.unit = unit
        self.fps = fps
        self.flag = False

    def process(self):
        self.unit.counter += 1
        if self.unit.counter == self.fps:
            if self.unit.x == 2000 and self.unit.y == 2000:
                self.unit.x = self.unit.reserv_x
                self.unit.y = self.unit.reserv_y
                self.flag = False
            else:
                if self.flag:
                    self.unit.x = 2000
                    self.unit.y = 2000
                    self.flag = False
                    self.unit.counter = 0

    def nast(self):
        self.flag = True
        if self.unit.counter >= self.fps:
            self.unit.counter = 0

    def get_unit(self):
        return self.unit
