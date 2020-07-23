from random import randint

class Die():
    """A class for a die"""

    def __init__(self, num_sides=6):
        """die has 6 faces"""
        self.num_sides = num_sides

    def roll(self):
        """return a random number between 1 and num_sides"""
        return randint(1, self.num_sides)
