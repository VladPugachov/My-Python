class Dice:
    def __init__(self):
        self.value = 1

    def get_value(self):
        return self.value

    def throw(self):
        from random import randint
        self.value = randint(1, 6)
