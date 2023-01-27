from dice import Dice
class Player:
    def __init__(self, name):
        self.name = name
        self.dice = Dice()
        self.points_sum = 0

    def turn(self):
        self.dice.throw()
        self.point_sum += self.dice.get_value()

    def __str__(self):
        return f"name: {self.name}, value = {self.dice.get_value()}, point sum = {self.point_sum}"
