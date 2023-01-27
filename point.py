class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.x

    def distance_from_origin(self):
        from math import sqrt
        return  sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other_point):
        from math import sqrt
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return sqrt(dx ** 2 + dy ** 2)


    def __str__(self):
        return f"({self.x}, {self.y})"
