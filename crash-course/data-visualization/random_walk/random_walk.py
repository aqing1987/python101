from random import choice

class RandomWalk():
    """a class for generating random walk"""

    def __init__(self, num_points = 5000):
        """init random walk attributes"""
        self.num_points = num_points

        # all random walk starts from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """compute all points for random walk"""

        # random walk until reach the pointed number of points
        while len(self.x_values) < self.num_points:
            # decide direction and distance
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # don't stay at (0, 0)
            if x_step == 0 and y_step == 0:
                continue

            # compute next point (x, y)
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
