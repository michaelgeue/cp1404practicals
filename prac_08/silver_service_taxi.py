"""
CP1404 Practical
Silver Service Taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfare = 4.50

    def __init__(self, name, fuel, fanciness=1.00):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * super().price_per_km

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfare)

    def get_fare(self):
        """Return the price for the taxi trip, including flagfare."""
        return self.flagfare + super().get_fare()

