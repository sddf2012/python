from random import choice


class RandomWalk:
    def __init__(self):
        self.count = 50000
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        i = len(self.x_values) + 1
        while i <= self.count:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
            i += 1

    def get_step(self):
        direct = choice([-1, 1])
        step = choice([0, 1, 2, 3, 4, 5])
        return direct * step
