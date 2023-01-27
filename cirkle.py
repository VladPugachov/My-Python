from math import pi, sqrt
class Circle:
    def __init__(self, center, radius):
        if radius < 0:
            raise ValueError('Negative radius')
        self.center = center
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def get_x(self):
        return self.center[0]

    def get_y(self):
        return self.center[1]

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def move(self, new_center):
        self.center = new_center

    def grow(self, d = 1):
        self.radius += d

    def shrink(self, d = 1):
        if self.radius - d >= 0:
            self.radius -= d
        else:
            self.radius = 0

    def distance(self, other):
        dx = self.get_x() - other.get_x()
        dy = self.get_y() - other.get_y()
        return math.sqrt(dx ** 2 + dy ** 2)
    def __str__(self):
        return f'<{self.center[0]}, {self.center[1]}>, {self.radius}'


