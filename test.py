from point import Point
from rectangle import Rectangle

p1 = Point()
p2 = Point(10, 8)
p3 = Point(-15, -20)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")
print(f"p1 attalims lidz centram: {p1.distance_from_origin()}")
print(f"p2 attalims lidz centram: {p2.distance_from_origin()}")
print(f"p1 attalums lidz p2: {p1.distance(p2)}")
box_1 = Rectangle()
box_2 = Rectangle(w=4, h=6)
box_3 = Rectangle(p2)
box_4 = Rectangle(Point(10, 10), 4, 6)
print(f"box_1: {box_1}")
print(f"box_2: {box_2}")
print(f"box_3: {box_3}")
print(f"box_4: {box_4}")

p2.set_x(3)
p2.set_y(5)
print(f"p2: {p2}")
print(f"box_3: {box_3}")
box_3.grow(5, 7)
print(f"box_3: {box_3}")
box_3.move(2, 2)
print(f"box_3: {box_3}")

