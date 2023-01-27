from point import Point
class Rectangle:
    def __init__(self, pos=Point(), w=1, h=1):
        self.corner = pos
        self.width = w
        self.height = h

    def grow(self, delta_width=1, delta_height=1):
        self.width += delta_width
        self.height += delta_height

    def move(self, delta_x, delta_y):
        new_x = self.corner.get_x() + delta_x
        new_y = self.corner.get_y() + delta_y
        self.corner.set_x(new_x)
        self.corner.set_y(new_y)

        self.corner.set_x(self.corner.get_x() + delta_x)
        self.corner.set_y(self.corner.get_y() + delta_y)

    def contains(self, other_point):
        pass

    def overlap(self, other_rectangle):
        pass

    def __str__(self):
        return f"({self.corner}, {self.width}, {self.height})"

