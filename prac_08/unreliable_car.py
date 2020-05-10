"""
CP1404 Practical
Unreliable Car class
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """A version of Car with an unreliable factor"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if randint(1, 100) < self.reliability:
            super().drive(distance)
        else:
            return 0
